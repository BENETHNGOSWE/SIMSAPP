from django.shortcuts import render, redirect
# from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# Create your views here.

def Homepage(request):
    return render(request, 'simsapp/dashboard.html')


def Register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('sname')
        name = request.POST.get('uname')
        password = request.POST.get('pass')
        confirm_password = request.POST.get('confirmpass')

        if password != confirm_password:
            error_msg = 'Password do not match. Please write again'
            return render(request, 'student/register.html', {'error_msg':error_msg})

        new_user = User.objects.create_user(name, confirm_password, password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login-page')
  
    return render(request, 'student/register.html', {})

def Login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home-page')
        else:
            return HttpResponse('Error, user does not exist')


    return render(request, 'student/login.html', {})

# def register(request):
#     if request.method == "POST":
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = UserRegisterForm()
    
#     return render(request, "student/register.html", {'form': form})




# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             if user.is_student:
#                 return redirect('student_view', student_id=user.student.id)
#             else:
#                 return redirect('dashboard')
#         else:
#             # Handle invalid login credentials
#             return render(request, 'student/login.html', {'error': 'Invalid username or password'})
#     else:
#         return render(request, 'student/login.html')
