from django.db import models

# Create your models here.


class Post(models.Model):
    text = models.CharField(max_length=100)
    day = models.DateField()
    reminder = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.text
