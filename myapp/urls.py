from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('login/',views.login),
   path('',views.signup),
   path('index/',views.index,name="index"),
   path('about/',views.about),
   path('contact/',views.contact),
   path('appointment/',views.appointment),
   path('service/',views.service),
   path('team/',views.team),
   path('testimonial/',views.testimonial),
   path('price/',views.price),
   path('form1/',views.form1),
   path('userlogout/',views.userlogout),

]