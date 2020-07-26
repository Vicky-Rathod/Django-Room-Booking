from django.forms import ModelForm
from django import forms
from .models import CheckIn, CheckOut,Customer



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname','lastname','phone','alternate_phone','address','gender','auth_number']

class CheckInForm(forms.ModelForm):
    class Meta:
        model = CheckIn
        fields = '__all__'
    def __init__ (self, *args, **kwargs):
        available_rooms = kwargs.pop('available_rooms', None)
        super().__init__(*args, **kwargs)
        if available_rooms:
            print(self.fields['room_type'])
            self.fields['room_type'].queryset = available_rooms

class CheckOutForm(forms.ModelForm):
    class Meta :
        model = CheckOut
        fields = '__all__'