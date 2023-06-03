from django.urls import path
from .views import send_claim,index_view,admin,login_view,lecture_login_view, manage_marks,update_marks,student_profile,admin_add_student,course_students_detail,course_students,dashboard,teacher_view,view_marks_and_sign,add_marks,StudentList,select_student,add_ue_marks, StudentListUE, select_student_ue,view_marks,sign_marks,sign_mark,student_view

urlpatterns = [
# -------------------homepage link-------------------------------- 
     path('', index_view, name='index'),

#--------------------mwanafunzi na mwalimu kulogin--------------------------  
     path('logins/', login_view, name='login'),
     path('lecture-login/', lecture_login_view, name='lecture_login'),


# ---------------------------admin---------------------------------------------------
    path('admin-add-student/', admin_add_student, name='admin_add_student'),
    path('student/profile/', student_profile, name='student_profile'), 

# -----------------------------teacher-------------------------------------------------
    path('', dashboard, name='dashboard'),

    path('course/students/', course_students, name='course_students'),
    path('course/students/<int:course_id>/', course_students_detail, name='course_students_detail'),
 
    path('add-marks/<int:student_id>/', add_marks, name='add_marks'),

    path('teacher/', teacher_view, name='teacher_view'),

    path('updatemarks/<str:student_id>/', update_marks, name='update_marks'),
    path('marksdata/', manage_marks, name='manage_marks'),

#-----------------------mwalimu dashboard----------------------------------   
     path('adminpage/', admin, name='adminpage'),

# ---------------------------student---------------------------------------------------------
    path('student/<int:student_id>/', student_view, name='student_view'),

#-----------------------mwanafunzi kutuma claim-----------------------------  
     path('send-claim/', send_claim, name='send_claim'),
     
# ------------------------------------------------------------------------------------

   







    path('student_list/', StudentList, name='student_list'),


    path('ue-marks/<int:student_id>/', add_ue_marks, name='add_ue_marks'),
    path('ue-student/', StudentListUE, name='StudentListUE'),
    path('select-studentue/', select_student_ue, name='select_student_ue'),


    path('view-marks/<int:student_id>/', view_marks, name='view_marks'),
    path('sign-marks/<int:student_id>/', sign_marks, name='sign_marks'),

    path('marks/<int:student_id>/', view_marks_and_sign, name='view_marks_and_sign'),
    path('sign/<int:mark_id>/', sign_mark, name='sign_mark'),


      # path('course/students/', course_students, name='course_students'),
    # path('course/students/<int:course_id>/', course_students_detail, name='course_students_detail'),
    # path('course/students/<int:course_id>/', course_students, name='course_students'),
    
   path('select-student/', select_student, name='select_student'),
    # other URL patterns
   
    
]
