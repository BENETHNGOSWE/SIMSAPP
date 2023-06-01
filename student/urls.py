from django.urls import path
from .views import  Register, Login, Homepage
from simsapp.views import student_view, dashboard

urlpatterns = [
    # path('register/', register, name="register"),
    #  path('student/<int:student_id>/', student_view, name='student_view'),
    # path('teacher/dashboard/', dashboard, name='teacher_dashboard'),
    # path('login/', login_view, name='login'),

    path('home/', Homepage, name="home-page"),
    path('register/', Register, name="register-page"),
    path('login/', Login, name="login-page"),
]