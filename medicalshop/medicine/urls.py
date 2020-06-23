from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='medicine'),
    #url(r'^$', views.index, name='medicine')
]
