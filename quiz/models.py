from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=100)

    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    
    answer  = models.CharField(max_length=100)