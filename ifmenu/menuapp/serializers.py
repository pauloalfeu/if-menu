from rest_framework import serializers
from .models import Produto, Cliente, Gerente # Pedidos

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class GerenteSerializer(serializers.ModelSerializer):
     class Meta:
         model = Gerente
         fields = '__all__'


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'