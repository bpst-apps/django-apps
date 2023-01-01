from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# function based view
def home(request):
    return HttpResponse("<h1>welcome to first django application</h1>")


def display_datetime(request):
    dt = datetime.now()
    dt_string = f"<h2>current system date and time: {str(dt)}</h2>"
    return HttpResponse(dt_string)

