from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns =[
    path('login/', views.login, name='login'),
    path('', views.index, name='signup'),
    #url(r'^/login/$',views.login,name='login'),
    #url(r'^$', views.index, name='signup')
]