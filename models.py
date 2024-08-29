from django.db import models



class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.date}"


    
    
    
    
class Report(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    report_date = models.DateField()
    details = models.TextField()

    def __str__(self):
        return f"Report for {self.patient} by {self.doctor} on {self.report_date}"
    
    
    
    
