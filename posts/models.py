from django.db import models
from django.urls import reverse
from django.conf import settings

class Notes(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=5, blank=True, null=False)
    title = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return reverse('home')