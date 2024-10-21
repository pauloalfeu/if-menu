from django.urls import path
from .views import ProdutoView, ProdutoReadUpdateDeleteView, ClienteView, ClienteReadUpdateDeleteView, GerenteView, GerenteReadUpdateDeleteView

urlpatterns = [
    path('produto/', ProdutoView.as_view()),
    path('produto/<int:id>/', ProdutoReadUpdateDeleteView.as_view(), name='Produto-detail'),
    path('cliente/', ClienteView.as_view()),
    path('cliente/<int:pk>/', ClienteReadUpdateDeleteView.as_view()),
    path('gerente/', GerenteView.as_view()),
    path('gerente/<int:pk>/', GerenteReadUpdateDeleteView.as_view()),
]