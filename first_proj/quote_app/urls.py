from django.urls import path
from quote_app import views

urlpatterns = [
    path("quote/", views.display_quote, name="quote"),
]
