from django.contrib import admin
from myApp.models import Student, Product, Patient, Appointment, Contact

# Register your models here.
admin.site.register(Student)
admin.site.register(Product)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Contact)