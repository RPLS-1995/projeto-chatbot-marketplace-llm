# Projeto de Chatbot para Marketplace com uso de LLMs

Este projeto visa desenvolver um Chatbot que simule um vendedor que
interage com um cliente e negocia a venda de eletrônicos disponíveis no Marketplace.
Para isso, deve ser usada uma LLM capaz de capturar informações do cliente e gerar uma proposta
comercial baseada nas suas requisições.


## Escolha da LLM ##
Após algumas pesquisas, optou-se inicialmente por uma LLM Open-Source por 2 motivos: O fato de ser gratuita e
a constante atualização e manutenção do modelo. Após checar as opções disponíveis no HuggingFace, a escolhida foi
a gp2-small-portuguese (https://huggingface.co/pierreguillou/gpt2-small-portuguese). A principal motivação foi
o treinamento ter sido realizado com palavras e textos no português do Brasil, o que poderia aumentar a capacidade
de responder mensagens em um chatbot.
No entanto, as expectativas não se concretizaram e a LLM começou a dar respostas muito diferentes do esperado,
em vários momentos sequer conseguindo recomendar algum eletrônico do Marketplace.

A segunda escolha, portanto, foi por uma LLM bastante consolidada no mercado. Dessa forma, a escolhida foi a **gpt-3.5-turbo**.
Várias foram as razões para a decisão:
- Uma experiência anterior com o ChatGPT, que indicou sua grande capacidade de interação
perguntas/respostas.
- O preço muito inferior em relação a outras LLMs da OpenAI (https://platform.openai.com/docs/models)
- O número inferior de tokens, o que exige uma quantidade menor de recursos computacionais para seu uso
e garante mais estabilidade em suas execuções.
- O fato dessa ser a LLM mais recomendada pela própria OpenAI para modelos de geração de texto. Segundo a empresa,
"If you’re not sure which model to use then try gpt-4o if you need high intelligence or gpt-3.5-turbo if you need the fastest speed and lowest cost."
(https://platform.openai.com/docs/guides/text-generation?lang=curl)
- A sua integração simples e intuitiva com o Streamlit, biblioteca Python voltada à implantação de uma página Web de forma rápida e prática.

Dessa vez os resultados foram muito superiores com a gpt-3.5-turbo e assim ela foi adotada para esse projeto.

## Como baixar e executar ##
### Com Docker (Linux) ###
Para este projeto os códigos foram implementados na linguagem Python (e revisados com flake8) e as execuções acontecem com o uso de Docker. O principal objetivo
do Docker é garantir que o Chatbot possa ser executado em qualquer máquina, independente de sua configuração.
Assim os passos para execução do Chatbot podem ser vistos abaixo:
1. Abra um terminal no computador e baixe o repositório usando o comando "git clone https://github.com/RPLS-1995/projeto-chatbot-marketplace-llm.git"
2. Abra uma IDE de sua preferência e entre na pasta do repositório clonado. Com o Docker instalado, execute o comando "sudo docker compose build".
Este comando fará que com as bibliotecas contidas no arquivo requirements.txt sejam instaladas na máquina.
3. Após o comando acima ser concluído, digite o comando "sudo docker compose up". Este comando irá criar e executa os contâiners necessários do projeto.
4. Quando essa mensagem aparecer no terminal, significa que o Chatbot está pronto para uso. ![image](https://github.com/RPLS-1995/projeto-chatbot-marketplace-llm/assets/174524067/b3f6f93b-84e7-4eb3-a252-ff85b763264e)
Assim, abra uma página no navegador de sua preferência com a URL http://0.0.0.0:8080 e aguarde o Chatbot ser totalmente carregado.
5. Caso o navegador exiba uma página Web similar a esta, significa que o Chatbot está pronto para uso! ![image](https://github.com/RPLS-1995/projeto-chatbot-marketplace-llm/assets/174524067/94b817a1-8120-42f6-8457-caed6700fbb0)

### Sem Docker (Linux e Windows) ###
1. Abra um terminal no computador e baixe o repositório usando o comando "git clone https://github.com/RPLS-1995/projeto-chatbot-marketplace-llm.git"
2. Abra uma IDE de sua preferência e entre na pasta do repositório clonado.
3. Execute na sequência os comandos abaixo:
   - python3 -m venv venv
   - source venv/bin/activate (para máquinas Linux) ou venv\Scripts\activate (para máquinas Windows)
   - pip3 install streamlit
   - pip3 install openai
   - pip3 install python-dotenv
   - streamlit run chatbot_llm_openai.py
4. Após executar o último comando, o terminal deve exibir essa mensagem: ![Captura de tela de 2024-07-04 11-23-02](https://github.com/RPLS-1995/projeto-chatbot-marketplace-llm/assets/174524067/ad6d9692-5196-476e-b113-a48195823af5)
   Assim, abra uma página no navegador de sua preferência com a URL http://localhost:8501 e aguarde o Chatbot ser totalmente carregado.

   
## Explorando o Chatbot ##
Conforme especificação, o Chatbot irá trabalhar como vendedor de um Marketplace de eletrônicos, em que há 8 diferentes produtos à venda. Para iniciar a interação com o Chatbot, o cliente deve digitar suas perguntas
e decisões no espaço mostrado abaixo e clicar no botão "Enviar".
![image](https://github.com/RPLS-1995/projeto-chatbot-marketplace-llm/assets/174524067/c2bd7c60-9747-4347-a773-7459cb1be54d)

Na sequência, o Chatbot irá capturar a mensagem e, baseando-se no seu conteúdo e num prompt de input com regras e condutas a serem adotadas, irá responder ao cliente. A resposta pode ser vista abaixo:
![image](https://github.com/RPLS-1995/projeto-chatbot-marketplace-llm/assets/174524067/6c5eaf06-046c-4a4a-a964-725af10142b1)

Após a resposta o cliente poderá digitar outra mensagem ao Chatbot, escolhendo um dos produtos e pedindo por mais detalhes ou adicionando-o ao carrinho. Essa interação de mensagens deve seguir até que o cliente
conclua uma compra ou saia do Chatbot, o que pode ser feito em qualquer momento clicando no botão "Sair". Quando esse comando é executado, a mensagem abaixo é exibida e todas as informações obtidas pelo
Chatbot na última conversa são perdidas.
![image](https://github.com/RPLS-1995/projeto-chatbot-marketplace-llm/assets/174524067/f2ae0d03-e106-4ebe-be4e-23f9419fe66b)

Os outros dois recursos estão disponíveis na barra lateral da aplicação Web. O primeiro é o botão que Reinicia o Chatbot, que deve ser usado caso o sistema não consiga mais responder adequadamente
às perguntas feitas pelo cliente. Ao clicar no botão, as conversas são deletadas e o Chatbot é reiniciado.
![image](https://github.com/RPLS-1995/projeto-chatbot-marketplace-llm/assets/174524067/367ef358-6d17-4bde-8945-f1ce052a3946)

Já o segundo é o botão que permite baixar a transcrição da última conversa feita com o Chatbot em um arquivo .csv. Assim basta clicar nele que um link para download é disponibilizado na tela.
![image](https://github.com/RPLS-1995/projeto-chatbot-marketplace-llm/assets/174524067/260d0872-61e4-4a69-8750-17e22b715210)

![image](https://github.com/RPLS-1995/projeto-chatbot-marketplace-llm/assets/174524067/e3c26e0c-16bc-4bbd-b4eb-97ca8c04661e)

![image](https://github.com/RPLS-1995/projeto-chatbot-marketplace-llm/assets/174524067/2e79b9a5-f9f6-408f-8bb3-27c0d8942896)

## Pontos de melhoria ##
Ao longo do desenvolvimento foram identificados vários pontos de melhoria, que foram implementados no sistema e que podem ser apeerfeiçoados. Dentre eles, temos:
- A escolha da LLM, que provou ser desafiador tanto na capacidade de gerar boas respostas ao cliente como no uso de recursos computacionais.
Como exemplo, uma delas exigia o uso de bibliotecas cujo import levava minutos para ser concluído.
- A dificuldade da LLM de entender sinônimos. Ao longo dos testes verificou-se que o modelo não conseguia relacionar as palavras "Notebook" e "Computador" com Laptop, o que fazia o Chatbot
não encontrar nenhum produto no catálogo. A solução foi acrescentar no prompt inicial sinônimos dos produtos disponíveis no Marketplace e exigir que a LLM fizesse a relação entre eles.
- A possibilidade de configurar mais parâmetros na LLM, que possam garantir respostas mais precisas ao cliente em um intervalo menor de tempo.
- A adição de arquivos executáveis (.exe), para que o Chatbot possa ser executado em diferentes Sistemas Operacionais sem a necessidade de seguir tutoriais de instalação.




