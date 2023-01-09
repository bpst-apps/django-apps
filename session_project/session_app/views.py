from django.shortcuts import render
from django.http import HttpResponse
from session_app.forms import ItemForm


def home(request):
    request.session.set_test_cookie()
    raise Exception('some error has occurred')
    return HttpResponse("<h1>Home Page</h1>")


def new_page(request):
    if request.session.test_cookie_worked():
        print("cookies are enabled")
        request.session.delete_test_cookie()
    return HttpResponse("<h1>New Page</h1>")


def view_counter(request):
    if 'view_count' in request.COOKIES:
        view_count = int(request.COOKIES['view_count']) + 1
    else:
        view_count = 1
    view_response = render(request, 'view_count.html', {'view_count': view_count})
    view_response.set_cookie('view_count', view_count)
    return view_response


def products_home(request):
    return render(request, 'products_home.html')


def add_product(request):
    product_form = ItemForm()
    view_response = render(request, 'add_product.html', {'product_form': product_form})
    if request.method == 'POST':
        filled_form = ItemForm(request.POST)
        if filled_form.is_valid():
            product_name = filled_form.cleaned_data['product_name']
            product_quantity = filled_form.cleaned_data['product_quantity']
            view_response.set_cookie(product_name, product_quantity, 120)
    return view_response


def view_products(request):
    return render(request, 'view_products.html')


def view_counter_session_api(request):
    view_count = request.session.get('view_count', 0)
    view_count += 1
    request.session['view_count'] = view_count
    return render(request, 'view_count_session.html', {'view_count': view_count})


def products_home_session(request):
    # request.session.set_expiry(240)
    # del request.session['view_count']
    return render(request, 'products_home_session.html')


def add_product_session(request):
    product_form = ItemForm()
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_quantity = request.POST['product_quantity']
        request.session[product_name] = product_quantity
    return render(request, 'add_product_session.html', {'product_form': product_form})


def view_products_session(request):
    return render(request, 'view_products_session.html')
