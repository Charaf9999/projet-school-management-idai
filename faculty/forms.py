from django import forms

from school.form_utils import StyledFormMixin

from .models import Department, Exam, ExamResult, Holiday, Subject, Teacher, TimeTable


class DepartmentForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class TeacherForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'department', 'first_name', 'last_name', 'email', 'phone', 'speciality', 'address']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
        }


class SubjectForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['department', 'teacher', 'name', 'code', 'coefficient', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class HolidayForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Holiday
        fields = ['title', 'holiday_date', 'description']
        widgets = {
            'holiday_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }


class TimeTableForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = TimeTable
        fields = ['class_name', 'day_of_week', 'start_time', 'end_time', 'room', 'subject', 'teacher']
        widgets = {
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
        }


class ExamForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['subject', 'class_name', 'exam_date', 'start_time', 'end_time', 'room', 'total_marks', 'notes']
        widgets = {
            'exam_date': forms.DateInput(attrs={'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'type': 'time'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }


class ExamResultForm(StyledFormMixin, forms.ModelForm):
    class Meta:
        model = ExamResult
        fields = ['exam', 'student', 'marks', 'remarks']
