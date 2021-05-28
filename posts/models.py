from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self):
        return self.title[:50]