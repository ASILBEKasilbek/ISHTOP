from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('employers/', views.employers, name='employers'),
    path('employers/edit/<int:ad_id>/', views.edit_employer_ad, name='edit_employer_ad'),
    path('employers/delete/<int:ad_id>/', views.delete_employer_ad, name='delete_employer_ad'),
    path('jobs/', views.jobs, name='jobs'),
    path('jobs/edit/<int:ad_id>/', views.edit_job_ad, name='edit_job_ad'),
    path('jobs/delete/<int:ad_id>/', views.delete_job_ad, name='delete_job_ad'),
    path('links/', views.links, name='links'),
    path('profile/', views.profile, name='profile'),
]