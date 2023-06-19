from django.db import models

# Create your models here.
class MembershipRequest(models.Model):
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   year = models.IntegerField()
   email = models.EmailField()