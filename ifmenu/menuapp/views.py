from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

#importando modelos e serializers
from .models import Produto, Cliente, Gerente # Pedidos
from .serializers import ProdutoSerializer, ClienteSerializer, GerenteSerializer # PedidosSerializer

# Create your views here.
class ProdutoView(APIView):

    # Define as ações quando recebe um requisicao do tipo post
    
    # POST
    def post(self, request):

        # Instancia o serialize com os dados recebidos no 'request'
        serializer = ProdutoSerializer(data = request.data)
        if serializer.is_valid():

            # Se o formato recebido estiver correto, salva os dados no banco de dados
            serializer.save()

            # Retorna com o codigo 201 e os dados do serializer
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        # Se o serializer não for valido, retorna erro 400
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    # GET
    def get(self, request):
        Produtos = Produto.objects.all()
        serializer = ProdutoSerializer(Produtos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ProdutoReadUpdateDeleteView(APIView):
# View para recuperar, atualizar ou deletar um Produto específico.

    # GET
    def get(self, request, id):
        Produto = get_object_or_404(Produto, pk=id)
        
        '''
            try:
                Produto = Produto.objects.get(pk=pk)
            except Produto.DoesNotExist:
                return Response({'detail': 'Produto não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        '''
        
        serializer = ProdutoSerializer(Produto)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # PUT
    def put(self, request, id):
        Produto = get_object_or_404(Produto, pk=id)
        serializer = ProdutoSerializer(Produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # DELETE
    def delete(self, request, id):
        Produto = get_object_or_404(Produto, pk=id)
        Produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

############################################
############################################ CLIENTE
############################################

class ClienteView(APIView):

    #define as ações quando recebe um requisicao do tipo post
    def post(self, request):

        #instancia o serialize com os dados recebidos no 'request'
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():

            #se o formato recebido estiver correto, salva os dados no banco de dados
            serializer.save()

            #retorna com o codigo 201 e os dados do serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        #se o serializer não for valido, retorna erro 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        Clientes = Cliente.objects.all()
        serializer = ClienteSerializer(Clientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClienteReadUpdateDeleteView(APIView):
    """
    View para recuperar, atualizar ou deletar um Cliente específico.
    """

    def get(self, request, pk):
        Cliente = get_object_or_404(Cliente, pk=pk)

        '''
        try:
            Cliente = Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return Response({'detail': 'Cliente não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        '''

        serializer = ClienteSerializer(Cliente)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        Cliente = get_object_or_404(Cliente, pk=pk)
        serializer = ClienteSerializer(Cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Cliente = get_object_or_404(Cliente, pk=pk)
        Cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

############################################
############################################ GERENTE 
############################################


class GerenteView(APIView):

    #define as ações quando recebe um requisicao do tipo post
    def post(self, request):

        #instancia o serialize com os dados recebidos no 'request'
        serializer = GerenteSerializer(data=request.data)
        if serializer.is_valid():

            #se o formato recebido estiver correto, salva os dados no banco de dados
            serializer.save()

            #retorna com o codigo 201 e os dados do serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        #se o serializer não for valido, retorna erro 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        Gerentes = Gerente.objects.all()
        serializer = GerenteSerializer(Gerentes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GerenteReadUpdateDeleteView(APIView):

    def get(self, request, pk):
        Gerente = get_object_or_404(Gerente, pk=pk)
        serializer = GerenteSerializer(Gerente)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        Gerente = get_object_or_404(Gerente, pk=pk)
        serializer = GerenteSerializer(Gerente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Gerente = get_object_or_404(Gerente, pk=pk)
        Gerente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
####################################################################
####################################################################