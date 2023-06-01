from django.contrib import admin
from .models import Module,Student, Status, Lecture,LectureUE,SignStatus,Course

admin.site.register(Student)
admin.site.register(Status)
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(LectureUE)
admin.site.register(SignStatus)
admin.site.register(Module)
