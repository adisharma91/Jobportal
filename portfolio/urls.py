from django.conf.urls import url
from portfolio import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^signin/$', views.signin, name='signin'),
     url(r'^signup/$', views.signup, name='signup'),
     url(r'^signout/$',views.signout, name='signout'),
     url(r'^biodata/(?P<Id>[\w-]+)$', views.biodata, name='biodata'),
     url(r'^profile/(?P<Id>[\w-]+)$', views.profile, name='profile'),
     url(r'^forgotpassword/$', views.forgotpassword, name='forgotpassword'),
     url(r'^biodatapdf/(?P<Id>[\w-]+)$', views.biodataPDFView, name='biodatapdf'),
     url(r'^check_user_exists_or_not/$', views.check_user_exists_or_not, name='check_user_exists_or_not'),
     url(r'^all_jobs_list/$', views.all_jobs_list, name='all_jobs_list'),
     url(r'^pdfdata/(?P<Id>[\w-]+)$', views.pdfdata, name='pdfdata'),
     url(r'^postjob/$', views.postjob, name='postjob'),
     url(r'^jobs/$', views.jobsview, name='jobs'),
     url(r'^jobdetail/(?P<Id>[\w-]+)$', views.jobdetail, name='jobdetail'),
     url(r'^apply/(?P<Id>[\w-]+)$', views.apply, name='apply'),
     url(r'^users/$', views.users, name='users'),
]