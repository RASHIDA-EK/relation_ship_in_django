from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Enrollment, Student, Course
from .forms import EnrollmentForm  # You'll need to create this form

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment/enrollment_list.html', {'enrollments': enrollments})

def enrollment_detail(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    return render(request, 'enrollment/enrollment_detail.html', {'enrollment': enrollment})

def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollment/enrollment_form.html', {'form': form})
