from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mensagem
import requests

class WebhookView(APIView):
    def post(self, request):
        data = request.data
        usuario = data.get('usuario')
        mensagem = data.get('mensagem', '').lower()
        
        resposta = "Desculpe, não entendi sua mensagem."
        
        if 'meus pedidos' in mensagem:
            pedidos = requests.get('https://fakestoreapi.com/products').json()
            resposta = f"Você tem {len(pedidos)} pedidos restantes"
            
            Mensagem.objects.create(usuario=usuario, mensagem=mensagem, resposta=resposta)
            
            return Response({'resposta': resposta}, status=status.HTTP_200_OK)
            
