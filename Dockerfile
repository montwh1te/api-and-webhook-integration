# Usa uma imagem do Python 3.10
FROM python:3.10

# Instala o Node.js e o npm
RUN apt-get update && apt-get install -y nodejs npm

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências do backend
RUN pip install --no-cache-dir -r requirements.txt

# Navega para o diretório do frontend e instala as dependências
WORKDIR /app/frontend
RUN npm install

# Executa o build do frontend
RUN npm run build

# Volta para o diretório raiz e coleta os arquivos estáticos
WORKDIR /app
RUN python manage.py collectstatic --noinput

# Expor a porta que o aplicativo usará
EXPOSE 8000

# Comando que será executado ao iniciar o container
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi:application"]