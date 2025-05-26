from operator import is_
from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm, ProfileForm
from .models import Profile, Skill
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .utils import searchProfiles


# Create your views here.

def profiles(request):
    profiles, search_query = searchProfiles(request)
    context = {'profiles': profiles, 'search_query': search_query}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    
    topskills = profile.skill_set.exclude(description__exact="")
    other_skills = profile.skill_set.filter(description="")
    
    context = {'profile': profile, 
               'topskills': topskills,
               'other_skills': other_skills}
    return render(request, 'users/user-profile.html', context)


def loginUser(request):
    page = 'login'
    context = {'page': page}
    
    # if user is already logged in, redirect to profiles page
    if request.user.is_authenticated:
        return redirect('profiles')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # check if user exists
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
            
        # if user credentials are correct, login the user, and save the user in the session
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'Username or password is incorrect')
        
    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login') 


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # presave in the memory
            user = form.save(commit=False)
            # set the username to lowercase, to be case insensitive
            user.username = user.username.lower()
            # now save to the database
            user.save()
            messages.success(request, 'User account was created')
            
            # login the user, the user credential is stored in the session
            login(request, user)
            # redirect to the profiles page
            return redirect('edit-account')
        else:
            messages.error(request, 'An error occurred during registration')
            
    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    topskills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile': profile, 
               'skills': topskills,
               'projects': projects}
    return render(request, 'users/account.html', context)

# Django decorator that ensures the view can only be accessed by authenticated users.
@login_required(login_url='login')
def editAccount(request):
    # Gets the currently logged-in user via request.user
    profile = request.user.profile
    # Initializes a blank ProfileForm
    form = ProfileForm(instance=profile)
    
    # Checks if the form has been submitted.
    if request.method == 'POST':
        # Reinitializes the form using the submitted data.
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
        
            return redirect('account')
            
    context = {'form': form}
    return render(request, 'users/profile_form.html', context)

@login_required(login_url='login')
def createSkill(request):
    context = {}
    return render(request, 'users/skill_form.html', context)


    