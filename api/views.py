from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Mensagem
import requests
from django.http import JsonResponse

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
        
class EnviarWebhookView(APIView):
    def post(self, request):
        
        ultima_mensagem = Mensagem.objects.last()
        
        if not ultima_mensagem:
            return Response({"erro": "Nenhuma mensagem encontrada"}, status=404)
        
        payload = {
            'usuario': ultima_mensagem.usuario,
            'mensagem': ultima_mensagem.mensagem,
            'resposta': ultima_mensagem.resposta,
        }
        
        url_webhook_externo = "https://webhook.site/42f13262-823d-4efd-a4f7-e258b3fcbb76"
        response = requests.post(url_webhook_externo, json=payload)
        
        if response.status_code == 200:
            return Response({"mensagem": "Webhook enviado com sucesso"}, status=200)
        else:
            return Response({"erro": "Falha ao enviar webhook"}, status=500)
