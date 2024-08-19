from taskmanager import db
from django.db import models
from django.utils import timezone

class Table(models.Model):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.number} (Seats {self.capacity})"

class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField()
    special_requests = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Booking for {self.name} on {self.date} at {self.time}"

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cancellation(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    reason = models.TextField(blank=True, null=True)
    cancelled_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Cancellation for booking {self.booking.id}"