# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Bus(models.Model):
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    destination = models.CharField(max_length=30)
    number_of_seats = models.DecimalField(decimal_places=0, max_digits=2)
    remaining_seats = models.DecimalField(decimal_places=0, max_digits=2)
    bus_fare = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    departure_time = models.TimeField()

    def __str__(self):
        return self.bus_name

# default user model used
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     email = models.EmailField()
#     name = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#
#     def __str__(self):
#         return self.email


class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    booked_by=models.ForeignKey(User,on_delete=models.CASCADE)
    bus_booked=models.ForeignKey(Bus,on_delete=models.CASCADE)
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=2)
    date_booked=models.DateField(default=timezone.now)

    def __str__(self):
        return self.booked_by
    # minimized by inheritance
    # email = models.EmailField()
    # name = models.CharField(max_length=30)
    # userid =models.DecimalField(decimal_places=0, max_digits=2)
    # busid=models.DecimalField(decimal_places=0, max_digits=2)
    # bus_name = models.CharField(max_length=30)
    # source = models.CharField(max_length=30)
    # dest = models.CharField(max_length=30)
    # nos = models.DecimalField(decimal_places=0, max_digits=2)
    # price = models.DecimalField(decimal_places=2, max_digits=6)
    # date = models.DateField()
    # time = models.TimeField()
