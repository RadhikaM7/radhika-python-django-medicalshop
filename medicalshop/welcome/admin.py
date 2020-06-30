from django.contrib import admin
from .models import Highlights

# Register your models here.

class OfferWelcome(admin.ModelAdmin):
  list_display = ('title','description')
#By writing the below line we are registering our Higlights Model to the Admin Site

admin.site.register(Highlights, OfferWelcome)

