from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import StudentProfileForm
from .models import StudentProfile
from django.shortcuts import get_object_or_404
# Create your views here.

def profile_list(request):
    profiles = StudentProfile.objects.all()
    return render(request, 'schoolprofile/profile_list.html', {'profiles': profiles})
def register(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()


    else:
        user_form = UserCreationForm()

    return render(request, 'schoolprofile/register.html', {'user_form': user_form})

def profile_create(request):
    if request.method == 'POST':
        form = StudentProfileForm(request.POST)
        if form.is_valid():
            form.save()
            print("form saved")
            return redirect('/')
    else:
        form = StudentProfileForm()
    return render(request, 'schoolprofile/profile_form.html', {'form': form})

def profile_detail(request, pk):
    profile = get_object_or_404(StudentProfile, pk=pk)
    return render(request, 'schoolprofile/profile_detail.html', {'profile': profile})

def profile_edit(request, pk):
    profile = get_object_or_404(StudentProfile, pk=pk)
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentProfileForm(instance=profile)
    return render(request, 'schoolprofile/profile_form.html', {'form': form})
