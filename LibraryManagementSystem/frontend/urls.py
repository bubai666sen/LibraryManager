
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.login_or_signup,name="login_or_signup"),
    path('signup', views.signup,name="signup"),
    path('signin', views.signin,name="signin"),
    path('index', views.index,name="index"),
    path('request-book', views.requestBook,name="request_book"),
    #url(r'^index/(?P<user_id>\d+)/$', views.index, name='index')
    url(r'^logout/$', views.logout_view,name="custom_logout")
]
