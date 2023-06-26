from django.db import models
from django.contrib.auth.models import User
from unicodedata import name


class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    upload_date = models.CharField(max_length=30)
    program = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    notesfile = models.FileField(null=True)
    filetype = models.CharField(max_length=30)
    description = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=15)

    class Meta:
       db_table = 'notes'
    
    def __str__(self):
        return 'note uploaded by ' + self.name 