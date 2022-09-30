from lib2to3.pgen2.token import EQUAL
from logging import PlaceHolder
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

#dito sa forms is yung form validation
#pangoutput rin ito sa mga html meron akong sample non sa add_client.html

class addClient(forms.Form):
    email = forms.EmailField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'email','placeholder':'Email','class':'form-control','id':'exampleInputEmail1','aria-describedby':'emailHelp'}))
    username = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'username','placeholder':'username','class':'form-control','id':'exampleInputEmail1','aria-describedby':'emailHelp'}))
    password = forms.CharField(label='', max_length=100,widget=forms.PasswordInput(attrs={'name':'password','placeholder':'password','class':'form-control','id':'exampleInputEmail1','aria-describedby':'emailHelp'}))
    confirm_password=forms.CharField(label='', max_length=100,widget=forms.PasswordInput(attrs={'name':'confirm_password','placeholder':'confirm_password','class':'form-control','id':'exampleInputEmail1','aria-describedby':'emailHelp'}))
    def clean(self): #clean() pag more than 1 ang ivavalidate
        User = get_user_model()
        # cleaned_data = self.cleaned_data
        # password = self.cleaned_data.get('password')
        # confirm_password = self.cleaned_data.get('confirm_password')
        cleaned_data = super().clean() #form validation ng inputs
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password:
            if password != confirm_password:
                # raise forms.ValidationError("Password doesn't match")
                msg = "Password doesn't match"
                self.add_error('password', msg)
                self.add_error('confirm_password', msg)
        # return cleaned_data

    def clean_email(self):
        User = get_user_model()
        data = self.cleaned_data.get('email')
        try: #try and catch ang solution pag hindi makikita yung data sa db
            if data and User.objects.get(email=data):
                # raise forms.ValidationError("Account already exist") #gumagana para sa validation ng email
                msg = "Account already exist"
                self.add_error('email', msg)
            # temp = User.objects.get(email=data)
        except User.DoesNotExist:
            temp = None