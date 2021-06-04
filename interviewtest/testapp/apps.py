from django.apps import AppConfig
from testapp.models import Customer_details,Order,Product_details

class TestappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'testapp'
 
 