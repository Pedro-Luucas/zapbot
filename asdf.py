from utils.evolutionAPI import evoAPI
import dotenv
import os
import cowsay

# Carrega variáveis do .env
dotenv.load_dotenv()

# Instância e API key
INSTANCE_ID = "zapbotinstancia"
API_KEY = os.getenv("API_KEY")

# Número de destino e mensagem
NUMERO_DESTINO = "NUMERO" # formato com DDI+DDD+NÚMERO
MENSAGEM = cowsay.get_output_string("trex", "auauauuauuuu auuau auuu auuu")

# Inicializa API
api = evoAPI()

# Envia mensagem
resposta = api.enviar_mensagem(INSTANCE_ID, API_KEY, NUMERO_DESTINO, MENSAGEM)

# Mostra resposta
print("Status Code:", resposta.status_code)
print("Resposta da API:", resposta.text)
