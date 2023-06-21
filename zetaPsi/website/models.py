from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class MembershipRequest(models.Model):
   first_name = models.CharField(max_length=200, verbose_name='First Name')    
   last_name = models.CharField(max_length=200, verbose_name='Last Name')
   graduation_year = models.IntegerField(default=0, verbose_name='Graduation Year')
   email = models.EmailField()

   def __str__(self):
      return self.first_name + ' ' + self.last_name

class Events(models.Model):
   title = models.CharField(max_length=200)
   eventDate = models.DateField(default=timezone.now)
   eventTime = models.TimeField(default=timezone.now)
   description = models.CharField(max_length=200)

   def __str__(self):
      return self.title
