from django.urls import path

from .views import UserLoginView, dashboard, home, redirect_after_login, signup, user_logout

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup, name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('redirect/', redirect_after_login, name='redirect_after_login'),
]
