from django.shortcuts import render
from django.contrib.auth import authenticate


# Create your views here.
def index(request):

    return render(request, 'index.html')


def login(request):
    # email = request.Post.get['']
    # password = request.Post.get['']

    return render(request, 'login.html')