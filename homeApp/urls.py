from demoproject.urls import mainproject
from django.urls import path
from .views import *
# baseurl:http://127.0.0.1:8000/homeApp/
urlpatterns = [
    path('',mainproject),
    path('homeApp/', ),
    # path('login/',registerView),
    
]