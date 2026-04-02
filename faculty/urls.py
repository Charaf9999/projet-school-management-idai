from django.urls import path

from .views import (
    DepartmentCreateView,
    DepartmentDeleteView,
    DepartmentListView,
    DepartmentUpdateView,
    ExamCreateView,
    ExamDeleteView,
    ExamDetailView,
    ExamListView,
    ExamResultCreateView,
    ExamResultDeleteView,
    ExamResultListView,
    ExamResultUpdateView,
    ExamUpdateView,
    HolidayCreateView,
    HolidayDeleteView,
    HolidayListView,
    HolidayUpdateView,
    SubjectCreateView,
    SubjectDeleteView,
    SubjectDetailView,
    SubjectListView,
    SubjectUpdateView,
    TeacherCreateView,
    TeacherDeleteView,
    TeacherDetailView,
    TeacherListView,
    TeacherUpdateView,
    TimeTableCreateView,
    TimeTableDeleteView,
    TimeTableListView,
    TimeTableUpdateView,
)

app_name = 'faculty'

urlpatterns = [
    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/add/', DepartmentCreateView.as_view(), name='department_add'),
    path('departments/<int:pk>/edit/', DepartmentUpdateView.as_view(), name='department_edit'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete'),

    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/add/', TeacherCreateView.as_view(), name='teacher_add'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/<int:pk>/edit/', TeacherUpdateView.as_view(), name='teacher_edit'),
    path('teachers/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),

    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('subjects/add/', SubjectCreateView.as_view(), name='subject_add'),
    path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('subjects/<int:pk>/edit/', SubjectUpdateView.as_view(), name='subject_edit'),
    path('subjects/<int:pk>/delete/', SubjectDeleteView.as_view(), name='subject_delete'),

    path('holidays/', HolidayListView.as_view(), name='holiday_list'),
    path('holidays/add/', HolidayCreateView.as_view(), name='holiday_add'),
    path('holidays/<int:pk>/edit/', HolidayUpdateView.as_view(), name='holiday_edit'),
    path('holidays/<int:pk>/delete/', HolidayDeleteView.as_view(), name='holiday_delete'),

    path('timetables/', TimeTableListView.as_view(), name='timetable_list'),
    path('timetables/add/', TimeTableCreateView.as_view(), name='timetable_add'),
    path('timetables/<int:pk>/edit/', TimeTableUpdateView.as_view(), name='timetable_edit'),
    path('timetables/<int:pk>/delete/', TimeTableDeleteView.as_view(), name='timetable_delete'),

    path('exams/', ExamListView.as_view(), name='exam_list'),
    path('exams/add/', ExamCreateView.as_view(), name='exam_add'),
    path('exams/<int:pk>/', ExamDetailView.as_view(), name='exam_detail'),
    path('exams/<int:pk>/edit/', ExamUpdateView.as_view(), name='exam_edit'),
    path('exams/<int:pk>/delete/', ExamDeleteView.as_view(), name='exam_delete'),

    path('results/', ExamResultListView.as_view(), name='result_list'),
    path('results/add/', ExamResultCreateView.as_view(), name='result_add'),
    path('results/<int:pk>/edit/', ExamResultUpdateView.as_view(), name='result_edit'),
    path('results/<int:pk>/delete/', ExamResultDeleteView.as_view(), name='result_delete'),
]
