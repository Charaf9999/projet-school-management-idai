from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from home_auth.mixins import StaffRequiredMixin

from .forms import ParentForm, StudentForm
from .models import Parent, Student


class ParentListView(StaffRequiredMixin, ListView):
    model = Parent
    template_name = 'student/parent_list.html'
    context_object_name = 'parents'


class ParentCreateView(StaffRequiredMixin, CreateView):
    model = Parent
    form_class = ParentForm
    template_name = 'student/parent_form.html'
    success_url = reverse_lazy('student:parent_list')


class ParentUpdateView(StaffRequiredMixin, UpdateView):
    model = Parent
    form_class = ParentForm
    template_name = 'student/parent_form.html'
    success_url = reverse_lazy('student:parent_list')


class ParentDeleteView(StaffRequiredMixin, DeleteView):
    model = Parent
    template_name = 'student/parent_confirm_delete.html'
    success_url = reverse_lazy('student:parent_list')


class StudentListView(StaffRequiredMixin, ListView):
    model = Student
    template_name = 'student/student_list.html'
    context_object_name = 'students'


class StudentDetailView(StaffRequiredMixin, DetailView):
    model = Student
    template_name = 'student/student_detail.html'
    context_object_name = 'student_obj'


class StudentCreateView(StaffRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('student:student_list')


class StudentUpdateView(StaffRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html'
    success_url = reverse_lazy('student:student_list')


class StudentDeleteView(StaffRequiredMixin, DeleteView):
    model = Student
    template_name = 'student/student_confirm_delete.html'
    success_url = reverse_lazy('student:student_list')
