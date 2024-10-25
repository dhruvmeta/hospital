from django import forms
from .models import user_appointment,user_contact,user_package,user_details

    


class u_appointment(forms.ModelForm):
    class Meta:
        model=user_appointment
        fields='__all__'



class u_contact(forms.ModelForm):
    class Meta:
        model=user_contact
        fields='__all__'



class u_package(forms.ModelForm):
    class Meta:
        model=user_package
        fields='__all__'

class u_details(forms.ModelForm):
    class Meta:
        model=user_details
        fields='__all__'
