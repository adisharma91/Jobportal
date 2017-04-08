from django import forms
from portfolio.models import BiodataModel, JobsModel
from .models import MyUser
from django.conf import settings


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control',
                             'placeholder': 'Email Address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                'placeholder': 'Create Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                'placeholder': 'Re-enter Password'}), error_messages={'required': "Please enter your password"})
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    contact_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}))

    user_type = forms.ChoiceField(choices={
        ("A", "Applicant"),
        ("E", "Employer"),
        }, widget=forms.RadioSelect(), initial="A")

    class Meta:
        model = MyUser
        fields = ('email', 'user_type', 'first_name', 'last_name', 'contact_number')

    def __init__(self, *args, **kwargs):

        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = False
        self.fields['password1'].label = False
        self.fields['password2'].label = False

    def clean_email(self):
        email = self.cleaned_data['email']
        #self.cleaned_data['username'] = email
        if MyUser.objects.filter(email=email).exists():
            raise forms.ValidationError("Email %s is already in use" % (email))
        return email

    def clean_password2(self):
        """Checks two password entries match.
        """
        cleaned_data = super(UserCreationForm, self).clean() #to see the password validation
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        # if len(password1) <= 4 or len(password2) <= 4:
        #     raise forms.ValidationError("Password must be at least 5 characters long")
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError("Passwords don't match")
                # del cleaned_data["password1"]  #to delete the invalid password, not necessary
                # del cleaned_data["password2"]
        return password2

    def save(self, commit=True):
        """Saves the provided password in hashed format.
        """
        user = super(UserCreationForm, self).save(commit=False)
        # get the user object first, then add password, then save
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.is_active = True
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control',
                             'placeholder': 'Your email address'}), error_messages={'required': "Please enter your email id"})
                           # widget=forms.widgets.TextInput
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                               'placeholder': 'Your password'}), error_messages={'required': "Please enter your password"})
                            # widget=forms.widgets.PasswordInput

    class Meta:
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = False
        self.fields['password'].label = False


class BiodataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BiodataForm, self).__init__(*args, **kwargs)
        self.fields['dob'].input_formats = settings.DATE_INPUT_FORMATS
        self.fields['dateofjoining'].input_formats = settings.DATE_INPUT_FORMATS
        self.fields['marital_status'].choices = BiodataModel.Status
        self.fields['gender'].choices = BiodataModel.Gender

    class Meta:
        model = BiodataModel
        exclude = ['pic','emailverified','deleted']

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
            'gender': forms.Select(attrs={'class': 'form-control'})
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = BiodataModel
        fields = ['pic',]

        widgets = {
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