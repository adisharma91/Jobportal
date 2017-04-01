from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from portfolio import forms as portfolioform
from django.http import HttpResponseRedirect, response
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import *
import json
import pdfkit
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    user_numbr = MyUser.objects.all().count()

    try:
        usr = MyUser.objects.get(id=request.user.id)
    except MyUser.DoesNotExist:
        usr = None

    applied = JobsApplied.objects.filter(userid_id=request.user.id)

    j = []
    if applied:
        for job in applied:
            jb = job.jobid_id
            j.append(jb)

        jobs = JobsModel.objects.all().exclude(id__in=j).order_by('-id')[:10]

        return render(request, 'index.html', {'user_numbr': user_numbr, 'jobs': jobs, 'usr':usr})
    else:
        jobs = JobsModel.objects.filter().order_by('-id')[:10]

        return render(request, 'index.html', {'user_numbr': user_numbr, 'jobs': jobs, 'usr':usr})


def signin(request):
    if request.method == 'POST':
        form = portfolioform.LoginForm(data=request.POST)
        if form.is_valid():

            user = authenticate(email=request.POST['email'], password=request.POST['password'])

            if user is not None:

                if user.is_active:
                    login(request, user)

                    return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Username/Password do not match. Please try again.')
            return render(request, 'signin.html')
    else:
        form = portfolioform.LoginForm()

    context = {'form': form}
    return render(request, 'signin.html', context)


def forgotpassword(request):
    if request.method == 'POST':
        if MyUser.objects.filter(email=request.POST.get('email')).exists():
            eml = request.POST.get('email')

            u = MyUser.objects.get(email=eml)
            password = MyUser.objects.make_random_password()
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
    return redirect('/')


def signup(request):
    if request.method == 'POST':
        userfrm = portfolioform.UserCreationForm(request.POST)

        if MyUser.objects.filter(email=request.POST.get('email')).exists():
            messages.add_message(request, messages.INFO, 'Email already exists !!')
            return render(request, 'signup.html', {'userform': userfrm})

        if userfrm.is_valid():
            userfrm.save()

            user = authenticate(email=request.POST['email'], password=request.POST['password1'])

            login(request, user)
            subject = 'Welcome to Job Portal.'
            message = 'Thank you for being part of us. \n We are glad to have you. \n Regards \n Team Job Portal'
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email, settings.EMAIL_HOST_USER]

            send_mail(subject, message, from_email, to_list, fail_silently=True)
            return HttpResponseRedirect('/',{'userform': userfrm})
        else:
            userfrm = portfolioform.UserCreationForm(request.POST)
            return render(request, 'signup.html', {'userform': userfrm})
    else:
        userfrm = portfolioform.UserCreationForm()

    return render(request, 'signup.html', {'userform': userfrm})


@login_required(login_url=settings.LOGIN_URL)
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


@login_required(login_url=settings.LOGIN_URL)
def profile(request,Id):
    try:
        bdata = BiodataModel.objects.get(user_id=Id)
    except BiodataModel.DoesNotExist:
        bdata = None

    return render(request,'profile.html', {'bdata':bdata})


@login_required(login_url=settings.LOGIN_URL)
def biodataPDFView(request,Id):
    uid = int(Id)
    path_wkthmltopdf = r'C:\Python27\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    pdf = pdfkit.from_url(('http://127.0.0.1:8000/pdfdata/%d' %uid), False, configuration=config)
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
    data = MyUser.objects.all()
    DataArray = []
    if data.exists():

        for code in data:
            try:
                DataArray.append('{}'.format(code.username))
            except UnicodeEncodeError:
                DataArray.append('{}'.format(code.firstname.encode("utf-8")))
    return HttpResponse(json.dumps(DataArray), content_type="application/json")


@login_required(login_url=settings.LOGIN_URL)
def postjob(request):
    if request.method == 'POST':
        frm = portfolioform.JobsForm(request.POST, request.FILES)

        logo = request.FILES.get('dept_logo')
        if logo:
           frm.save()
        else:
            job = JobsModel.objects.create(jobtitle=request.POST['jobtitle'],
                                           description=request.POST['description'],
                                           department=request.POST['department'],
                                           location=request.POST['location'],
                                           qualification=request.POST['qualification'],
                                           experience=request.POST['experience'],
                                           vacancies=request.POST['vacancies'],
                                           salary=request.POST['salary'],
                                           lastdate=request.POST['lastdate'],
                                           interview_process=request.POST['interview_process'],
                                           interview_venue=request.POST['interview_venue'],
                                           doj=request.POST['doj'],
                                           bondtime=request.POST['bondtime'],
                                           about=request.POST['about'],
                                           dept_logo='logo/soslogo.png'
                                           )
            job.save()

        return HttpResponseRedirect('/')
    else:
        frm = portfolioform.JobsForm()

        return render(request, 'postjob.html',{'frm':frm})


def jobsview(request):
    applied = JobsApplied.objects.filter(userid_id=request.user.id)

    j = []
    if applied:
        for job in applied:
            jb = job.jobid_id
            j.append(jb)

        jobs_list = JobsModel.objects.all().exclude(id__in=j).order_by('-id')
    else:
        jobs_list = JobsModel.objects.all().order_by('-id')

    page = request.GET.get('page', 1)

    paginator = Paginator(jobs_list, 5)
    try:
        jobs = paginator.page(page)
    except PageNotAnInteger:
        jobs = paginator.page(1)
    except EmptyPage:
        jobs = paginator.page(paginator.num_pages)

    return render(request,'jobs.html', {'jobs': jobs})


@login_required(login_url=settings.LOGIN_URL)
def apply(request, Id):
    if request.POST:
        applied = JobsApplied.objects.create(jobid_id=Id,
                                             userid_id=request.user.id
                                             )
        applied.save()

    return JsonResponse({'success': True})


def jobdetail(request, Id):
    try:
        job = JobsModel.objects.get(id=Id)
    except JobsModel.DoesNotExist:
        job = None

    return render(request, 'jobdetails.html', {'job': job})


@login_required(login_url=settings.LOGIN_URL)
def users(request):
    try:
        users = BiodataModel.objects.all()
    except BiodataModel.DoesNotExist:
        users = None

    page = request.GET.get('page', 1)

    paginator = Paginator(users, 20)
    try:
        usrs = paginator.page(page)
    except PageNotAnInteger:
        usrs = paginator.page(1)
    except EmptyPage:
        usrs = paginator.page(paginator.num_pages)

    return render(request, 'users.html', {'users': usrs})