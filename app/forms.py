from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EmployerAd, JobAd


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Foydalanuvchi nomi'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Parol'}),
            'password2': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Parolni tasdiqlang'}),
        }
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
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