#!/bin/bash

echo "Iniciando deploy..."

# Navega para o diretório do frontend e executa o build
cd frontend
echo "Instalando dependências do frontend..."
npm install
echo "Executando build do frontend..."
npm run build
echo "Build do frontend concluído."

# Volta para o diretório raiz e coleta os arquivos estáticos
cd ..
echo "Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

# Inicia o servidor Gunicorn
echo "Iniciando Gunicorn..."
gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT