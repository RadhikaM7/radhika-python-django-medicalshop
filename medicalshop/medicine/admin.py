from django.contrib import admin
from .models import Medicine

# Register your models here.
#IMP: There is another way of doing this which is by model. Check the welcome.model
# By adding str method and returning the fields we want to show. Not working for me

#def __str__(self):
 # return self.title

class OfferMedicine(admin.ModelAdmin):
    list_display =('name', 'batchNumber', 'company','expiryDate')


admin.site.register(Medicine, OfferMedicine)