from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
    path('team/<int:member_id>/', views.team_member_detail, name='team_member_detail'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('careers/<int:career_id>/', views.career_detail, name='career_detail'),
    path('careers/<int:career_id>/', views.career_detail, name='career_detail'),
    path('careers/<int:career_id>/success/', views.application_success, name='application_success'),
]