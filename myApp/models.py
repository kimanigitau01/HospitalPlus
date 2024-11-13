from django.db import models

# Create your models here.
class Student(models.Model):
    fullname = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email =  models.EmailField()
    password = models.CharField(max_length=20)
    age = models.IntegerField()
    yob = models.DateField()

    def __str__(self):
        return self.fullname

class Product(models.Model):
    price = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    yob = models.DateField()
    gender = models.CharField(max_length=200)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.firstName

class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateTimeField()
    department = models.CharField(max_length=200)
    doctor = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name
