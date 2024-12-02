from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    contato = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=False)
    is_manager = models.BooleanField(default=False, null=False)
    def __str__(self):
        return self.email

class Produto(models.Model):
    nome_prod = models.CharField(max_length=200)
    preco_prod = models.FloatField()
    descricao_prod = models.CharField(max_length=600)
    img_prod = models.ImageField(upload_to='produtos_imagens/')
    def __str__(self):
        return self.nome_prod
    

