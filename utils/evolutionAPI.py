import requests

class evoAPI:
  def __init__(self):
    pass
  
  def enviar_mensagem(self, instance, apikey, senderNumber, msg):
    url = f'http://localhost:8080/message/sendText/{instance}'
    payload = {
    "number": f"{senderNumber}",
    "options": {
        "delay": 737,
            },
        "text": f"{msg}"
        }
    
    headers = {
    "apikey": f"{apikey}",
    "Content-Type": "application/json"
        }
    
    response = requests.request("POST", url, json=payload, headers=headers)
    return response