from django.contrib import admin
from .models import *

# Register your models here.

class studData(admin.ModelAdmin):
    
    list_display=['id','name','email','subject','message']

admin.site.register(user_contact,studData)





class stud(admin.ModelAdmin):
    list_display=['id','deparment','doctor','name','email','date','time']
admin.site.register(user_appointment,stud)






class study(admin.ModelAdmin):
    list_display=['fname','lname','number','email','package']
admin.site.register(user_package,study)
