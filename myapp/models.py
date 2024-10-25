from django.db import models

# Create your models here.

class user_appointment(models.Model):
    deparment=models.CharField(max_length=20)
    doctor=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)


class user_contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    subject=models.CharField(max_length=20)
    message=models.CharField(max_length=120)

class user_package(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    number=models.BigIntegerField()
    email=models.EmailField()
    package=models.CharField(max_length=20)

class user_details(models.Model):
    name=models.CharField(max_length=25)
    number=models.BigIntegerField()
    password=models.CharField(max_length=8)

    
