from django.db import models
from django.contrib.auth.models import User

class EmployerAd(models.Model):
    CATEGORY_CHOICES = [
        ('worker', 'Ishchi'),
        ('programmer', 'Dasturchi'),
        ('doctor', 'Shifokor'),
        ('teacher', 'O‘qituvchi'),
        ('other', 'Boshqa'),
    ]
    CURRENCY_CHOICES = [
        ('UZS', 'UZS'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
    ]
    WORK_TYPE_CHOICES = [
        ('remote', 'Uydan'),
        ('office', 'Ofisdan'),
        ('hybrid', 'Gibrid'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    phone = models.CharField(max_length=20)
    telegram = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)  # Joylashuv
    salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES)
    requirements = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.position}"

class JobAd(models.Model):
    CATEGORY_CHOICES = EmployerAd.CATEGORY_CHOICES
    CURRENCY_CHOICES = EmployerAd.CURRENCY_CHOICES
    WORK_TYPE_CHOICES = EmployerAd.WORK_TYPE_CHOICES

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    phone = models.CharField(max_length=20)
    telegram = models.URLField(blank=True)
    location = models.CharField(max_length=100, blank=True)  # Joylashuv
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    work_type = models.CharField(max_length=20, choices=WORK_TYPE_CHOICES)
    experience = models.TextField(blank=True)  # Tajriba
    desired_position = models.CharField(max_length=100)
    salary_min = models.DecimalField(max_digits=10, decimal_places=2)
    salary_max = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.desired_position}"