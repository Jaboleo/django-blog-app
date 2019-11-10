from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100, blank=True, default = 'anonymous')
    date = models.DateField(("Date"), default=datetime.datetime.now())
    body = models.TextField()

    def __str__(self):
        return self.title