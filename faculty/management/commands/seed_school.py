from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from faculty.models import Department, Exam, ExamResult, Holiday, Subject, Teacher, TimeTable
from student.models import Parent, Student


class Command(BaseCommand):
    help = 'Crée quelques données de test pour le projet de gestion scolaire.'

    def handle(self, *args, **options):
        User = get_user_model()

        admin_user, _ = User.objects.get_or_create(username='admin', defaults={
            'email': 'admin@school.com',
            'first_name': 'Admin',
            'last_name': 'Principal',
            'is_superuser': True,
            'is_staff': True,
            'is_admin': True,
        })
        admin_user.is_superuser = True
        admin_user.is_staff = True
        admin_user.is_admin = True
        admin_user.set_password('admin12345')
        admin_user.save()

        teacher_user, _ = User.objects.get_or_create(username='teacher1', defaults={
            'email': 'teacher1@school.com',
            'first_name': 'Yassine',
            'last_name': 'Karim',
            'is_teacher': True,
        })
        teacher_user.is_teacher = True
        teacher_user.set_password('teacher12345')
        teacher_user.save()

        student_user, _ = User.objects.get_or_create(username='student1', defaults={
            'email': 'student1@school.com',
            'first_name': 'Salma',
            'last_name': 'Amrani',
            'is_student': True,
        })
        student_user.is_student = True
        student_user.set_password('student12345')
        student_user.save()

        dep_math, _ = Department.objects.get_or_create(name='Mathématiques', defaults={'description': 'Département des mathématiques'})
        dep_info, _ = Department.objects.get_or_create(name='Informatique', defaults={'description': 'Département informatique'})

        teacher, _ = Teacher.objects.get_or_create(
            email='teacher1@school.com',
            defaults={
                'user': teacher_user,
                'department': dep_info,
                'first_name': 'Yassine',
                'last_name': 'Karim',
                'phone': '0600000000',
                'speciality': 'Développement web',
                'address': 'Tanger',
            }
        )
        teacher.user = teacher_user
        teacher.department = dep_info
        teacher.save()

        parent, _ = Parent.objects.get_or_create(
            full_name='Ahmed Amrani',
            defaults={
                'phone': '0611111111',
                'email': 'parent1@mail.com',
                'profession': 'Fonctionnaire',
                'address': 'Tanger',
            }
        )

        student, _ = Student.objects.get_or_create(
            registration_number='STD001',
            defaults={
                'user': student_user,
                'parent': parent,
                'first_name': 'Salma',
                'last_name': 'Amrani',
                'gender': 'Femme',
                'email': 'student1@school.com',
                'phone': '0622222222',
                'address': 'Tanger',
                'class_name': 'S1 IDAI',
            }
        )
        student.user = student_user
        student.parent = parent
        student.save()

        subject1, _ = Subject.objects.get_or_create(
            code='PY101',
            defaults={
                'department': dep_info,
                'teacher': teacher,
                'name': 'Python',
                'coefficient': 2,
                'description': 'Introduction à Python',
            }
        )

        subject2, _ = Subject.objects.get_or_create(
            code='ALG201',
            defaults={
                'department': dep_math,
                'teacher': teacher,
                'name': 'Algèbre',
                'coefficient': 2,
                'description': "Bases d'algèbre",
            }
        )

        Holiday.objects.get_or_create(
            title='Aïd Al Fitr',
            holiday_date='2026-04-10',
            defaults={'description': 'Congé national'}
        )

        timetable, _ = TimeTable.objects.get_or_create(
            class_name='S1 IDAI',
            day_of_week='Lundi',
            start_time='08:30',
            end_time='10:30',
            subject=subject1,
            defaults={'teacher': teacher, 'room': 'Salle 4'}
        )
        timetable.teacher = teacher
        timetable.room = 'Salle 4'
        timetable.save()

        exam, _ = Exam.objects.get_or_create(
            subject=subject1,
            class_name='S1 IDAI',
            exam_date='2026-05-20',
            start_time='09:00',
            end_time='11:00',
            defaults={'room': 'Salle A', 'total_marks': 20, 'notes': 'Examen semestriel'}
        )

        result, _ = ExamResult.objects.get_or_create(
            exam=exam,
            student=student,
            defaults={'marks': 16.50, 'remarks': 'Bon travail'}
        )
        result.marks = 16.50
        result.remarks = 'Bon travail'
        result.save()

        self.stdout.write(self.style.SUCCESS('Données de test créées avec succès.'))
