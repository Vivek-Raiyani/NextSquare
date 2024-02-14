from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def log(request):
        # code to login the user
        if request.method=='POST':
                username=request.POST['user']
                password=request.POST['password']
                user=authenticate(username=username,password=password)
                if user is not None:
                        login(request,user)
                        return redirect('home:homepage')
                else:
                        return HttpResponse('invalid credentials')# redirect to login with roor tost
                            

        return render(request,'login/login.html')
        #return render(request,template,context={})

def signup(request):
        # code to  register user  security and input is valif=d remaining
        # user input validation before saving the user
        if request.method=='POST':
                username=request.POST['username']
                firstname=request.POST['firstname']
                lastname=request.POST['lastname']
                email=request.POST['email']
                password1=request.POST['password1']
                password2=request.POST['password2']
                password = make_password(password1)

                if password1==password2:
                        user=User()
                        user.username=username
                        user.first_name=firstname
                        user.last_name=lastname
                        user.email=email
                        user.password=password
                        user.save()
                        return redirect('login:login')
        #return HttpResponse('hello')
        return render(request,'login/signup.html' )

def logo(request):
        logout(request)
        # code to logout the user
        return redirect('home:homepage')