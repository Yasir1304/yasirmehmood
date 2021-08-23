# from django import shortcuts
from django.shortcuts import render
from django.http.response import HttpResponse
# from django.shortcuts import render_to_response
from homeApp.views import*
from .models import*
from .forms import*
# Create your views here.

def loginview(r):
    resp=render(r,"homeApp\index.html")
    return resp

def homeView(r):
    resp=render(r,"homeApp\home.html")
    return resp

def registerView(request):
    d1={}
    if(request.method=="POST"):
        reg=Register()
        reg.firstname=request.POST.get('firstname')
        reg.lastname=request.POST.get('lastname')
        reg.password=request.POST.get('password')
        reg.confirmpassword=request.POST.get('confirmpassword')
        reg.gender=request.POST.get('gender')
        reg.email=request.POST.get('email')
        reg.phone=request.POST.get('phone')
        reg.question=request.POST.get('question')
        reg.answer=request.POST.get('answer')
        reg.save()
        # return HttpResponse("Employee Registered Successfully !!!!!!!!!!!!!!!!!!!!!!!!!!!")
        allemp=Register.objects.all()
        d1['allemp']=allemp
    resp=render(request,'homeApp\index.html',context=d1)
    # return render_to_response('homeApp\index.html', message='Employee Added Successfully')
    return resp
def addemp(request):
    
    d1={}
    if request.method=="GET":
        form_emp=EmployeeForm()
        d1['form']=form_emp
        resp=render(request,'homeApp/employee.html',context=d1)
        return resp
    elif request.method=="POST":
        form_emp=EmployeeForm(request.POST)
        d1['form']=form_emp
        if(form_emp.is_valid()):
            form_emp.save()
            return HttpResponse("Employee Added Sucessfully")
        else:
            resp=render(request,'homeApp/employee.html',context=d1)
            return resp