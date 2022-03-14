from django.db import models
from django.contrib.auth.models import User




class Location(models.Model):
    abbrev              = models.CharField(max_length=10)
    title               = models.CharField(max_length=100)

    def __str__(self):
        return '%s (%s)' % (self.title, self.abbrev)


class Customer(models.Model):
    abbrev              = models.CharField(max_length=10)
    title               = models.CharField(max_length=100)
    location            = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return '%s (%s)' % (self.title, self.abbrev)


class Project(models.Model):
    number              = models.CharField(max_length=7)
    title               = models.CharField(max_length=100)
    customer            = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s (%s)' % (self.number, self.title, self.customer.abbrev)


class Staff(models.Model):
    email               = models.CharField(max_length=255, unique=True)
    first_name          = models.CharField(max_length=32)
    last_name           = models.CharField(max_length=32)
    user                = models.OneToOneField(User, on_delete=models.CASCADE)
    home_location       = models.OneToOneField(Location, on_delete=models.CASCADE)

    def __str__(self):
        return '%s, %s (%s)' % (self.last_name, self.first_name, self.user)

    class Meta:
        ordering = ['last_name', 'first_name']

