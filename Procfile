web: |
  echo "Iniciando deploy..."
  cd frontend
  echo "Instalando dependências do frontend..."
  npm install
  echo "Executando build do frontend..."
  npm run build
  echo "Build do frontend concluído."
  cd ..
  echo "Coletando arquivos estáticos..."
  python manage.py collectstatic --noinput
  echo "Iniciando Gunicorn..."
  gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT