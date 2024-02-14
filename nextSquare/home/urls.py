from django.conf import settings
from django.urls import path
from . import views

from django.conf.urls.static import static

app_name='home'
urlpatterns = [
          path('base',views.home,name='homepage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
