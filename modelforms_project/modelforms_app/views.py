from django.shortcuts import render
from modelforms_app.forms import ProjectForm
from modelforms_app.models import Project


def index(request):
    return render(request, 'index.html')


def list_projects(request):
    project_list = Project.objects.all()
    return render(request, 'list_projects.html', context={'project_list': project_list})


def add_project(request):
    project_form = ProjectForm()
    if request.method == 'POST':
        filled_form = ProjectForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
        return index(request)
    return render(request, 'add_project.html', context={'project_form': project_form})
