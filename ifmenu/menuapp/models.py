from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    contato = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=False)
    is_manager = models.BooleanField(default=False, null=False)
    def __str__(self):
        return self.email

CATEGORY_CHOICES = [
    ('salgados', 'Salgados'),
    ('doces', 'Doces'),
    ('bebidas', 'Bebidas'),
    ('outros', 'Outros'),
    ('em promoção', 'Em Promoção'),
]

class Produto(models.Model):
    nome_prod = models.CharField(max_length=200)
    valor_und = models.FloatField()
    descricao_prod = models.CharField(max_length=600)
    category_prod = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    img_prod = models.ImageField(upload_to='produtos_imagens/')
    qtd_disp = models.IntegerField()
    def __str__(self):
        return self.nome_prod

# Para obter todos os produtos da categoria "lanche"
#lanches = Produto.objects.filter(category_prod='lanche')
    
STATUS_CHOICES = [
    ('pendente', 'Pendente'),
    ('entregue', 'Entregue'),
    ('cancelado', 'Cancelado'),
    ('finalizado', 'Finalizado'),
]

class Pedido(models.Model):
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_pedido = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    itens_pedido = models.ForeignKey(ItensPedido, on_delete=models.CASCADE)

class ItensPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveSmallIntegerField(null=True, blank=True)