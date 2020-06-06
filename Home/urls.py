from django.conf.urls import url
from django.urls import include, path
from .import views
urlpatterns = [
    url(r'^$',views.homepage,name='home'),
    url(r'^spot/$',views.homepage,name='home'),
    url(r'^loginpage/$',views.loginpage,name="login"),
    url(r'^loginformsubmit/$',views.loginformsubmit,name="loginform"),
    url(r'^register/$', views.Register, name="register"),
    url(r'^registersubmit/$', views.Registersubmit, name="registersubmit"),
    url(r'^show/$', views.show, name="show"),
    url(r'^noti/$', views.noti, name="noti"),
    url(r'^editdelete/$', views.editdelete, name="editdelete"),
    url(r'^registerstudentinfo/$', views.registerstudentinfo, name="registerstudentinfo"),
    url(r'^gdstudentinfo/$', views.gdstudentinfo, name="gdstudentinfo"),
    url(r'^pptstudentinfo/$', views.pptstudentinfo, name="pptstudentinfo"),
    url(r'^gdsubmit/$', views.gdsubmit,name="gdsubmit"),
    url(r'^judgesubmit/$', views.judgesubmit, name="judgesubmit"),
    url(r'^winner/$', views.winner, name="winner"),
    url(r'^winnersubmit/$', views.winnersubmit, name="winnersubmit"),
    url(r'^deletee/$', views.deletee, name="deletee"),
]
