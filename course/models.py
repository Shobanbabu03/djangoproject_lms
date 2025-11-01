from django.db import models
from django.conf import settings

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    trainers = models.ManyToManyField(
         settings.AUTH_USER_MODEL, 
         limit_choices_to={'role':'TRAINER'},
         related_name='courses_trained'
         )
    
    def __str__(self):
        return self.title

