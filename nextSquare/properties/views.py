from django.http import HttpResponse
from django.shortcuts import render

from home.models import Properties

# Create your views here.

def properties(request,id):
          # how to get data from database 
          prop=Properties.objects.get(pk=id)
          return render(request, 'home/properties_page.html', context={'property':prop})
