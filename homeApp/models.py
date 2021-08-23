from django.db import models
from django.forms.widgets import DateInput, DateTimeBaseInput

# Create your models here.
class Register(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    confirmpassword=models.CharField(max_length=10)
    gender=models.CharField(max_length=10,null=True)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15,null=True)
    question=models.CharField(max_length=100)
    answer=models.CharField(max_length=100,)

class Employee(models.Model):
    name=models.CharField(max_length=20)
    designation=models.CharField(max_length=10)
    address=models.TextField(max_length=500)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=15,null=True)
    dateofjoining=models.DateField()

class Student(models.Model):
    id=models.CharField(max_length=10,unique=True,primary_key=True)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15,null=True)
class PersonalDetails(models.Model):
    email=models.CharField(max_length=50)
    address=models.TextField(max_length=500)
    course=models.CharField(max_length=50)
    semester=models.CharField(max_length=50)
    Date_of_admission=models.DateField()
    student=models.OneToOneField(Student,on_delete=models.CASCADE)
    