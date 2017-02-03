from django import forms
from portfolio.models import BiodataModel
from django.contrib.auth.models import User
from django.conf import settings

class Userform(forms.ModelForm):
    first_name =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'false', 'placeholder':'Ex: John'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ex: McCarthy'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'********'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Johnmcharty@gmail.com'}))

    class Meta:
        model = User
        fields = ('first_name','last_name','email','password')

class BiodataForm(forms.ModelForm):
    fathername =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'false'}))
    dob = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    qualification = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    old_erp_esic_numbr = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    bank_acnt = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ifsc_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    police_station = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    idnty_mark = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dateofjoining = forms.DateTimeField(input_formats=settings.DATE_INPUT_FORMATS,widget=forms.TextInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Date when project start*'}))
    document_submitted = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    experience = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    preffered_jobs = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pic = forms.FileField()

    class Meta:
        model = BiodataModel
        fields = '__all__'

