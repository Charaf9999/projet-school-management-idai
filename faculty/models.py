from django.conf import settings
from django.db import models

from student.models import Student


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Teacher(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='teacher_profile'
    )
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='teachers')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    speciality = models.CharField(max_length=100, blank=True)
    address = models.TextField(blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Subject(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='subjects')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    coefficient = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.code})"


class Holiday(models.Model):
    title = models.CharField(max_length=120)
    holiday_date = models.DateField()
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['holiday_date']

    def __str__(self):
        return f"{self.title} - {self.holiday_date}"


class TimeTable(models.Model):
    DAYS = (
        ('Lundi', 'Lundi'),
        ('Mardi', 'Mardi'),
        ('Mercredi', 'Mercredi'),
        ('Jeudi', 'Jeudi'),
        ('Vendredi', 'Vendredi'),
        ('Samedi', 'Samedi'),
    )

    class_name = models.CharField(max_length=50, verbose_name='Classe')
    day_of_week = models.CharField(max_length=20, choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50, blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetables')
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, related_name='timetables')

    class Meta:
        ordering = ['class_name', 'day_of_week', 'start_time']

    def __str__(self):
        return f"{self.class_name} - {self.subject.name} - {self.day_of_week}"


class Exam(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='exams')
    class_name = models.CharField(max_length=50, verbose_name='Classe')
    exam_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50, blank=True)
    total_marks = models.PositiveIntegerField(default=20)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['exam_date', 'start_time']

    def __str__(self):
        return f"{self.subject.name} - {self.class_name} - {self.exam_date}"


class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='exam_results')
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    remarks = models.CharField(max_length=200, blank=True)

    class Meta:
        unique_together = ('exam', 'student')
        ordering = ['student__last_name']

    def __str__(self):
        return f"{self.student} - {self.exam.subject.name} - {self.marks}"
