from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from home_auth.mixins import StaffRequiredMixin

from .forms import DepartmentForm, ExamForm, ExamResultForm, HolidayForm, SubjectForm, TeacherForm, TimeTableForm
from .models import Department, Exam, ExamResult, Holiday, Subject, Teacher, TimeTable


class DepartmentListView(StaffRequiredMixin, ListView):
    model = Department
    template_name = 'faculty/department_list.html'
    context_object_name = 'departments'


class DepartmentCreateView(StaffRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'faculty/department_form.html'
    success_url = reverse_lazy('faculty:department_list')


class DepartmentUpdateView(StaffRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'faculty/department_form.html'
    success_url = reverse_lazy('faculty:department_list')


class DepartmentDeleteView(StaffRequiredMixin, DeleteView):
    model = Department
    template_name = 'faculty/department_confirm_delete.html'
    success_url = reverse_lazy('faculty:department_list')


class TeacherListView(StaffRequiredMixin, ListView):
    model = Teacher
    template_name = 'faculty/teacher_list.html'
    context_object_name = 'teachers'


class TeacherDetailView(StaffRequiredMixin, DetailView):
    model = Teacher
    template_name = 'faculty/teacher_detail.html'
    context_object_name = 'teacher_obj'


class TeacherCreateView(StaffRequiredMixin, CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'faculty/teacher_form.html'
    success_url = reverse_lazy('faculty:teacher_list')


class TeacherUpdateView(StaffRequiredMixin, UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'faculty/teacher_form.html'
    success_url = reverse_lazy('faculty:teacher_list')


class TeacherDeleteView(StaffRequiredMixin, DeleteView):
    model = Teacher
    template_name = 'faculty/teacher_confirm_delete.html'
    success_url = reverse_lazy('faculty:teacher_list')


class SubjectListView(StaffRequiredMixin, ListView):
    model = Subject
    template_name = 'faculty/subject_list.html'
    context_object_name = 'subjects'


class SubjectDetailView(StaffRequiredMixin, DetailView):
    model = Subject
    template_name = 'faculty/subject_detail.html'
    context_object_name = 'subject_obj'


class SubjectCreateView(StaffRequiredMixin, CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'faculty/subject_form.html'
    success_url = reverse_lazy('faculty:subject_list')


class SubjectUpdateView(StaffRequiredMixin, UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = 'faculty/subject_form.html'
    success_url = reverse_lazy('faculty:subject_list')


class SubjectDeleteView(StaffRequiredMixin, DeleteView):
    model = Subject
    template_name = 'faculty/subject_confirm_delete.html'
    success_url = reverse_lazy('faculty:subject_list')


class HolidayListView(StaffRequiredMixin, ListView):
    model = Holiday
    template_name = 'faculty/holiday_list.html'
    context_object_name = 'holidays'


class HolidayCreateView(StaffRequiredMixin, CreateView):
    model = Holiday
    form_class = HolidayForm
    template_name = 'faculty/holiday_form.html'
    success_url = reverse_lazy('faculty:holiday_list')


class HolidayUpdateView(StaffRequiredMixin, UpdateView):
    model = Holiday
    form_class = HolidayForm
    template_name = 'faculty/holiday_form.html'
    success_url = reverse_lazy('faculty:holiday_list')


class HolidayDeleteView(StaffRequiredMixin, DeleteView):
    model = Holiday
    template_name = 'faculty/holiday_confirm_delete.html'
    success_url = reverse_lazy('faculty:holiday_list')


class TimeTableListView(StaffRequiredMixin, ListView):
    model = TimeTable
    template_name = 'faculty/timetable_list.html'
    context_object_name = 'timetables'


class TimeTableCreateView(StaffRequiredMixin, CreateView):
    model = TimeTable
    form_class = TimeTableForm
    template_name = 'faculty/timetable_form.html'
    success_url = reverse_lazy('faculty:timetable_list')


class TimeTableUpdateView(StaffRequiredMixin, UpdateView):
    model = TimeTable
    form_class = TimeTableForm
    template_name = 'faculty/timetable_form.html'
    success_url = reverse_lazy('faculty:timetable_list')


class TimeTableDeleteView(StaffRequiredMixin, DeleteView):
    model = TimeTable
    template_name = 'faculty/timetable_confirm_delete.html'
    success_url = reverse_lazy('faculty:timetable_list')


class ExamListView(StaffRequiredMixin, ListView):
    model = Exam
    template_name = 'faculty/exam_list.html'
    context_object_name = 'exams'


class ExamDetailView(StaffRequiredMixin, DetailView):
    model = Exam
    template_name = 'faculty/exam_detail.html'
    context_object_name = 'exam_obj'


class ExamCreateView(StaffRequiredMixin, CreateView):
    model = Exam
    form_class = ExamForm
    template_name = 'faculty/exam_form.html'
    success_url = reverse_lazy('faculty:exam_list')


class ExamUpdateView(StaffRequiredMixin, UpdateView):
    model = Exam
    form_class = ExamForm
    template_name = 'faculty/exam_form.html'
    success_url = reverse_lazy('faculty:exam_list')


class ExamDeleteView(StaffRequiredMixin, DeleteView):
    model = Exam
    template_name = 'faculty/exam_confirm_delete.html'
    success_url = reverse_lazy('faculty:exam_list')


class ExamResultListView(StaffRequiredMixin, ListView):
    model = ExamResult
    template_name = 'faculty/result_list.html'
    context_object_name = 'results'


class ExamResultCreateView(StaffRequiredMixin, CreateView):
    model = ExamResult
    form_class = ExamResultForm
    template_name = 'faculty/result_form.html'
    success_url = reverse_lazy('faculty:result_list')


class ExamResultUpdateView(StaffRequiredMixin, UpdateView):
    model = ExamResult
    form_class = ExamResultForm
    template_name = 'faculty/result_form.html'
    success_url = reverse_lazy('faculty:result_list')


class ExamResultDeleteView(StaffRequiredMixin, DeleteView):
    model = ExamResult
    template_name = 'faculty/result_confirm_delete.html'
    success_url = reverse_lazy('faculty:result_list')
