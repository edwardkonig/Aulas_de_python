from django.db import models

# Create your models here.
class Remedio(models.Model):
    nome = models.CharField(max_length = 500, blank = False)
    preco = models.IntegerField(default = 0)
    dosagem = models.IntegerField(default = 0)

'''
https://docs.djangoproject.com/en/3.0/
Tutorial Django para criar enquente
'''



