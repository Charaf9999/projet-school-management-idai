from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_superuser or user.is_admin)


class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_superuser or user.is_admin or user.is_teacher)


class TeacherRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.is_teacher


class StudentRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and user.is_student
