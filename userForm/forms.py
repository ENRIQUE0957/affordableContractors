from django import forms
from userForm.models import UserInfo
class UserInput(forms.ModelForm):
    #validators go here
    class Meta:
        model = UserInfo
        fields = "__all__"
        exclude = []