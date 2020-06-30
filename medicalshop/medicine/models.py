from django.db import models


# Create your models here.
class Medicine(models.Model):
    id = models.IntegerField(auto_created=True)
    name = models.CharField(max_length=100)
    batchNumber = models.CharField(max_length=10, primary_key=True)
    company = models.CharField(max_length=100)
    quantity = models.IntegerField()
    expiryDate = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="medicine/images")
    medicineType = models.CharField(max_length=10)
    description = models.CharField(max_length=255)


#class Wishlist(models.Model):
 #   medicine = models.ForeignKey('medicine.Medicine', on_delete=models.CASCADE)
  #  user = models.ForeignKey('login.User', on_delete=models.CASCADE)
