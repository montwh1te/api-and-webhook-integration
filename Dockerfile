# Usa uma imagem do Python 3.10
FROM python:3.10

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências do projeto
RUN pip install -r requirements.txt

# Comando que será executado ao iniciar o container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]