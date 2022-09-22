from django.db import models

# Create your models here.

class CustomerOrder(models.Model):
    """ Customer Order Model """
    
    order_id = models.CharField(max_length=20)
    order_date = models.DateField()
    quantity = models.CharField(max_length=5)


    def __str__(self):
        return f'{self.order_id}'
