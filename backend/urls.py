from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from pathlib import Path
import logging

class ReactAppView(TemplateView):
    template_name = "index.html"

    def get_template_names(self):
        template_path = Path(settings.BASE_DIR) / "frontend" / "build" / "index.html"
        logging.info(f"Verificando o caminho do template: {template_path}")
        
        if not template_path.exists():
            logging.error(f"Arquivo {template_path} não encontrado. Rode 'npm run build'.")
            raise ValueError(f"Arquivo {template_path} não encontrado. Rode 'npm run build'.")
        
        logging.info(f"Arquivo {template_path} encontrado.")
        return [str(template_path)]

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls")),
    re_path(r"^(?!api/|admin/).*", ReactAppView.as_view()),
]