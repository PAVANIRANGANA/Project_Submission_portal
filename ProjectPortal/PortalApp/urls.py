from django.urls import path
from . import views
from .views import combined_login_view

urlpatterns = [
    path('', views.home, name='home'),
    path('submit/', views.submit_project, name='submit_project'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('review/<int:project_id>/', views.review_project, name='review_project'),
    path('register/', views.student_register, name='student_register'),
    path('after-login/', views.after_login_redirect, name='after_login'),
    path('login/', combined_login_view, name='combined_login'), 
]