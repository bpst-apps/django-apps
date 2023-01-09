from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView
from django.http import HttpResponse
from classbasedviews_app.models import Student
from django.urls import reverse_lazy


class GreetingView(View):
    greeting_message = "<h1>Hello from CBV</h1>"

    def get(self, request):
        return HttpResponse(self.greeting_message)


class StudentListView(ListView):
    model = Student
    # default template_name is student_list.html
    # default context_object is student_list
    # If we want we can change
    # template_name = ''


class StudentDetailView(DetailView):
    model = Student
    # default template_name is student_detail.html
    # default context_object is student


class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'test_score')


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('view_records')
