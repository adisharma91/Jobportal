from django.conf.urls import url
from portfolio import views

urlpatterns = [
     url(r'^index/$', views.index, name='index'),
     url(r'^login/$', views.login, name='login')
]