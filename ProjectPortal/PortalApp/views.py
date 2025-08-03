from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.utils.timezone import make_aware
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
import datetime

from django.views.decorators.csrf import csrf_protect
from .forms import ProjectForm, ReviewForm, StudentRegistrationForm
from .models import Project

def home(request):
    return render(request, 'home.html')

@login_required
def submit_project(request):
    deadline = make_aware(datetime.datetime.strptime(settings.SUBMISSION_DEADLINE, '%Y-%m-%d %H:%M:%S'))
    if timezone.now() > deadline:
        return render(request, 'submit_project.html', {'error': 'Submission deadline has passed.'})

    form = ProjectForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        project = form.save(commit=False)
        project.student = request.user
        project.save()
        messages.success(request, 'Project submitted successfully!')
        return redirect('dashboard')
    return render(request, 'submit_project.html', {'form': form})


@login_required
def dashboard(request):
    projects = Project.objects.filter(student=request.user)
    return render(request, 'dashboard.html', {'projects': projects})

@login_required
def admin_view(request):
    if not request.user.is_staff:
        return redirect('login')
    projects = Project.objects.exclude(status="Approved")
    return render(request, 'admin_view.html', {'projects': projects})

@login_required
def review_project(request, project_id):
    if not request.user.is_staff:
        return redirect('dashboard')
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            send_mail(
                subject='Project Review Update',
                message=f'Your project "{project.title}" has been {project.status}. Feedback: {project.feedback}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[project.student.email],
                fail_silently=True,
            )
            return redirect('admin_view')
    else:
        form = ReviewForm(instance=project)
    return render(request, 'review.html', {'form': form, 'project': project})

def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = False
            user.save()
            auth_login(request, user)
            return redirect('combined_login')
    else:
        form = StudentRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@csrf_protect
def combined_login_view(request):
    student_form = AuthenticationForm(data=request.POST if 'student_login' in request.POST else None)
    admin_form = AuthenticationForm(data=request.POST if 'admin_login' in request.POST else None)

    if request.method == 'POST':
        if 'student_login' in request.POST and student_form.is_valid():
            user = authenticate(username=student_form.cleaned_data['username'],
                                password=student_form.cleaned_data['password'])
            if user and not user.is_staff:
                auth_login(request, user)
                return redirect('dashboard')
            
        elif 'admin_login' in request.POST and admin_form.is_valid():
            user = authenticate(username=admin_form.cleaned_data['username'],
                                password=admin_form.cleaned_data['password'])
            if user and user.is_staff:
                auth_login(request, user)
                return redirect('admin_view')

    return render(request, 'registration/dual_login.html', {
        'student_form': student_form,
        'admin_form': admin_form,
    })

@login_required
def after_login_redirect(request):
    if request.user.is_staff:
        return redirect('admin_view')
    else:
        return redirect('dashboard')

