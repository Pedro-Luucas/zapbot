import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from utils.evolutionAPI import EvolutionAPI

load_dotenv()

API_KEY = os.getenv("API_KEY2")
INSTANCE_ID = os.getenv("INSTANCE_ID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

app = Flask(__name__)
evo_api = EvolutionAPI()

@app.route("/webhook", methods=["POST"])
def webhook():
    dados = request.json
    token = dados.get("apikey")  # O token vem como "apikey" no JSON, não como parâmetro de query

    event = dados.get("event")
    print("📨 Evento recebido:\n", event, "\n\n\n", dados, "\n\n\n", token, "\n \n \n")
    
    evo_api.enviar_mensagem("TESTE DO ZAP", INSTANCE_ID , API_KEY, "554891272434")

    return jsonify({"status": "mensagem processada"}), 200

if __name__ == "__main__":
    app.run(port=5000, debug=True)


