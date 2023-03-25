from django.db import models

# Create your models here.
class Translator(models.Model):
    english = models.CharField(max_length=130)
    uzbek = models.CharField(max_length=130)
