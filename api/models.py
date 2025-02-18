from django.db import models

class Mensagem(models.Model):
    usuario = models.CharField(max_length=100)
    mensagem = models.TextField()
    resposta = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now_add=True)
