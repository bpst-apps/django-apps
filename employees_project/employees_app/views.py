
from django.shortcuts import render
from employees_app.models import Employee


def employee_data(request):
    employees = Employee.objects.all()
    emp_dict = {"employees": employees}
    return render(request, "employees.html", context=emp_dict)
