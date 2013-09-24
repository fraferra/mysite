from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):

    #user = models.OneToOneField(User)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    
    UNIVERSITY_CHOICES = (
        ('UC', 'UCL'),
        ('KE', 'Kent'),
        ('EP', 'EPFL'),
    )
    university = models.CharField(max_length=2,
                                      choices=UNIVERSITY_CHOICES,
                                      default = 'UC')
 



    def __unicode__(self):  # Python 3: def __str__(self):
        return self.last_name
   
