from django.db import models
from django.contrib.auth.models import AbstractUser

class Cliente(AbstractUser):
    contato = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True, null=False)


class Gerente(models.Model):
     login = models.CharField(max_length=200)
     senha = models.CharField(max_length=200)
     def __str__(self):
         return self.login

class Produto(models.Model):
    nome_prod = models.CharField(max_length=200)
    preco_prod = models.FloatField()
    descricao_prod = models.CharField(max_length=600)
    img_prod = models.CharField(max_length=900)
    def __str__(self):
        return self.nome_prod
    

