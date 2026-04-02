from django.urls import path

from .views import (
    ParentCreateView,
    ParentDeleteView,
    ParentListView,
    ParentUpdateView,
    StudentCreateView,
    StudentDeleteView,
    StudentDetailView,
    StudentListView,
    StudentUpdateView,
)

app_name = 'student'

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('add/', StudentCreateView.as_view(), name='student_add'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),

    path('parents/', ParentListView.as_view(), name='parent_list'),
    path('parents/add/', ParentCreateView.as_view(), name='parent_add'),
    path('parents/<int:pk>/edit/', ParentUpdateView.as_view(), name='parent_edit'),
    path('parents/<int:pk>/delete/', ParentDeleteView.as_view(), name='parent_delete'),
]
