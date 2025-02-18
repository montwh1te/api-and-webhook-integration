from django.urls import path
from api.views import WebhookView, EnviarWebhookView

urlpatterns = [
    path('webhook/', WebhookView.as_view(), name='webhook'),
    path('enviar-webhook/', EnviarWebhookView.as_view(), name='enviar-webhook'),
]