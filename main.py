import requests
import json
from .key import API_KEY


HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

link_models = "https://api.openai.com/v1/models"

req = requests

# Pegando todos os medelos disponiveis pelo openAI
model_list = req.get(link_models, headers=HEADERS)

# Modelo disponivel selecionado
model_id = 'gpt-3.5-turbo'

# api de post do modelo
links_post = 'https://api.openai.com/v1/chat/completions'

print("Olá sou jarvis") 

# Loop infinito para execução do Programa
while True:
    
    user_input = str(input("User: "))

    # conteudo do requisição post
    body_message = {
        "model": model_id,
        "messages": [{"role":"user", "content": user_input}]
    }

    print(".......")
    print("Calculando")
    print('........')

    # modelo da requisição para json
    data = json.dumps(body_message)

    # Resposta da requisição em formato json
    res = req.post(links_post, headers=HEADERS, data=data)

    # Resposta da requisição converttido para dict
    response = res.json()
    ai_response = response["choices"][0]["message"]["content"]

    print("AI: " + ai_response)

