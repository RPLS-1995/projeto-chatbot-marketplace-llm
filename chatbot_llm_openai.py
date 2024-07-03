import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
import prompts

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()


# Prompt inicial que define o comportamento do bot
initial_prompt = prompts.SALE_RULES_PROMPT


client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
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

# Histórico da conversa
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": initial_prompt}]

# Layout da página
st.sidebar.header("Opções")
if st.sidebar.button("Limpar Conversa"):
    st.session_state.messages = [{"role": "system", "content": initial_prompt}]
    st.rerun()

# Input do usuário
user_input = st.text_input("Você:", key="user_input")

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
