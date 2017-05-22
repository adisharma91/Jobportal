from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, user_type, first_name, last_name, contact_number, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            user_type=user_type,
            username=username,
            contact_number=contact_number,
            first_name=first_name,
            last_name=last_name
        )

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, user_type, first_name, last_name, contact_number, password):

        user = self.create_user(email=email,
                                password=password,
                                user_type=user_type,
                                username=username,
                                contact_number=contact_number,
                                first_name=first_name,
                                last_name=last_name
                                )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, default='user')
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, db_index=True,)
    user_type = models.CharField(max_length=30, choices={
        ("A", "Applicant"),
        ("E", "Employer"),
        }, default='A')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    contact_number = models.CharField(max_length=13, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','contact_number']

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def get_email(self):
        return self.email

    def __unicode__ (self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin


class BiodataModel(models.Model):

    Status = [
        ('m','Married'),
        ('s','Single'),
        ('d','Divorced'),
        ('w','Widowed')
    ]

    Gender = [
        ('m','Male'),
        ('f','Female')
    ]

    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    fathername = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    marital_status = models.CharField(max_length=10, choices=Status, null=True, blank=True)
    gender = models.CharField(max_length=2, choices=Gender, null=True, blank=True)
    qualification = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    pincode = models.CharField(max_length=200, null=True, blank=True)
    old_erp_esic_numbr = models.CharField(max_length=200, null=True, blank=True)
    bank_acnt = models.CharField(max_length=200, null=True, blank=True)
    ifsc_code = models.CharField(max_length=200, null=True, blank=True)
    police_station = models.CharField(max_length=200, null=True, blank=True)
    idnty_mark = models.CharField(max_length=200, null=True, blank=True)
    dateofjoining = models.DateField(null=True, blank=True)
    experience = models.CharField(max_length=1000, null=True, blank=True)
    preffered_jobs = models.CharField(max_length=500, null=True, blank=True)
    pic = models.ImageField(upload_to='profile')
    emailverified = models.BooleanField(default=False)
    lastupdated = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)


class JobsModel(models.Model):

    Time = [
        ('a','1 yr'),
        ('b','2 yr'),
        ('c','3 yr'),
        ('d','4 yr'),
        ('e','5 yr')
    ]

    ExperienceType = [
        ('entry','Entry Level'),
        ('mid','Mid Level'),
        ('senior','Mid-Senior Level'),
        ('top','Top Level')
    ]

    jobtitle = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    about = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    qualification = models.CharField(max_length=200, null=True, blank=True)
    experience = models.CharField(max_length=200, choices=ExperienceType, null=True, blank=True)
    vacancies = models.IntegerField(null=True, blank=True)
    salary = models.CharField(max_length=200, null=True, blank=True)
    addedon = models.DateTimeField(auto_now_add=True)
    lastdate = models.DateField(null=True, blank=True)
    doj = models.DateField(null=True, blank=True)
    interview_process = models.CharField(max_length=200, null=True, blank=True)
    interview_venue = models.CharField(max_length=200, null=True, blank=True)
    bondtime = models.CharField(max_length=50, choices=Time, null=True, blank=True)
    dept_logo = models.FileField(upload_to='logo', null=True)
    deleted = models.BooleanField(default=False)


class JobsApplied(models.Model):
    jobid = models.ForeignKey(JobsModel, on_delete=models.CASCADE)
    userid = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)


class FormUANbased(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    UAN =  models.CharField(max_length=50, null=True, blank=True)
    leaving_date = models.DateField(null=True, blank=True)
    PAN = models.CharField(max_length=50, null=True, blank=True)
    purpose = models.CharField(max_length=200, null=True, blank=True)
    advance_amount = models.CharField(max_length=200, null=True, blank=True)
    agency_address = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    PIN = models.CharField(max_length=200, null=True, blank=True)

class Form10c(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    claimant_name = models.CharField(max_length=50, null=True, blank=True)
    father_name = models.CharField(max_length=50, null=True, blank=True)
    husband_name = models.CharField(max_length=50, null=True, blank=True)
    old_Estt_name = models.CharField(max_length=50, null=True, blank=True)
    old_Estt_address = models.CharField(max_length=50, null=True, blank=True)
    old_Estt_region = models.CharField(max_length=50, null=True, blank=True)
    old_Estt_code_no = models.CharField(max_length=50, null=True, blank=True)
    old_Estt_Acnt_no = models.CharField(max_length=50, null=True, blank=True)
    leaving_reason = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    PIN = models.CharField(max_length=200, null=True, blank=True)
    family_name = address = models.CharField(max_length=200, null=True, blank=True)
    family_dob = models.CharField(max_length=200, null=True, blank=True)
    family_relation = models.CharField(max_length=200, null=True, blank=True)
    nomine = models.CharField(max_length=200, null=True, blank=True)
    member_death_date = models.CharField(max_length=200, null=True, blank=True)
    claminant_name = models.CharField(max_length=200, null=True, blank=True)
    claminant_relation = models.CharField(max_length=200, null=True, blank=True)
    SB_Acnt_no = models.CharField(max_length=200, null=True, blank=True)
    SB_BankName = models.CharField(max_length=200, null=True, blank=True)
    SB_BankBranch = models.CharField(max_length=200, null=True, blank=True)
    SB_BankIFSC = models.CharField(max_length=200, null=True, blank=True)
    SB_BankAddress = models.CharField(max_length=200, null=True, blank=True)

class Form19c_Old(models.Model):
    father_name = models.CharField(max_length=50, null=True, blank=True)
    husband_name = models.CharField(max_length=50, null=True, blank=True)
    factory_address = models.CharField(max_length=50, null=True, blank=True)
    PF_Acnt_no = models.CharField(max_length=50, null=True, blank=True)
    UAN = models.CharField(max_length=50, null=True, blank=True)
    doj = models.DateField(null=True, blank=True)
    leaving_date = models.DateField(null=True, blank=True)
    leaving_reason = models.CharField(max_length=50, null=True, blank=True)
    PAN = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    PIN = models.CharField(max_length=50, null=True, blank=True)
    saving_Acnt_bo = models.CharField(max_length=50, null=True, blank=True)
    saving_bank = models.CharField(max_length=50, null=True, blank=True)
    saving_bank_address = models.CharField(max_length=50, null=True, blank=True)
    saving_bank_IFSC = models.CharField(max_length=50, null=True, blank=True)

