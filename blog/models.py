from django.db import models
from django.utils import timezone

class Posts(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=15)
    slug = models.CharField(max_length=50)
    timeStamp = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return "message from" + self.title + " - "+self.author