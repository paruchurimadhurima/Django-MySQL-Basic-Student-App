from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length = 250)
    age = models.IntegerField()
    gender = models.CharField(max_length = 20)

    class Meta:
        unique_together = ('name', 'age', 'gender')
