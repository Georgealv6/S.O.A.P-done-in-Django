from django.db import models
from django.contrib.auth.models import User


Gender_Choices = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other")
)   

# Create your models here
class UserProfile(models.Model): 
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures', default='uploads/profile_pictures/default.png', blank=True)

class PatientInfo(models.Model):
    patient_name = models.CharField(max_length=100)
    ssn = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=45)
    DOB = models.DateField(auto_now_add=False, auto_now=False, blank=True,)
    age = models.IntegerField(blank=True)
    gender = models.CharField(max_length=20, choices=Gender_Choices)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)


    def __str__(self):
        return self.patient_name 



class RegisteredPatient(models.Model):
    patient = models.ForeignKey(PatientInfo, null=True, on_delete= models.SET_NULL)

