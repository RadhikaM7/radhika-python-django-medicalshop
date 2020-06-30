from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.index, name='medicine'),
    path('<str:batchnumber>/', views.detail,name='detail')
    #url(r'^$', views.index, name='medicine')
]
