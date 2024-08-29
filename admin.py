from django.contrib import admin
from .models import Patient, Doctor, Appointment, Department

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(Department)
