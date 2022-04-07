from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User =get_user_model()
class Order(models.Model):
    SIZES=(
        ('SMAILL','small'),
        ('MEDIUM','medium'),
        ('LARGE','large'),
        ('EXTRA_LARGE','extraLarge'),
    )
    ORDER_STATUS=(
        ('PENDING','pending'),
        ('IN_TRANSIT','inTransit'),
        ('DELIVERED','delivered'),
    )
    customer=models.ForeignKey(User, on_delete=models.CASCADE)# cascade:When the referenced object is deleted, also delete the objects that have references to it 
    size=models.CharField(max_length=20,choices=SIZES, default=SIZES[0][0])
    order_status=models.CharField(max_length=20, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)########## called while creating the object
    updated_at=models.DateTimeField(auto_now=True)######### called while updating the object


    def __str__(self):
        return f"<Order {self.size} by {self.customer.id}>"
