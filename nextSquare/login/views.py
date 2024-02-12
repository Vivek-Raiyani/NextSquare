from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
          return render(request,'home/base.html')
          #return render(request,template,context={})

def signup(request):
        return HttpResponse('hello')
        #return render(request, tmeplate, content={})
