from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login(request):
          if request.method == 'POST':
                    username = request.POST.get('username')
                    password1 = request.POST.get('password1')
                    password2= request.POST.get('password2')
                    email=request.POST.get('email')
                    if password1==password2:
                              user=User.objects.create_user(username=username,password=password1,email=email)
                              user.save()
                              return HttpResponse('success')
                    else:
                              return HttpResponse('error')
                            

          return render(request,'login/login.html')
          #return render(request,template,context={})

def signup(request):
        if request.method == 'POST':
                    username = request.POST.get('username')
                    password1 = request.POST.get('password1')
                    password2= request.POST.get('password2')
                    email=request.POST.get('email')
                    if password1==password2:
                              user=User.objects.create_user(username=username,password=password1,email=email)
                              user.save()
                              return HttpResponse('successful signup')
                    else:
                              return HttpResponse('error')
        return HttpResponse('hello')
        #return render(request, tmeplate, content={})
