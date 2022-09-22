from django.db import models

# Create your models here.

class Order(models.Model):
    """ Orders Model"""

    order_number = models.CharField(max_length=10)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order_number}'



class OrderLine(models.Model):
    """ Orders lines Model"""

    

    class ItemName(models.TextChoices):
        LAPTOP = 'LAPTOP', 'Laptop'
        MOUSE = 'MOUSE', 'Mouse'
        KEYBOARD = 'KEYBOARD', 'Keyboard'
        GAME = 'GAME', 'Game'
        BOOK = 'BOOK', 'Book'
        SHIRT = 'SHIRT', 'Shirt'
        PANTS = 'PANTS', 'Pants'
        TV = 'TV', 'TV'
        DVD = 'DVD', 'DVD'
    
    item_name = models.CharField(
        max_length=8,
        choices=ItemName.choices,
        verbose_name="item name", 
    )

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        SHIPPED = 'SHIPPED', 'Shipped'
        CANCELLED = 'CANCELLED', 'Cancelled'
    
    status = models.CharField(
        max_length=9,
        choices=Status.choices,
        verbose_name="order status",
        default=Status.PENDING,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    # Relations
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orders_lines")

    def __str__(self):
        return f'order:{self.order.order_number} {self.item_name}'
    









