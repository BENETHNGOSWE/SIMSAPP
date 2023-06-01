from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Module(models.Model):
    program = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    modulename = models.CharField(max_length=100, null=True, blank=True)
    modulecode = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.modulename


class Student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=50)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, blank=True)
    courses = models.ManyToManyField(Course, null=True, blank=True)
    # signature = models.ImageField(upload_to='signatures/', null=True, blank=True)
    saini = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name

class Status(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.is_registered}"




# class Signature(models.Model):
#     student = models.OneToOneField(Student, on_delete=models.CASCADE)
#     signature = models.CharField(max_length=100, null=True, blank=True)
#     id = models.BigAutoField(primary_key=True)

#     def __str__(self):
#         return f"{self.student.name}"


class Lecture(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks = models.IntegerField()
    lecture = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student.name} - {self.lecture}"
    

class LectureUE(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,null=True, blank=True)
    test1 = models.IntegerField(null=True, blank=True)
    test2 = models.IntegerField(null=True, blank=True)
    individual1 = models.IntegerField(null=True, blank=True)
    individual2 = models.IntegerField(null=True, blank=True)
    group = models.IntegerField(null=True, blank=True)
    presentation = models.IntegerField(null=True, blank=True)
    marks = models.IntegerField()
    signed = models.BooleanField(default=False,null=True, blank=True)
    # lecture = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student}- {self.signed}"    
    
class SignStatus(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='sign_statuses_received')
    marks = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    sign = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='sign_statuses_given')

    def __str__(self):
        return f"{self.marks} - {self.sign}"
