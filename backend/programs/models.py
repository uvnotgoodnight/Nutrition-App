from django.db import models

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration_days = models.IntegerField()

    def __str__(self):
        return self.name