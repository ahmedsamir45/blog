from django.db import models
from django.utils import timezone

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, null=True, blank=True)
    content = models.TextField()
    timeStamp = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return "message from" + self.name + " - "+self.email