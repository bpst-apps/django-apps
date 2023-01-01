from django.shortcuts import render


# Create your views here.

def render_template(request):
    my_dict = {"name": "Bhanu", "data": {"test": "okay"}}
    return render(request, 'templates_app/first_template.html', context=my_dict)


def render_employee(request):
    emp_dict = {"id": 10001, "name": "Don", "salary": 6000}
    return render(request, 'templates_app/employee_template.html', context=emp_dict)
