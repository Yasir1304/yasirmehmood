from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def customer(r):
    resp=HttpResponse("This is our customer page---MokshiLAla")
    return resp

resp=render