import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Carregar o modelo e o tokenizer do GPT-2 em português
model_name = "pierreguillou/gpt2-small-portuguese"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Criar a pipeline de geração de texto
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Título da aplicação Streamlit
st.title("Chatbot em Português")

# Caixa de texto para entrada do usuário
user_input = st.text_input("Você: ")

# Gerar resposta do chatbot quando o usuário fornece uma entrada
if user_input:
    response = chatbot(user_input, max_length=500, num_return_sequences=1)
    chatbot_response = response[0]['generated_text']
    st.text_area("Chatbot:", value=chatbot_response, height=200)

# Manter a conversa no histórico
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = ""
