FROM python:3.11

# Mantenedor / quem está disponibilizando a aplicação 
LABEL maintainer="beatrizbramont"

# Define diretório de trabalho / pasta que vamos trabalhar
WORKDIR /app1

# Copia os arquivos / cópia da nossa aplicação para transformar em imagem
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expõe a porta da aplicação / trabalha com as nossas portas
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "app.py"]
