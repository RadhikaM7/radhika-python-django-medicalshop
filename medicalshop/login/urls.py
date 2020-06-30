from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns =[
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('', views.signupuser, name='signup'),

    #url(r'^/login/$',views.login,name='login'),
    #url(r'^$', views.index, name='signup')
]