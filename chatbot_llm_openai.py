import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
import prompts
import styles
import csv
import base64

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


# Prompt inicial que define o comportamento do bot
initial_prompt = prompts.SALE_RULES_PROMPT


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.getenv("OPENAI_API_KEY"),
)


# Função para chamar a API da OpenAI
def get_response_from_openai(messages):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    message = response.choices[0].message.content.strip()
    return message


# Configurar a interface do Streamlit
st.set_page_config(page_title="Chatbot, o seu vendedor de Eletrônicos do Marketplace", page_icon="🤖")
st.title("🤖 Chatbot Vendedor de Eletrônicos")

# Injetar CSS para personalização
st.markdown(styles.CSS_STYLES, unsafe_allow_html=True)

# Histórico da conversa
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": initial_prompt}]

# Layout da página
st.sidebar.header("Opções")
if st.sidebar.button("Reiniciar Chatbot"):
    st.session_state.messages = [{"role": "system", "content": initial_prompt}]
    st.rerun()

# Botão para fazer download das mensagens
if st.sidebar.button("Baixar Mensagens"):
    # Definir nome do arquivo de saída
    file_name = "mensagens.csv"

    # Salvar as mensagens em um arquivo CSV
    with open(file_name, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Role", "Content"])  # Cabeçalho do CSV
        for message in st.session_state.messages:
            if message != st.session_state.messages[0]:
                writer.writerow([message["role"], message["content"]])

    # Gerar link para download do arquivo CSV
    with open(file_name, "rb") as f:
        csv_bytes = f.read()
        b64 = base64.b64encode(csv_bytes).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{file_name}">Clique aqui para baixar</a>'
        st.markdown(href, unsafe_allow_html=True)        

    # Mensagem de sucesso e link para download
    st.success("Mensagens exportadas com sucesso!")

# Input do usuário
user_input = st.text_input("Digite aqui...", key="user_input")

# Botão para enviar a mensagem
if st.button("Enviar"):
    if user_input:
        # Adiciona a entrada do usuário ao histórico
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Obtém a resposta da LLM
        response = get_response_from_openai(st.session_state.messages)

        # Adiciona a resposta ao histórico
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Exibe o histórico atualizado
        for message in st.session_state.messages:
            if message['role'] != 'system':
                st.write(f"{message['role'].capitalize()}: {message['content']}")

# Botão para sair
if st.button("Sair"):
    st.write("Vendedor (Bot): Até mais! Volte sempre!")
    st.session_state.messages = [{"role": "system", "content": initial_prompt}]
    st.stop()
