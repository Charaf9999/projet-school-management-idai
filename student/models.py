from django.conf import settings
from django.db import models


class Parent(models.Model):
    full_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


class Student(models.Model):
    GENDER_CHOICES = (
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='student_profile'
    )
    parent = models.OneToOneField(Parent, on_delete=models.CASCADE, related_name='student')
    registration_number = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Homme')
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    class_name = models.CharField(max_length=50, verbose_name='Classe')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
