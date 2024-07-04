from django.urls import path
from . import views

app_name = 'schoolprofile'

urlpatterns = [
    path('', views.profile_list, name='profile_list'),
path('profile/<int:pk>/', views.profile_detail, name='profile_detail'),

    path('create/', views.profile_create, name='profile_create'),
    path('profile/<int:pk>/edit/', views.profile_edit, name='profile_edit'),

    path('register/', views.register, name='register')]