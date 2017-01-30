from django.conf.urls import url
from portfolio import views

urlpatterns = [
     url(r'^index/$', views.index, name='index')
]