from django import forms
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model
class Registerform(forms.ModelForm):
    password1=forms.CharField(label='password', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    pic=forms.FileField(label='Profile picture')

    #model other parameters from the User method
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username','email']

    def validator(self):
        #the super method is valid only within a class it is used to call the validator method
        cleaned_data=super().validator()
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")
        
        #validation 
        if (password1 == password2):
            if (len(password1) < 8):
                raise forms.ValidationError("Password too short")
        else:
            raise forms.ValidationError("Passwords do not match")
        return password1
                

#logged in user password reset
class SetPasswordForm(SetPasswordForm):
    class Meta:
        model=get_user_model()
        fields=['newpassword1', 'newpassword2']

