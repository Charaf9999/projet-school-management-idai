from django.contrib import admin

from .models import Department, Exam, ExamResult, Holiday, Subject, Teacher, TimeTable

admin.site.register(Department)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(Holiday)
admin.site.register(TimeTable)
admin.site.register(Exam)
admin.site.register(ExamResult)
