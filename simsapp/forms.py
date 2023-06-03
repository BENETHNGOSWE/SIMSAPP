from django import forms
from .models import Lecture,LectureUE, Claim

class MarksForm(forms.ModelForm):
    class Meta:
        model = LectureUE
        fields = '__all__'

class LectureUEForm(forms.ModelForm):
    class Meta:
        model = LectureUE
        fields = '__all__'

# class SignatureForm(forms.ModelForm):
#     class Meta:
#         model = Signature
#         fields = '__all__'        

class SignForm(forms.Form):
    sign = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your signature'}))


class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['message']