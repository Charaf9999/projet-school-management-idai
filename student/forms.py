from django import forms

from school.form_utils import StyledFormMixin

from .models import Parent, Student


class ParentForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['full_name', 'phone', 'email', 'profession', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }


class StudentForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'user', 'parent', 'registration_number', 'first_name', 'last_name', 'birth_date',
            'gender', 'email', 'phone', 'address', 'class_name'
        ]
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }
