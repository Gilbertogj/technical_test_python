from django.db import models

# Create your models here.

class CustomerOrder(models.Model):
    order_id = models.CharField(max_length=20)
    order_date = models.DateField()
    quantity = models.CharField(max_length=5)

    # def season_status(self):
    #     "Returns the person's baby-boomer status."
    #     import datetime
    #     if self.order_date < datetime.date(1945, 8, 1):
    #         return "Pre-boomer"
    #     elif self.order_date < datetime.date(1965, 1, 1):
    #         return "Baby boomer"
    #     else:
    #         return "Post-boomer"

    def __str__(self):
        return f'{self.order_id}'
