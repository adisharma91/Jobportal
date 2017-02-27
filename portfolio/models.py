from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class BiodataModel(models.Model):

    Status = [
        ('m','Married'),
        ('s','Single'),
        ('d','Divorced'),
        ('w','Widowed')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fathername = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    marital_status = models.CharField(max_length=10, choices=Status, null=True, blank=True)
    qualification = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    old_erp_esic_numbr = models.CharField(max_length=200, null=True, blank=True)
    bank_acnt = models.CharField(max_length=200, null=True, blank=True)
    ifsc_code = models.CharField(max_length=200, null=True, blank=True)
    police_station = models.CharField(max_length=200, null=True, blank=True)
    idnty_mark = models.CharField(max_length=200, null=True, blank=True)
    dateofjoining = models.DateField(null=True, blank=True)
    experience = models.CharField(max_length=1000, null=True, blank=True)
    preffered_jobs = models.CharField(max_length=500, null=True, blank=True)
    pic = models.FileField(upload_to='profile', null=True, blank=True)
    emailverified = models.BooleanField(default=False)
    lastupdated = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
