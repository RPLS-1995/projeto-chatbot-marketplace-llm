CSS_STYLES = """
    <style>
    /* Fonte e tamanho da fonte */
    body, .stTextInput, .stButton, .stMarkdown, .stTitle {
        font-family: 'Arial', sans-serif;
    }

    /* Cor de fundo da página */
    .main {
        background-color: #f9f9f9; /* Cor de fundo mais suave */
    }

    /* Cor de fundo dos elementos de entrada */
    .stTextInput, .stButton, .stMarkdown, .stTitle {
        color: #333333;
    }

    /* Estilizando os botões com sombra */
    .stButton button {
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
        margin-top: 10px;
    }

    /* Estilizando a entrada de texto */
    .stTextInput input {
        font-size: 20px; /* Texto maior na entrada de texto */
        width: 100%; /* Largura maior na entrada de texto */
        padding: 15px; /* Espaçamento interno para melhor usabilidade */
        box-sizing: border-box;
    }

    /* Estilizando o título */
    .stTitle h1 {
        font-size: 36px; /* Aumentar o tamanho do texto do título */
        width: 100%; /* Ocupar uma largura maior na página */
        text-align: center; /* Centralizar o título */
    }

    /* Estilizando as mensagens */
    .user-message, .assistant-message, .st.session_state.messages {
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 5px;
    }

    </style>
    """
