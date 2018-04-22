from django.shortcuts import render
from .forms import AuthForm,UserProfileForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.




def index(req):
    return render(req,'auth_app/index.html')

def register_page(req):

    registered=False

    if req.method=='POST':
        auth_form = AuthForm(req.POST)
        profile_form = UserProfileForm(req.POST)

        if auth_form.is_valid() and profile_form.is_valid():
            user = auth_form.save()
            user.set_password(user.password)
            user.save()

            profile_data=profile_form.save(commit=False)
            profile_data.user=user

            if 'profile_pic' in req.FILES:
                profile_data.profile_pic= req.FILES['profile_pic']

            profile_data.save()

            registered=True

        else:
            print(auth_form.errors,profile_form.errors)

    else:
        auth_form=AuthForm()
        profile_form=UserProfileForm()


    return render(req,'auth_app/registration.html',{'auth_cform':auth_form,'profile_form':profile_form,'registered':registered})

def login_page(req):

    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(req,user)
                return HttpResponseRedirect(reverse('auth_app:index'))
            else:
                return HttpResponse("User not active")
        else:
            print("Someoene tried to login and failed")
            print("Username:{} and password:{}".format(username,password))
            return HttpResponse("Invalid Details")
    else:
        return render(req,'auth_app/login.html')

@login_required
def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse('auth_app:index'))

@login_required
def special(req):
    return HttpResponse("You are logged in")