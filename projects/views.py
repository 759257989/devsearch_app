from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .form import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    # pass a parameter  msg to the template (inside the template, it is passed to page palceholder)
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    
    return render(request, 'projects/single-project.html', {'project': projectObj})


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            # if form fields are valid, save to the database and redirect
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def updateProject(request, pk):
    # get the project by id
    project = Project.objects.get(id=pk)
    # filled the form with the project data
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            # if form fields are valid, save to the database and redirect
            form.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
    # get the project by id
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        # if the request method is POST, delete the project
        # and redirect to the projects page
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
    
# Create your views here.
