# Fitness_Chatbot

Chatbot Fitness
Este é um chatbot desenvolvido para responder perguntas relacionadas a exercícios físicos utilizando o modelo BERT para question answering.

Índice
Visão Geral
Funcionalidades
Requisitos
Instalação
Uso
Estrutura do Projeto
Contribuições
Licença
Visão Geral
Este projeto implementa um chatbot que responde a perguntas sobre exercícios físicos. Utilizando um dataset de perguntas e respostas sobre exercícios, o chatbot é capaz de fornecer informações detalhadas sobre como realizar os exercícios, os músculos envolvidos e alternativas de exercícios.

Funcionalidades
Responder perguntas sobre como realizar um exercício específico.
Informar quais músculos são trabalhados por um determinado exercício.
Sugerir alternativas para um exercício específico.
Requisitos
Python 3.7 ou superior
Bibliotecas Python listadas no arquivo requirements.txt
Instalação
Clone este repositório:

bash
Copiar código
git clone https://github.com/seu-usuario/chatbot-fitness.git
cd chatbot-fitness
Crie um ambiente virtual:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Para Windows, use `venv\Scripts\activate`
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Baixe e prepare o dataset:

Coloque seu arquivo ExercisesDataset.xlsx na pasta data.

Execute o script de processamento de dados para gerar o dataset de perguntas e respostas:

bash
Copiar código
python data_processing.py
Treine o modelo:

bash
Copiar código
python training.py
Uso
Inicie a aplicação:

bash
Copiar código
python app.py
Acesse a interface do Gradio que será aberta no navegador.

Digite sua pergunta no campo de texto e clique em "Submit" para obter uma resposta.

Estrutura do Projeto
app.py: Arquivo principal que inicia a interface do Gradio.
data_processing.py: Script para processar e criar o dataset de perguntas e respostas.
training.py: Script para treinar o modelo BERT.
data/: Pasta que contém o dataset de exercícios.
saved_model/: Pasta onde o modelo treinado é salvo.
requirements.txt: Lista de dependências do projeto.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

