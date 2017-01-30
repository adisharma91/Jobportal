from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BiodataModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fathername = models.CharField(max_length=200,default='')
    dob = models.DateTimeField()
    marital_status = models.CharField(max_length=200, default='')
    qualification = models.CharField(max_length=1000, default='')
    address = models.CharField(max_length=200,default='')
    old_erp_esic_numbr = models.CharField(max_length=200,default='')
    bank_acnt = models.CharField(max_length=200,default='')
    ifsc_code = models.CharField(max_length=200,default='')
    police_station = models.CharField(max_length=200,default='')
    idnty_mark = models.CharField(max_length=200,default='')
    dateofjoining = models.DateTimeField(max_length=200,default='')
    document_submitted = models.CharField(max_length=200,default='')
    experience = models.CharField(max_length=500,default='')
    preffered_jobs = models.CharField(max_length=500,default='')
    pic = models.FileField(upload_to='profile')
    emailverified = models.BooleanField(default=False)
    timeupdated = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
