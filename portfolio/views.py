from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from portfolio import forms as portfolioform
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):

    return render(request, 'index.html')


def signin(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

        if user is not None:
            if user.is_active:
                login(request, user)

            return render(request, 'index.html')
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