from django.shortcuts import render
from django.contrib.auth import authenticate,login, logout
from portfolio import forms as portfolioform
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):

    return render(request, 'index.html')


def signin(request):

    return render(request, 'signin.html')

def signup(request):
    userfrm = portfolioform.Userform()
    flag = 'none';

    if request.method == 'POST':
        # isemailexists = User.objects.filter(email=request.POST['email']).count();
        # if isemailexists > 0:
        #     return render(request, 'signup.html', {'request': request, 'userform': userfrm,'flag':'block'});

        user = User.objects.create_user(request.POST['email'],request.POST['email'],request.POST['password'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        user.save()
        login(request, user);
        return render(request, 'index.html');
    else:
        userfrm = portfolioform.Userform()
        return render(request, 'signup.html', {'request': request, 'userform': userfrm});