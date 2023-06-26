from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from unicodedata import name

class Contact(models.Model):
    serialno = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return 'Message from ' + self.name    
    class Meta:
        db_table = 'contact_us'
