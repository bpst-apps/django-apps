from django.contrib import admin
from employees_app.models import Employee


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'salary']


admin.site.register(Employee, EmployeeAdmin)
