from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from pathlib import Path

class ReactAppView(TemplateView):
    template_name = "index.html"

    def get_template_names(self):
        template_path = Path(settings.BASE_DIR) / "frontend" / "build" / "index.html"
        if not template_path.exists():
            raise ValueError(f"Arquivo {template_path} não encontrado. Rode 'npm run build'.")
        return [str(template_path)]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),  # Mantém a API funcionando normalmente
    re_path(r"^.*$", ReactAppView.as_view()),  # Serve o React para todas as outras rotas
]