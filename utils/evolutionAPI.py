import requests

class EvolutionAPI():
    def __init__(self):
        pass

    def enviar_mensagem(self, message, instance, api_key, sender_number):
        url = f"http://localhost:8080/webhook/message/sendText/{instance}"
        payload = {
            "number": sender_number,
            "text": message,
            "delay": 123
            }
        
        headers = {
            "apikey": api_key,
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers)
        print(response)
        return response
