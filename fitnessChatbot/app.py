import random

import gradio as gr
import pandas as pd
import torch
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from transformers import BertForQuestionAnswering, BertTokenizerFast

# Carregar o modelo e o tokenizer
tokenizer = BertTokenizerFast.from_pretrained('bert-base-multilingual-cased')
model = BertForQuestionAnswering.from_pretrained('./saved_model')

qa_dataset_path = './data/qa_dataset.csv'
qa_data = pd.read_csv(qa_dataset_path)

# Criar o TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
vectorizer.fit(qa_data['question'].tolist())

def load_examples(file_path):
    """Carregar exemplos de perguntas do cvs ('./data/qa_dataset.csv')"""
    data = pd.read_csv(file_path)
    return data['question'].tolist()

def find_relevant_context(question):
    """Encontrar o contexto mais relevante"""
    query_vec = vectorizer.transform([question])
    qa_vec = vectorizer.transform(qa_data['question'].tolist())
    similarity = cosine_similarity(query_vec, qa_vec).flatten()
    most_similar_idx = similarity.argmax()
    return qa_data.iloc[most_similar_idx]['answer']

def predict_answer(question):
    """Prever resposta dependendo do contexto"""
    relevant_context = find_relevant_context(question)
    print(f"Contexto relevante encontrado: {relevant_context}")

    inputs = tokenizer(question, relevant_context, return_tensors='pt', truncation=True, max_length=512, padding=True, return_offsets_mapping=True)
    offset_mapping = inputs.pop("offset_mapping")

    with torch.no_grad():
        outputs = model(**inputs)

    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits) + 1

    print(f"Start index: {answer_start}, End index: {answer_end}")

    # Logica para que indices estao dentro dos limites e propriamente ordenados
    if answer_start >= len(offset_mapping[0]):
        answer_start = len(offset_mapping[0]) - 1
    if answer_end > len(offset_mapping[0]):
        answer_end = len(offset_mapping[0])
    if answer_start > answer_end:
        answer_start, answer_end = answer_end, answer_start

    print(f"Start adjusted index: {answer_start}, Adjusted End index: {answer_end}")

    # Converter indices de tokens
    start_char = offset_mapping[0][answer_start][0]
    end_char = offset_mapping[0][answer_end - 1][1]

    print(f"Start char: {start_char}, End char: {end_char}")

    answer = relevant_context[start_char:end_char].strip()

    return answer if answer else "Desculpe, não consegui encontrar uma resposta adequada."

def get_random_examples(file_path, num_examples=3):
    """ Dar exemplos de perguntas para o usuario"""
    examples = load_examples(file_path)
    random_examples = random.sample(examples, num_examples)
    return random_examples

def create_interface(file_path):
    """Interface com Gradio"""
    examples = get_random_examples(file_path)
    iface = gr.Interface(
        fn=predict_answer,
        inputs=gr.Textbox(lines=2, placeholder="Digite sua pergunta aqui..."), 
        outputs="text",
        title="Chatbot Fitness",
        description="Faça uma pergunta sobre exercícios e obtenha uma resposta!",
        examples=[[example] for example in examples]
    )
    return iface

# Launch interface
if __name__ == "__main__":
    file_path = './data/qa_dataset.csv'
    iface = create_interface(file_path)
    iface.launch()
