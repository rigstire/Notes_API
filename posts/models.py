from django.db import models
from django.urls import reverse

class Notes(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse('home')