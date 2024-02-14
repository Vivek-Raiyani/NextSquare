from django.http import HttpResponse
from django.shortcuts import render

from .models import Properties

# Create your views here.
def home(request):
          properties=Properties.objects.all()
          if properties is None:
                  return HttpResponse('no properties found')

          return render (request,'home/index.html',context={'properties':properties})