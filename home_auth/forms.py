from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from school.form_utils import StyledFormMixin

User = get_user_model()


class SignUpForm(StyledFormMixin, UserCreationForm):
    ROLE_CHOICES = (
        ('student', 'Étudiant'),
        ('teacher', 'Enseignant'),
    )

    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES, label='Rôle')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        role = self.cleaned_data.get('role')
        user.email = self.cleaned_data.get('email')
        user.is_admin = False
        user.is_teacher = role == 'teacher'
        user.is_student = role == 'student'
        if commit:
            user.save()
        return user


class SimpleLoginForm(StyledFormMixin, AuthenticationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)
