from django.db import models
from django.contrib.auth.models import User
from customuser.models import CustomUser,Counsellor


class Appointment(models.Model):
    user = models.ForeignKey(Counsellor, on_delete=models.CASCADE, null=True, default=None)
    councellor_name = models.CharField(max_length=255)
    councellor_email = models.CharField(max_length=255)
    a_date=models.DateField()
    a_time= models.TimeField()
    approved= models.BooleanField(default=False)
                                      
    def __str__(self):
        return f"{self.councellor_name}"
    


class AppointmentRequest(models.Model):
    posted_by = models.CharField(max_length=20 , default=None)
    requested_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, default=None)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, default=None)
    reason = models.TextField(blank=True)
    mobile  = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    approved= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.requested_by} ({self.appointment}) - posted by {self.posted_by}"


 #######Shafiul

from django.db import models

class Document(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class PatientStory(models.Model):
    patient_name = models.CharField(max_length=100)
    story_title = models.CharField(max_length=200)
    story_content = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.story_title