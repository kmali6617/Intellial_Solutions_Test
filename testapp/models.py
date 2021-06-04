from django.db import models


# Create your models here.
# class Details(models.Model):
#     cst = models.CharField(max_length=20, default='',null=False)
#     prd = models.CharField(max_length=30, default='',null=False)

class Customer_details(models.Model):
    first_name=models.CharField(max_length=25, default='', null=False)
    last_name=models.CharField(max_length=25,  default='', null=False)
    contact_no=models.CharField(max_length=15, default='', null=False)
    pincode=models.IntegerField()
    
class Product_details(models.Model):
    Pname = models.CharField(max_length=20, default='', null=False)
    Unit_price=models.DecimalField(max_digits=10, decimal_places=2)
    Customer_details = models.OneToOneField(Customer_details, on_delete=models.CASCADE, related_name='Product_details')

class Order(models.Model):
    Customer_details = models.ForeignKey(Customer_details, on_delete=models.CASCADE, related_name='Order')
    Product_details = models.ForeignKey(Product_details, on_delete=models.CASCADE, related_name='Order')
    Qty=models.IntegerField(max_length=20, default='', null=False)
    Total_price = models.DecimalField(max_digits=10,decimal_places=2)
    created_date=models.DateTimeField()