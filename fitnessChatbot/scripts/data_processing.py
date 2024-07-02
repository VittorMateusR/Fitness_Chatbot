import pandas as pd
from sklearn.model_selection import train_test_split
from transformers import BertTokenizer


def load_data(file_path):
    """Carregar dados do Dataset( excel )"""
    data = pd.read_excel(file_path)
    return data

def create_qa_pairs(data):
    """Criar os pares de pergunta e respostas"""
    qa_pairs = []

    # Template para as perguntas
    question_templates = [
        "Como faço para executar um(a) {}?",
        "Como faço para fazer um(a) {}?",
        "Você pode explicar como fazer um(a) {}?",
        "Qual é a forma correta para {}?",
        "Quais músculos o(a) {} trabalha?",
        "Quais músculos são trabalhados por um(a) {}?",
        "Quais são algumas alternativas para {}?",
        "Alternativas para {}",
        "Alternativas para substituir {}"
    ]

    for index, row in data.iterrows():
        exercise = row['Exercício']
        main_muscle_group = row['Grupo Muscular Principal']
        secondary_muscle_groups = row['Grupos Musculares Secundários']
        how_to = row['Como Fazer']
        level = row['Nível']
        equipment = row['Equipamento']
        alternative_exercises = row['Exercícios Alternativos']

        answers = {
            "Como": f"{how_to}. Este exercício é considerado de nível {level}, e requer {equipment}",
            "Musculos": f"Músculo principal: {main_muscle_group}, músculos secundários: {secondary_muscle_groups}.",
            "Alternativas": f"Três alternativas para {exercise} são {alternative_exercises}."
        }

        # Logica para criar as perguntas e respostas
        for template in question_templates:
            question = template.format(exercise)
            if "Como" in question or "forma" in question:
                answer = answers["Como"]
            elif "músculos" in question or "Músculos" in question:
                answer = answers["Musculos"]
            else:
                answer = answers["Alternativas"]

            qa_pairs.append((question, answer))

    qa_data = pd.DataFrame(qa_pairs, columns=['question', 'answer'])
    return qa_data

def preprocess_data(data, tokenizer):
    """Tokenize e processar as perguntas e respostas."""
    tokenized_inputs = tokenizer(data['question'].tolist(), padding=True, truncation=True, max_length=512, return_tensors='pt')
    tokenized_labels = tokenizer(data['answer'].tolist(), padding=True, truncation=True, max_length=512, return_tensors='pt')

    # Preparar o dataset para treinamento
    dataset = []
    for i in range(len(tokenized_inputs['input_ids'])):
        inputs = {
            'input_ids': tokenized_inputs['input_ids'][i],
            'attention_mask': tokenized_inputs['attention_mask'][i],
            'start_positions': tokenized_labels['input_ids'][i].tolist().index(tokenizer.cls_token_id),
            'end_positions': tokenized_labels['input_ids'][i].tolist().index(tokenizer.sep_token_id) - 1,
        }
        dataset.append(inputs)
    return dataset

def split_data(qa_data):
    """Logica para dividir o dataset em treino e evalucao"""
    qa_data = qa_data.sample(frac=1).reset_index(drop=True)
    train_data, eval_data = train_test_split(qa_data, test_size=0.2, random_state=43)
    return train_data, eval_data


#Main
if __name__ == "__main__":
    file_path = '../data/ExercisesDataset.xlsx'
    data = load_data(file_path)
    print(data.head())

    # Criar o .csv com as perguntas e respostas
    qa_data = create_qa_pairs(data)
    qa_data.to_csv('../data/qa_dataset.csv', index=False)
    print("QA dataset created and saved as 'qa_dataset.csv'")

    tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-cased')
    dataset = preprocess_data(qa_data, tokenizer)

    # Criar os arquivos de training and evaluation
    train_data, eval_data = split_data(qa_data)
    print(f"Tamanho dos dados de treino: {len(train_data)}, Tamanho dos dados de avaliação: {len(eval_data)}")
