from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import RegisterForm, EmployerAdForm, JobAdForm
from .models import EmployerAd, JobAd

def home(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Muvaffaqiyatli ro‘yxatdan o‘tdingiz!")
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Muvaffaqiyatli kirdingiz!")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def employers(request):
    ads = EmployerAd.objects.all().order_by('-created_at')
    form = EmployerAdForm()  # Filtr uchun forma

    # Filtrlash
    category = request.GET.get('category')
    salary_min = request.GET.get('salary_min')
    location = request.GET.get('location')
    if category:
        ads = ads.filter(category=category)
    if salary_min:
        ads = ads.filter(salary_min__gte=salary_min)
    if location:
        ads = ads.filter(location__icontains=location)

    # Sahifalash
    paginator = Paginator(ads, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employers.html', {'page_obj': page_obj, 'form': form})

@login_required
def create_employer_ad(request):
    if request.method == 'POST':
        form = EmployerAdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            messages.success(request, "E’lon muvaffaqiyatli joylashtirildi!")
            return redirect('employers')
    else:
        form = EmployerAdForm()
    return render(request, 'create_employer_ad.html', {'form': form})

@login_required
def employer_ad_detail(request, ad_id):
    ad = get_object_or_404(EmployerAd, id=ad_id)
    return render(request, 'employer_ad_detail.html', {'ad': ad})

@login_required
def edit_employer_ad(request, ad_id):
    ad = get_object_or_404(EmployerAd, id=ad_id, user=request.user)
    if request.method == 'POST':
        form = EmployerAdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            messages.success(request, "E’lon muvaffaqiyatli tahrirlandi!")
            return redirect('employers')
    else:
        form = EmployerAdForm(instance=ad)
    return render(request, 'create_employer_ad.html', {'form': form})

@login_required
def delete_employer_ad(request, ad_id):
    ad = get_object_or_404(EmployerAd, id=ad_id, user=request.user)
    ad.delete()
    messages.success(request, "E’lon muvaffaqiyatli o‘chirildi!")
    return redirect('employers')

@login_required
def jobs(request):
    ads = JobAd.objects.all().order_by('-created_at')
    form = JobAdForm()  # Filtr uchun forma

    # Filtrlash
    category = request.GET.get('category')
    salary_min = request.GET.get('salary_min')
    location = request.GET.get('location')
    if category:
        ads = ads.filter(category=category)
    if salary_min:
        ads = ads.filter(salary_min__gte=salary_min)
    if location:
        ads = ads.filter(location__icontains=location)

    # Sahifalash
    paginator = Paginator(ads, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'jobs.html', {'page_obj': page_obj, 'form': form})

@login_required
def create_job_ad(request):
    if request.method == 'POST':
        form = JobAdForm(request.POST, request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user
            ad.save()
            messages.success(request, "E’lon muvaffaqiyatli joylashtirildi!")
            return redirect('jobs')
    else:
        form = JobAdForm()
    return render(request, 'create_job_ad.html', {'form': form})

@login_required
def job_ad_detail(request, ad_id):
    ad = get_object_or_404(JobAd, id=ad_id)
    return render(request, 'job_ad_detail.html', {'ad': ad})

@login_required
def edit_job_ad(request, ad_id):
    ad = get_object_or_404(JobAd, id=ad_id, user=request.user)
    if request.method == 'POST':
        form = JobAdForm(request.POST, request.FILES, instance=ad)
        if form.is_valid():
            form.save()
            messages.success(request, "E’lon muvaffaqiyatli tahrirlandi!")
            return redirect('jobs')
    else:
        form = JobAdForm(instance=ad)
    return render(request, 'create_job_ad.html', {'form': form})

@login_required
def delete_job_ad(request, ad_id):
    ad = get_object_or_404(JobAd, id=ad_id, user=request.user)
    ad.delete()
    messages.success(request, "E’lon muvaffaqiyatli o‘chirildi!")
    return redirect('jobs')

def links(request):
    return render(request, 'links.html')

@login_required
def profile(request):
    employer_ads = EmployerAd.objects.filter(user=request.user).order_by('-created_at')
    job_ads = JobAd.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'profile.html', {'employer_ads': employer_ads, 'job_ads': job_ads})