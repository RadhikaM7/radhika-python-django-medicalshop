from django.shortcuts import render
from .models import Highlights
from django.http import HttpResponse


# Create your views here.
def index(request):
    #Way to query all the data of table Higlights
    highlights = Highlights.objects.all()[0:3]
    headings = Highlights.objects.all()[3:6]
    return render(request,'base.html',{'highlights':highlights,'headings': headings})