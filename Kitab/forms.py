from attr import field
from django import forms

from Kitab.models import Booking, kitab

from django.contrib.auth import get_user_model



User=get_user_model()


class KitabForm(forms.ModelForm):

  class Meta:

    model = kitab

    fields = ("kitab_name","kitab_fromthePublisher","Kitab_image")


class BookForm(forms.ModelForm):

  class Meta:

    model = Booking

    fields = ("__all__")    



class UserResgistrationForm(forms.ModelForm): 
    class Meta:
        model = User
        fields = ["username","first_name","email","password"]
        widgets = {
            'password': forms.PasswordInput()
        }

    def get_id(self):
        return self.user.id    


