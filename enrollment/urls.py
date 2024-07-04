from django.urls import path
from . import views

urlpatterns = [
    path('', views.enrollment_list, name='enrollment_list'),
    path('<int:pk>/', views.enrollment_detail, name='enrollment_detail'),
    path('new/', views.enrollment_create, name='enrollment_create'),
]