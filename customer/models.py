from django.db import models

# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=20,null=False,blank=False)
    address=models.TextField(max_length=500)
    mobileno=models.CharField(max_length=15,null=False)
    emailid=models.CharField(max_length=100,null=False,blank=False)