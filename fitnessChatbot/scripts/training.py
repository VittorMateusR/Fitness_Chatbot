from pathlib import Path

import torch
from data_processing import (create_qa_pairs, load_data, preprocess_data,
                             split_data)
from transformers import (BertForQuestionAnswering, BertTokenizerFast, Trainer,
                          TrainingArguments)


def train():
    # Carregar o dataset principal
    file_path = '../data/ExercisesDataset.xlsx'
    data = load_data(file_path)
    qa_data = create_qa_pairs(data)
    
    # Dividir os dados para treino e avaliacao de performance
    train_data, eval_data = split_data(qa_data)
    train_data.to_csv('../data/train_dataset.csv', index=False)
    eval_data.to_csv('../data/eval_dataset.csv', index=False)
    
    # Inicializar o tokenizer e o modelo pre treinado
    model_name = 'bert-base-multilingual-cased'
    tokenizer = BertTokenizerFast.from_pretrained(model_name)
    model = BertForQuestionAnswering.from_pretrained(model_name)
    
    # Pre-processar os dados de treinamento e avaliacao
    train_dataset = preprocess_data(train_data, tokenizer)
    eval_dataset = preprocess_data(eval_data, tokenizer)
    
    #Configurar diretorio de logs
    logging_dir = Path("./logs")
    if logging_dir.exists() and not logging_dir.is_dir():
        logging_dir.unlink()
        logging_dir.mkdir(parents=True, exist_ok=True)
    
    # Definir parametros para treinamento
    training_args = TrainingArguments(
        output_dir='./results',
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir=str(logging_dir),
        logging_steps=10,
    )
    
    # Inicializar treinamento
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
    )
    
    # Treinar e salvar o modelo
    trainer.train()
    
    model.save_pretrained('./saved_model')
    tokenizer.save_pretrained('./saved_model')

if __name__ == "__main__":
    train()
