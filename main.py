from flask import Flask, request, jsonify
from utils.evolutionAPI import evoAPI
import dotenv, os

a = dotenv.load_dotenv()

app = Flask(__name__)
api = evoAPI()

# Configuração da API
INSTANCE_ID = "zapbotinstancia"
API_KEY = os.getenv("API_KEY")

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Webhook recebido:", data)

    try:
        numero = data["message"]["from"]
        texto = data["message"]["body"]["text"]

        print(f"Recebido de {numero}: {texto}")

        resposta = api.enviar_mensagem(INSTANCE_ID, API_KEY, "numero", " mesnage ")

        return jsonify({
            "status": "mensagem enviada",
            "numero": numero,
            "texto": texto,
            "resposta_api": resposta.json()
        })

    except Exception as e:
        print("Erro:", str(e))
        return jsonify({"erro": str(e)}), 500


if __name__ == "__main__":
    app.run(port=5000)     # ← Inicia o servidor Flask


