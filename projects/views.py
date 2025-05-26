from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project, Tag
from .form import ProjectForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProjects


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    # pass a parameter  msg to the template (inside the template, it is passed to page palceholder)
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    
    projects, search_query = searchProjects(request)
    context = {'project': projects, 'search_query': search_query}
    
    return render(request, 'projects/single-project.html', context)

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            # if form fields are valid, save to the database and redirect
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
        
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    
    # get the project by id
    project = profile.project_set.get(id=pk)
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

@login_required(login_url='login')
def deleteProject(request, pk):
    # get the project by id
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        # if the request method is POST, delete the project
        # and redirect to the projects page
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
    
# Create your views here.
