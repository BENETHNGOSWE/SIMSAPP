# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from .models import UserProfile

# class UserRegisterForm(UserCreationForm):
#     is_student = forms.BooleanField(label='Are you a student?', required=False)

#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2', 'is_student']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()
#             is_student = self.cleaned_data.get('is_student')
#             UserProfile.objects.create(user=user, is_student=is_student)
#         return user
