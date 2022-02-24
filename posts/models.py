from django.db import models
from django.urls import reverse
from django.conf import settings

class Notes(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=5, blank=True, null=False)
    folder = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.folder[:50]

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    root_note = models.ForeignKey(Notes, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    done = models.BooleanField(default=False)
    

    def __str__(self):
        return self.comment
    
    def get_absolute_url(self):
        return reverse('home')
