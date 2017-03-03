from django.conf.urls import url
from portfolio import views

urlpatterns = [
     url(r'^index/$', views.index, name='index'),
     url(r'^signin/$', views.signin, name='signin'),
     url(r'^signup/$', views.signup, name='signup'),
     url(r'^signout/$',views.signout, name='signout'),
     url(r'^biodata/(?P<Id>[\w-]+)$', views.biodata, name='biodata'),
     url(r'^profile/(?P<Id>[\w-]+)$', views.profile, name='profile'),
     url(r'^forgotpassword/$', views.forgotpassword, name='forgotpassword'),
     url(r'^biodatapdf/$', views.biodataPDFView, name='biodatapdf'),
     url(r'^check_user_exists_or_not/$', views.check_user_exists_or_not, name='check_user_exists_or_not'),
]
