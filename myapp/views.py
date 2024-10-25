from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
from doctor1 import settings
from .models import user_details
from django.contrib.auth import logout


# Create your views here.
def index (request):
    user=request.session.get('user')
    if request.method=='POST':
        dhruv=u_appointment(request.POST)
        if dhruv.is_valid():
            dhruv.save()
            print("Your appoinment has been saved!")
              #email
            sub="Thank you!"
            msg=f"Dear User\n\nYour appointment has been booked!\n\nWe will contact you shortly.\n If you have any problem, contact us anytime.\n\nThank & Regards\nCRITICARE - Rajkot\n+91 7435820532 | criticare03@gmail.com | www.CRITICARE.com"
            from_id=settings.EMAIL_HOST_USER
            #to_id=["metadhruv4@gmail.com",]
            to_id=[request.POST['email']]
            
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)

            sub1="we have one new appointment"
            msg1=f"dear \n\n we have one new appointment \n please check it \n and contact fast as soon as possible !"
            from1_id=settings.EMAIL_HOST_USER
            to1_id=["criticare03@gmail.com",]
            
            
            send_mail(subject=sub1,message=msg1,from_email=from1_id,recipient_list=to1_id)
           
        else:
            print(u_appointment.errors)
    return render (request,'index.html',{'user':user})

def about (request):
    return render (request,'about.html')

def appointment (request):
    if request.method=='POST':
        dhruv=u_appointment(request.POST)
        if dhruv.is_valid():
            dhruv.save()
            print("Your appoinment has been saved!")

            #email
            sub="Thank you!"
            msg=f"Dear User\n\nYour appointment has been booked!\n\n We will contact you shortly.\n and give you visit date and time \n If you have any problem, contact us anytime.\n\nThank & Regards\nCRITICARE - Rajkot\n+91 7435820532 | criticare03@gmail.com | www.CRITICARE.com"
            from_id=settings.EMAIL_HOST_USER
            #to_id=["metadhruv4@gmail.com",]
            to_id=[request.POST['email']]
            
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)

            sub1="we have one new appointment"
            msg1=f"dear \n\n we have one new appointment \n please check it \n and contact fast as soon as possible !"
            from1_id=settings.EMAIL_HOST_USER
            to1_id=["criticare03@gmail.com",]
            
            
            send_mail(subject=sub1,message=msg1,from_email=from1_id,recipient_list=to1_id)

            
            return redirect ('index') 
        else:
            print(u_appointment.errors)
    return render (request,'appointment.html')

def login (request):
    if request.method=='POST':
        nu=request.POST['number']
        pas=request.POST['password']
        user=user_details.objects.filter(number=nu,password=pas)
        if user:
            print("login successfuly.....!")
            request.session["user"]=nu 
            return redirect('index')
        else:
            print("Error...number or password are wrong ...!")
    return render (request,'login.html')


def contact (request):
    if request.method=='POST':
        newappoin=u_contact(request.POST)
        if newappoin.is_valid():
            newappoin.save()
            print("Your message has been saved!")
            #email
            sub="we have one new message !"
            msg=f"Dear \n\n we have one new  \n\n message please check it ....!"
            from_id=settings.EMAIL_HOST_USER
            #to_id=["metadhruv4@gmail.com",]
            to_id=[request.POST['email']]
            
            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)

            
            return redirect ('index')
        else:
            print(u_contact.errors)
    return render (request,'contact.html')

def price (request):
    return render (request,'price.html')



def service (request):
    return render (request,'service.html')

def team (request):
    return render (request,'team.html')

def testimonial (request):
    return render (request,'testimonial.html')

def form1 (request):
    if request.method=='POST':
        harsh=u_package(request.POST)
        if harsh.is_valid():
            harsh.save()
            print("Your information has been send !")
            return redirect ('index')
        else:
            print(harsh.errors)
    return render (request ,'form1.html')

def signup (request):
    if request.method=='POST':
        harsh=u_details(request.POST)
        if harsh.is_valid():
            harsh.save()
            print("Your account has been created  !")
            return redirect ('index')
        else:
            print(harsh.errors)
    return render(request,'signup.html')

def userlogout(request):
    logout(request)
    return redirect ('/')