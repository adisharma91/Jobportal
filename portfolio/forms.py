from django import forms
from portfolio.models import BiodataModel
from django.contrib.auth.models import User
from django.conf import settings


class Userform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    first_name =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':'false', 'placeholder':'Firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lastname'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}), required=True, help_text='Password must be 8 characters minimum length (with at least 1 lower case, 1 upper case and 1 number).')
    # password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}),required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Email'}))

    class Meta:
        model = User
        fields = ('first_name','last_name','email','password')


class BiodataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BiodataForm, self).__init__(*args, **kwargs)
        self.fields['dob'].input_formats = settings.DATE_INPUT_FORMATS
        self.fields['dateofjoining'].input_formats = settings.DATE_INPUT_FORMATS
        self.fields['marital_status'].choices = BiodataModel.Status

    class Meta:
        model = BiodataModel
        exclude = ['emailverified','deleted']

        widgets = {
            'fathername': forms.TextInput(attrs={'class': 'form-control','required':'true'}),
            'dob': forms.DateInput(attrs={'class': 'form-control','id': 'datepicker1','required':'true'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            'qualification': forms.Textarea(attrs={'class': 'form-control','rows': 5}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required':'true'}),
            'old_erp_esic_numbr': forms.TextInput(attrs={'class': 'form-control'}),
            'bank_acnt': forms.TextInput(attrs={'class': 'form-control'}),
            'ifsc_code': forms.TextInput(attrs={'class': 'form-control'}),
            'police_station': forms.TextInput(attrs={'class': 'form-control'}),
            'idnty_mark': forms.TextInput(attrs={'class': 'form-control'}),
            'dateofjoining': forms.DateInput(attrs={'class': 'form-control','id': 'datepicker2'}),
            'experience': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'preffered_jobs': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'pic': forms.FileInput()
        }

