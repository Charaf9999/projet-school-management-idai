from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

    def get_role(self):
        if self.is_superuser or self.is_admin:
            return 'Administrateur'
        if self.is_teacher:
            return 'Enseignant'
        if self.is_student:
            return 'Étudiant'
        return 'Utilisateur'

    def __str__(self):
        return f"{self.username} - {self.get_role()}"
