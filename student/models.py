from django.contrib.auth.models import User
from django.db import models

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_student = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username





# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to='profile_pics', null=True, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'