from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class LoginUserForm(AuthenticationForm, forms.ModelForm):
    """ LogIn form """
    class Meta:
        model = User
        fields = ("username", "password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Charfield
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class AddBlankForm(forms.ModelForm):
    """Форма добавление бланка в базу"""
    class Meta:
        model = Blank
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Charfield
        self.fields['grz'].widget.attrs['class'] = 'form-control'
        self.fields['car_mark'].widget.attrs['class'] = 'form-control'
        self.fields['sale'].widget.attrs['class'] = 'form-control'
        self.fields['price'].widget.attrs['class'] = 'form-control'
        #SelectField
        self.fields['car_class'].widget.attrs['class'] = 'form-select'
        self.fields['wash_man'].widget.attrs['class'] = 'form-select'
        self.fields['wash_type'].widget.attrs['class'] = 'form-select'
        self.fields['date'].widget.attrs['class'] = 'form-select'
        self.fields['pay_type'].widget.attrs['class'] = 'form-select'
        self.fields['service'].widget.attrs['class'] = 'form-select'
        #Other
        self.fields['service'].widget.attrs['size'] = '8'
        self.fields['service'].widget.attrs['aria-label'] = 'multiple'
        #CheckBox
        self.fields['super_clean'].widget.attrs['class'] = 'form-check-input'
        self.fields['night_clean'].widget.attrs['class'] = 'form-check-input'
        self.fields['done_clean'].widget.attrs['class'] = 'form-check-input'
        

class AddDate(forms.ModelForm):
    """Форма добавление бланка в базу"""
    class Meta:
        model = Date
        fields = ('__all__')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs['class'] = 'hui'
        