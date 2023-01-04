from django.shortcuts import render
from . import forms


def user_registration_view(request):
    registration_form = forms.UserRegistrationForm()
    if request.method == 'POST':
        registration_form = forms.UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            print("form is valid")
            print(f"First Name: {registration_form.cleaned_data['first_name']}")
    return render(request, "user_registration.html", context={"form": registration_form})
