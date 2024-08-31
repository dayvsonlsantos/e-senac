from flask import Flask, render_template, request, jsonify
import requests
import json
from dotenv import load_dotenv
import os

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter a chave da API do .env
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        question = request.form["question"]

        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

        data = {
            "model": "gpt-4",
            "messages": [
                {"role": "system", "content": "Você é um professor experiente em diversas áreas do conhecimento."},
                {"role": "user", "content": question}
            ],
            "temperature": 0.8,
            "max_tokens": 1000,
            "n": 1
        }

        response = requests.post(url, headers=headers, json=data)

        if response.status_code == 200:
            message_content = response.json()['choices'][0]['message']['content']
        else:
            message_content = "Erro ao se comunicar com a API. Tente novamente."

        return jsonify({"response": message_content})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
