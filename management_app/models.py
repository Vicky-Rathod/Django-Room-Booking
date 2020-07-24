from django.db import models
import datetime
from django.utils.timezone import now
# Create your models here.
Gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class Customer(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    alternate_phone = models.CharField(max_length=20)
    address = models.TextField()
    customer_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=6, choices=Gender)
    auth_number = models.CharField(max_length=10)

class Rooms(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class CheckIn(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    purpose_of_booking = models.CharField(max_length=200, blank=True)
    partner_name = models.CharField(max_length=200, )
    checkin_id = models.AutoField(primary_key=True)
    room_type = models.ForeignKey(Rooms, on_delete=models.CASCADE, blank=True)
    date_of_checkin = models.DateField(default=datetime.date.today)
    time_of_checkin = models.TimeField(blank=True, default=now)

    def __str__(self):
        return self.customer.firstname

class CheckOut(models.Model):
    id =  models.AutoField(primary_key=True)
    checkin = models.ForeignKey(CheckIn, on_delete=models.CASCADE, default=None)
    date_of_checkout = models.DateField(default=datetime.date.today)
    time_of_checkout = models.TimeField(blank=True, default=now)
