from django.urls import path
from api.views import WebhookView, EnviarWebhookView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('webhook/', WebhookView.as_view(), name='webhook'),
    path('enviar-webhook/', EnviarWebhookView.as_view(), name='enviar-webhook'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]