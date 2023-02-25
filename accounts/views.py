from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def registerview(request):
    if (request.method=='POST'):
        user_form=Registerform(request.POST, request.FILES)
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
        user_form=Registerform()
    return render(request,'accounts/register.html', {'user_form':user_form})

def login(request):
    if (request.method=='POST'):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            #end
            else:
                return redirect('web:index')   
        else:
            return redirect('accounts:login')
    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return render(request, 'accounts/logout.html')

@login_required
def setpassword(request):
    user=request.user
    if(request.method=='POST'):
        reset_password_form=SetPasswordForm(user, request.POST)
        if reset_password_form.is_valid():
            reset_password_form.save()
            return redirect('accounts:login')
    else:
        reset_password_form=SetPasswordForm(user)
    return render(request, 'accounts/resetpassword.html', {'reset_password_form':reset_password_form})