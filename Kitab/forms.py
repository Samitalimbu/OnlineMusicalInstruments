from django import forms

from Kitab.models import Booking, kitab




class KitabForm(forms.ModelForm):

  class Meta:

    model = kitab

    fields = ("kitab_name","kitab_fromthePublisher","Kitab_image")


class BookForm(forms.ModelForm):

  class Meta:

    model = Booking

    fields = ("__all__")    