from django import forms
from portfolio.models import BiodataModel, JobsModel
from django.contrib.auth.models import User
from django.conf import settings


class Userform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    first_name =  forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Lastname'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))
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


class JobsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JobsForm, self).__init__(*args, **kwargs)
        self.fields['bondtime'].choices = JobsModel.Time
        self.fields['experience'].choices = JobsModel.ExperienceType

    class Meta:
        model = JobsModel
        fields = '__all__'

        widgets = {
            'jobtitle': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'required': 'true', 'rows': 5}),
            'department': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'qualification': forms.Textarea(attrs={'class': 'form-control', 'required': 'true', 'rows': 5}),
            'experience': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
            'vacancies': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'lastdate': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker1', 'required': 'true'}),
            'interview_process': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'interview_venue': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            'doj': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker2', 'required': 'true'}),
            'bondtime': forms.Select(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'dept_logo': forms.FileInput()
        }