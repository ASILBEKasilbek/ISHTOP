from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EmployerAd, JobAd

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EmployerAdForm(forms.ModelForm):
    class Meta:
        model = EmployerAd
        fields = ['company_name', 'position', 'category', 'logo', 'phone', 'telegram', 'location',
                  'salary_min', 'salary_max', 'currency', 'work_type', 'requirements']
        widgets = {
            'requirements': forms.Textarea(attrs={'rows': 4}),
        }

class JobAdForm(forms.ModelForm):
    class Meta:
        model = JobAd
        fields = ['full_name', 'age', 'phone', 'telegram', 'location', 'category', 'work_type',
                  'experience', 'desired_position', 'salary_min', 'salary_max', 'currency', 'cv']
        widgets = {
            'experience': forms.Textarea(attrs={'rows': 4}),
        }