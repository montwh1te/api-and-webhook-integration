#!/bin/bash

chmod +x deploy.sh

# Navega para o diretório do frontend e executa o build
cd frontend
npm install
npm run build

# Volta para o diretório raiz e coleta os arquivos estáticos
cd ..
python manage.py collectstatic --noinput

# Inicia o servidor Gunicorn
gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT