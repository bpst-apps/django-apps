from django.shortcuts import render


# Create your views here.
def render_electronics(request):
    products_dict = {
        "heading": "List of Electronics Products",
        "product_1": "MacBook Pro",
        "product_2": "Dell G15",
        "product_3": "iPhone 14 Pro",
        "product_type": "electronics"
    }
    return render(request, 'products.html', context=products_dict)


def render_toys(request):
    products_dict = {
        "heading": "List of Toys",
        "product_1": "Remote Car",
        "product_2": "Drone",
        "product_3": "Bycycle",
        "product_type": "toys"
    }
    return render(request, 'products.html', context=products_dict)


def render_shoes(request):
    products_dict = {
        "heading": "List of Shoes",
        "product_1": "Reebok",
        "product_2": "PUMA",
        "product_3": "Nike",
        "product_type": "shoes"
    }
    return render(request, 'products.html', context=products_dict)


def index(request):
    return render(request, 'index.html')
