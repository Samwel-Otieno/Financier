from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import *
# Create your views here.

def Registerview(request):
    if (request.method=='POST'):
        user_form=Registerform(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            messages.success(request, "Registration successful")
            return redirect("accounts:register")
    else:
        form=Registerform()
    return render(request,'accounts/register.html', {'user_form':user_form})
