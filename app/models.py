from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=123)
    text = models.CharField(max_length=9999)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
