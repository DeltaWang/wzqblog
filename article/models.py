from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 80)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length = 30)
    publish_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-publish_time']
