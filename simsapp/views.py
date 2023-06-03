from django.shortcuts import render, redirect, get_object_or_404
from .models import Claim,Student, Lecture, LectureUE, SignStatus,Course, Module
from .forms import MarksForm, LectureUEForm, SignForm, ClaimForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# ------------------------------------PAGE YA KUCHAGUA ROLE------------------
def index_view(request):
    return render(request, 'index.html')

# -------------------------MWANAFUNZI LOGIN-----------------------------------

def login_view(request):
    if request.method == 'POST':
        reg_no = request.POST['reg_no']
        
        try:
            student = Student.objects.get(reg_no=reg_no)
            # Perform login directly without checking the password
            request.session['student_id'] = student.id
            return redirect('student_view', student_id=student.id)
        except Student.DoesNotExist:
            messages.error(request, 'Invalid reg_no. Please try again.')
    
    return render(request, 'student/login.html')

# -----------------------------MWALIMU LOGIN--------------------------------

def lecture_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('adminpage')  # Replace 'lecture_dashboard' with the actual URL name for the lecture dashboard
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    
    return render(request, 'student/lecture_login.html')

def admin(request):
    return render(request,'student/teacher_dashboard.html')




# ---------------------------------MSAJIRI KUADD MWANAFUNZI-----------------------------------------------
def admin_add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        reg_no = request.POST['reg_no']
        student = Student(name=name, reg_no=reg_no)
        student.save()
    return render(request, 'simsapp/admin_add_student.html')


# ---------------------------------MWANAFUNZI KUADD SAINI YAKE---------------------------------------------
def student_profile(request):
    if request.method == 'POST':
        saini = request.POST['saini']
        student = Student.objects.get(id=request.user.id)
        student.saini = saini
        student.save()
    return render(request, 'add_marks.html')


# --------------------------------DASHBOARD YA MWALIMU -------------------------------------------

def dashboard(request):
    return render(request, 'simsapp/dashboard.html')

# -------------------------------sehemu ya mwalimu kuona wanafunzi wote--------------------------------
def teacher_view(request):
    students = Student.objects.filter(lectureue__signed=True).distinct()
    context = {
        'students': students
    }
    return render(request, 'simsapp/teacher_view.html', context)
# ----------------------mwalimu kuchagua mwanafunzi------------------------------
def select_student(request):
    students = Student.objects.filter(status__is_registered=True)
    
    if request.method == 'POST':
        student_id = request.POST.get('student')
        if student_id:
            return redirect('add_marks', student_id=student_id)
    
    return render(request, 'simsapp/show_marks.html', {'students': students})

# ----------------------mwalimu kuweka marks za wanafunzi--------------------------
def add_marks(request, student_id):
    student = Student.objects.get(id=student_id)
    
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.instance.student = student
            form.save()
            return redirect('/marksdata')
    else:
        form = MarksForm()
    
    return render(request, 'simsapp/add_marks.html', {'form': form, 'student': student})



# ------------------------update marks za mwanafunzi---------------------------
def update_marks(request, pk):
    lectures = get_object_or_404(LectureUE, id=pk)
    form = MarksForm(instance=lectures)

    if request.method == "POST":
        form = MarksForm(request.POST, instance=lectures)
        if form.is_valid():
            form.save()
            return redirect('/show_marks')

    context = {"form":form}
    return render(request, 'simsapp/add_marks.html', context)


def update_marks(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    lectureue = student.lectureue_set.first()  # Assuming each student has only one LectureUE instance
    
    if request.method == 'POST':
        form = MarksForm(request.POST, instance=lectureue)
        if form.is_valid():
            form.save()
            return redirect('/marksdata')

    else:
        form = MarksForm(instance=lectureue)

    return render(request, 'simsapp/add_marks.html', {'form': form, 'student': student})    

# ------------------------kumanage wanafunzi wote-------------------------
def manage_marks(request):
    lectures = LectureUE.objects.all()
    context = {'lectures': lectures}
    return render(request, 'simsapp/manage_marks.html', context)

# def manage_marks(request):
#     context = {'lectures':  LectureUE.objects.all()}
#     return render(request, 'simsapp/manage_marks.html', context)
# -----------------------------------------------------------------------------------------------


def StudentList(request):
    students = Student.objects.all()
    lectures = Lecture.objects.all()
    # signatures = Signature.objects.filter(student__in=students)
    
    return render(request, 'student_list.html', {'students': students, 'lectures': lectures})


def course_students(request):
    if request.method == 'POST':
        course_id = request.POST.get('course')
        if course_id:
            course = get_object_or_404(Module, pk=course_id)
            students = course.student_set.all()
            context = {
                'course': course,
                'students': students,
            }
            return render(request, 'simsapp/course_students.html', context)

    module = Module.objects.all()
    return render(request, 'simsapp/course_selection.html', {'module': module})



def course_students_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    students = course.student_set.all()

    context = {
        'course': course,
        'students': students,
    }

    return render(request, 'simsapp/course_students.html', context)

# ------------------------mwanafunzi ------------------------------------------

# def student_view(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)
#     marks = LectureUE.objects.filter(student=student)
#     module = Module.objects.filter(student=student)
#     context = {
#         'student': student,
#         'marks': marks,
#         'module':module,
#     }
#     return render(request, 'student/student_view.html', context)

 

# --------------------KUTUMA CLAIM MWANAFUZI-------------------------------

def send_claim(request):
    if request.method == 'POST':
        form = ClaimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.student = request.user
            # claim.teacher = claim.student.module.teacher
            claim.save()
            return redirect('student_view', student_id=request.user.id)
    else:
        form = ClaimForm()
    
    return render(request, 'student_view.html', {'form': form})





# ************************************************************************
# ********************UE***************************************************




def add_ue_marks(request, student_id):
    student = Student.objects.get(id=student_id)
    
    if request.method == 'POST':
        form = LectureUEForm(request.POST)
        if form.is_valid():
            form.instance.student = student
            form.save()
            return redirect('show_marks')
    else:
        form = LectureUEForm()
    
    return render(request, 'add_marks_ue.html', {'form': form, 'student': student})


def StudentListUE(request):
    students = Student.objects.all()
    lectures = LectureUE.objects.all()
    lecture = Lecture.objects.all()
    return render(request, 'student_list_ue.html', {'students': students, 'lectures': lectures, 'lecture': lecture})


def select_student_ue(request):
    students = Student.objects.filter(status__is_registered=True)
    
    if request.method == 'POST':
        student_id = request.POST.get('student')
        if student_id:
            return redirect('add_marks', student_id=student_id)
    
    return render(request, 'show_marks_ue.html', {'students': students})
# ******************************************************************************
# #+************************view marks for student**************************

def view_marks(request, student_id):
    student = Student.objects.get(id=student_id)
    marks = LectureUE.objects.filter(student=student)

    return render(request, 'view_marks.html', {'student': student, 'marks': marks})


def sign_marks(request, student_id):
    student = Student.objects.get(id=student_id)
    marks = LectureUE.objects.filter(student=student)
    # signature = Signature.objects.filter(student=student).first()
    
    if request.method == 'POST':
        # Perform any necessary actions when the student presses the sign button
        return redirect('view_marks', student_id=student_id)
    
    return render(request, 'sign_marks.html', {'student': student, 'marks':marks})



def view_marks_and_sign(request, student_id):
    student = Student.objects.get(id=student_id)
    lectures = Lecture.objects.filter(student=student)
    

    if request.method == 'POST':
        form = SignForm(request.POST)
        if form.is_valid():
            signature = form.cleaned_data['signature']
            # Create or update the SignStatus for the student and lectures
            for lecture in lectures:
                sign_status, created = SignStatus.objects.get_or_create(
                    student=student,
                    marks=lecture,
                )
                sign_status.sign = signature
                sign_status.save()
            
            return redirect('student_marks', student_id=student_id)
    else:
        form = SignForm()

    return render(request, 'view_marks.html', {
        'student': student,
        'lectures': lectures,
        'form': form,
    })




# def sign_mark(request, marks_id):
#     marks = Lecture.objects.get(id=marks_id)
#     student = request.user.student  # Assuming you have a user profile model with a OneToOneField to the User model

#     if request.method == 'POST':
#         form = SignForm(request.POST)
#         if form.is_valid():
#             sign = form.cleaned_data['sign']
#             sign_status = SignStatus.objects.create(student=student, marks=marks, sign=sign)
#             return redirect('success')
#     else:
#         form = SignForm()

#     return render(request, 'sign_marks.html', {'form': form, 'marks': marks})

def sign_mark(request, mark_id):
    mark = get_object_or_404(LectureUE, pk=mark_id)
    mark.signed = True
    mark.save()
    return redirect('teacher_view')




