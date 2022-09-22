from django.db import models

# Create your models here.

class Weather(models.Model):
    """Weather model """

    date = models.DateField()
    rain = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f'{self.date} {self.rain}'
