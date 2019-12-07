from django.db import models
import datetime
import os
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def post_fragment(self):
        splitted = self.body.split(2*os.linesep)
        return splitted[0]
