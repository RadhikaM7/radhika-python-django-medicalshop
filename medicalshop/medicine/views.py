from django.shortcuts import render, get_object_or_404
from .models import Medicine
from django.http import request

# Create your views here.
def index(request):
    medicines = Medicine.objects.all()
    return render(request,'medicine.html',{'medicines':medicines})

def detail(request, batchnumber):
    detail = get_object_or_404(Medicine, pk= batchnumber)
    return render(request, 'detail.html',{'detail':detail})