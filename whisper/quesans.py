from pydoc import text
from unittest import result
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

nlp = pipeline('question-answering',model='deepset/roberta-base-squad2',tokenizer='deepset/roberta-base-squad2')

ques = input("Ask me anything ?")

ques_dict  = {
    'question':ques,
    'context':text
}

results = nlp(ques_dict)
print("Ans -> ",results['answer'])