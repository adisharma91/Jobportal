from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from portfolio import forms as portfolioform
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, response
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import *
import json
import pdfkit
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.pagesizes import A4
# from reportlab.platypus import Image


def index(request):
    user_numbr = User.objects.all().count()

    return render(request, 'index.html' , {'user_numbr' : user_numbr})


def signin(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

        if user is not None:
            if user.is_active:
                login(request, user)

            return HttpResponseRedirect('/index')
        else:
            messages.add_message(request, messages.INFO, 'Username/Password do not match. Please try again.')
            return render(request, 'signin.html')
    else:
        return render(request, 'signin.html')


def forgotpassword(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.POST.get('email')).exists():
            eml = request.POST.get('email')

            u = User.objects.get(email=eml)
            password = User.objects.make_random_password()
            u.set_password(password)
            u.save()

            subject = 'Mail for password change.'
            message = 'You are recieving this mail as you requested for password change. \n Your password is = ' + str(
                password) + ' \n Regards \n Team Job Portal'
            from_email = settings.EMAIL_HOST_USER
            to_list = [u.email, settings.EMAIL_HOST_USER]

            send_mail(subject, message, from_email, to_list, fail_silently=True)
            return HttpResponseRedirect('/signin')
        else:
            messages.add_message(request, messages.INFO, 'Please enter a valid email !!')
            return HttpResponseRedirect('/forgotpassword')

    return render(request, 'forgotpassword.html')


def signout(request):
    logout(request)
    return redirect('index')


def signup(request):
    if request.method == 'POST':
            userfrm = portfolioform.Userform(request.POST)
            if User.objects.filter(username=request.POST.get('username')).exists():
                messages.add_message(request, messages.INFO, 'Username already exists !!')
                return render(request, 'signup.html', {'userform': userfrm})
            else:
                user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
                user.first_name = request.POST['first_name']
                user.last_name = request.POST['last_name']
                user.save()
                login(request, user)
                subject = 'Welcome to Job Portal.'
                message = 'Thank you for being part of us. \n We are glad to have you. \n Regards \n Team Job Portal'
                from_email = settings.EMAIL_HOST_USER
                to_list = [user.email, settings.EMAIL_HOST_USER]

                send_mail(subject, message, from_email, to_list, fail_silently=True)
                return HttpResponseRedirect('/index',{'userform': userfrm})

    else:
        userfrm = portfolioform.Userform()
        return render(request, 'signup.html', {'userform': userfrm})


@login_required(login_url="signin/")
def biodata(request,Id):
    try:
        bdexist = BiodataModel.objects.get(user_id=Id)
    except BiodataModel.DoesNotExist:
        bdexist = None

    if request.method == 'POST':
        frm = portfolioform.BiodataForm(request.POST, request.FILES)
        bdata = BiodataModel.objects.create(user_id=request.user.id)
        bdata.fathername = request.POST['fathername']
        bdata.dob = request.POST['dob']
        bdata.marital_status = request.POST['marital_status']
        bdata.qualification = request.POST['qualification']
        bdata.address = request.POST['address']
        bdata.old_erp_esic_numbr = request.POST['old_erp_esic_numbr']
        bdata.bank_acnt = request.POST['bank_acnt']
        bdata.ifsc_code = request.POST['ifsc_code']
        bdata.police_station = request.POST['police_station']
        bdata.idnty_mark = request.POST['idnty_mark']
        bdata.dateofjoining = request.POST['dateofjoining']
        bdata.experience = request.POST['experience']
        bdata.preffered_jobs = request.POST['preffered_jobs']
        bdata.pic = request.FILES['pic']
        bdata.save()

        return redirect('profile', Id=request.user.id)
    else:
        frm = portfolioform.BiodataForm()

        return render(request, 'biodata.html',{'frm':frm})


# @login_required(login_url="signin/")
def profile(request,Id):
    try:
        bdata = BiodataModel.objects.get(user_id=Id)
    except BiodataModel.DoesNotExist:
        bdata = None

    return render(request,'profile.html', {'bdata':bdata})


def biodataPDFView(request):
    try:
        bdexist = BiodataModel.objects.get(user_id=request.user.id)
        uid = request.user.id
        print bdexist.fathername
    except BiodataModel.DoesNotExist:
        bdexist = None

    pdf = pdfkit.from_url(('http://127.0.0.1:8000/pdfdata/%d' %uid) ,False)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="biodata.pdf"'
    return response


def pdfdata(request,Id):
    try:
        bdata = BiodataModel.objects.get(user_id=Id)
    except BiodataModel.DoesNotExist:
        bdata = None

    return render(request, 'demopdf.html' ,{'bdata':bdata})


def check_user_exists_or_not(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        try:
            if User.objects.filter(username=username).exists():
                return HttpResponse('Already_used')
            else:
                return HttpResponse('Not_used')
        except:
                return HttpResponse('False')


def all_jobs_list(request):
    data =  User.objects.all()
    DataArray = []
    if data.exists():

        for code in data:
            try:
                DataArray.append('{}'.format(code.username))
            except UnicodeEncodeError:
                DataArray.append('{}'.format(code.firstname.encode("utf-8")))
    return HttpResponse(json.dumps(DataArray), content_type="application/json")

