from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from faculty.models import Department, Exam, Subject, Teacher
from student.models import Student

from .forms import SignUpForm, SimpleLoginForm


def home(request):
    context = {
        'students_count': Student.objects.count(),
        'teachers_count': Teacher.objects.count(),
        'subjects_count': Subject.objects.count(),
        'departments_count': Department.objects.count(),
        'exams_count': Exam.objects.count(),
    }
    return render(request, 'home_auth/home.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Compte créé avec succès. Vous pouvez maintenant vous connecter.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'home_auth/signup.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'home_auth/login.html'
    authentication_form = SimpleLoginForm

    def form_valid(self, form):
        messages.success(self.request, 'Connexion réussie.')
        return super().form_valid(form)


def user_logout(request):
    logout(request)
    messages.info(request, 'Déconnexion effectuée.')
    return redirect('login')


@login_required
def redirect_after_login(request):
    if request.user.is_superuser or request.user.is_admin:
        return redirect('dashboard')
    if request.user.is_teacher:
        return redirect('dashboard')
    if request.user.is_student:
        return redirect('dashboard')
    return redirect('home')


@login_required
def dashboard(request):
    teacher_profile = None
    student_profile = None

    if request.user.is_teacher:
        teacher_profile = Teacher.objects.filter(user=request.user).first()
    if request.user.is_student:
        student_profile = Student.objects.filter(user=request.user).first()

    context = {
        'teacher_profile': teacher_profile,
        'student_profile': student_profile,
        'students_count': Student.objects.count(),
        'teachers_count': Teacher.objects.count(),
        'subjects_count': Subject.objects.count(),
        'departments_count': Department.objects.count(),
        'exams_count': Exam.objects.count(),
    }
    return render(request, 'home_auth/dashboard.html', context)
