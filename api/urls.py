from django.urls import path
from api.views import WebhookView

urlpatterns = [
    path('webhook/', WebhookView.as_view(), name='webhook'),   
]