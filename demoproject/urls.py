"""demoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from homeApp.views import* 
from customer.models import customer
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.urls.conf import settings
from django.http.response import HttpResponse
from django.views.static import serve
from django.conf.urls.static import static, url 
# base url=http://127.0.0.1:8000/
# def mainproject(r):
#     resp=HttpResponse("This is our main page---MokshiLAla")
#     return resp
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',mainproject),
    # path('home/',include('homeapp.urls')),
#     path('yasir/',include('yasirapp.urls')),
    path('login/',registerView),
     path('',homeView),
     path('emp/',addemp),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
