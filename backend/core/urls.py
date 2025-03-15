from django.urls import path
from .views import *

urlpatterns = [
    path('pedido/', PedidoView.as_view()),
    path('pedido/<int:id>', PedidoView.as_view()),
    path('validate/<int:id>', ValidarPedidoView.as_view()), 
    path('pedido/<int:id>/aprovar/', ValidarPedidoView.as_view()), 
    path('pedido/<int:id>/reprovar/', ValidarPedidoView.as_view()), 
]


