from django.db import models
import datetime
from django.contrib.auth import get_user_model


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField(("Date"), default=datetime.datetime.now())
    body = models.TextField()

    def __str__(self):
        return self.title