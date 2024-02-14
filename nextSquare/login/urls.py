from . import views
from django.contrib import admin
from django.urls import path

app_name='login'
urlpatterns = [
    path('log/',views.log, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logo/',views.logo,name='logout')
]
