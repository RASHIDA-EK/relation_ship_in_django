from django.urls import path
from . import views



urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('new/', views.course_create, name='course_create'),
    path('<int:pk>/edit/', views.course_edit, name='course_edit'),
    path('<int:course_id>/students/new/', views.student_create, name='student_create'),
]
