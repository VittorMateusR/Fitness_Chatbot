# Chatbot Fitness

Este é um chatbot desenvolvido para responder perguntas relacionadas a exercícios físicos utilizando o modelo BERT para question answering.

## Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuições](#contribuições)
- [Licença](#licença)

## Visão Geral

Este projeto implementa um chatbot que responde a perguntas sobre exercícios físicos. Utilizando um dataset de perguntas e respostas sobre exercícios, o chatbot é capaz de fornecer informações detalhadas sobre como realizar os exercícios, os músculos envolvidos e alternativas de exercícios.

## Funcionalidades

- Responder perguntas sobre como realizar um exercício específico.
- Informar quais músculos são trabalhados por um determinado exercício.
- Sugerir alternativas para um exercício específico.

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python listadas no arquivo `requirements.txt`

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/chatbot-fitness.git
    cd chatbot-fitness
    ```

2. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # Para Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Baixe e prepare o dataset:

    - Coloque seu arquivo `ExercisesDataset.xlsx` na pasta `data`.
    - Execute o script de processamento de dados para gerar o dataset de perguntas e respostas:

        ```bash
        python data_processing.py
        ```

5. Treine o modelo:

    ```bash
    python training.py
    ```

## Uso

1. Inicie a aplicação:

    ```bash
    python app.py
    ```

2. Acesse a interface do Gradio que será aberta no navegador.

3. Digite sua pergunta no campo de texto e clique em "Submit" para obter uma resposta.

## Estrutura do Projeto

- `app.py`: Arquivo principal que inicia a interface do Gradio.
- `data_processing.py`: Script para processar e criar o dataset de perguntas e respostas.
- `training.py`: Script para treinar o modelo BERT.
- `data/`: Pasta que contém o dataset de exercícios.
- `saved_model/`: Pasta onde o modelo treinado é salvo.
- `requirements.txt`: Lista de dependências do projeto.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo `LICENSE` para mais detalhes.
