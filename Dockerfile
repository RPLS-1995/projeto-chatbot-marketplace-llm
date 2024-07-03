# Usar a imagem base oficial do Python
FROM python:3.10-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o diretório de trabalho
COPY chatbot_llm_openai.py .

# Comando para executar o Streamlit quando o contêiner iniciar
CMD ["streamlit", "run", "chatbot_llm_openai.py", "--server.port=8080", "--server.address=0.0.0.0"]
