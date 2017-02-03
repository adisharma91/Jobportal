from django.conf.urls import url
from portfolio import views

urlpatterns = [
     url(r'^index/$', views.index, name='index'),
     url(r'^signin/$', views.signin, name='signin'),
     url(r'^signup/$', views.signup, name='signup'),
]