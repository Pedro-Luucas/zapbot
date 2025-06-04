from flask import Flask, request, jsonify
import hashlib
import hmac
import base64

app = Flask(__name__)

# Configurações (em produção, armazene estas chaves de forma segura)
API_KEY = "sua_api_key_aqui"
AUTH_TOKEN = "seu_auth_token_aqui"

def verify_signature(api_key, auth_token, payload, received_signature):
    """
    Verifica a assinatura da requisição
    """
    # Concatena os parâmetros
    message = f"{api_key}{auth_token}{payload}"
    
    # Calcula o HMAC-SHA256
    signature = hmac.new(
        auth_token.encode('utf-8'),
        message.encode('utf-8'),
        hashlib.sha256
    ).digest()
    
    # Codifica em base64
    expected_signature = base64.b64encode(signature).decode('utf-8')
    
    # Compara com a assinatura recebida
    return hmac.compare_digest(expected_signature, received_signature)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    try:
        # Obter cabeçalhos de autenticação
        api_key = request.headers.get('X-API-Key')
        auth_token = request.headers.get('X-Auth-Token')
        signature = request.headers.get('X-Signature')
        
        # Verificar se os cabeçalhos necessários estão presentes
        if not all([api_key, auth_token, signature]):
            return jsonify({"error": "Missing authentication headers"}), 401
        
        # Verificar credenciais
        if api_key != API_KEY or auth_token != AUTH_TOKEN:
            return jsonify({"error": "Invalid credentials"}), 403
        
        # Obter o corpo da requisição como string para verificação de assinatura
        payload = request.get_data(as_text=True)
        
        # Verificar a assinatura
        if not verify_signature(api_key, auth_token, payload, signature):
            return jsonify({"error": "Invalid signature"}), 403
        
        # Se chegou aqui, a autenticação foi bem-sucedida
        data = request.json
        
        # Processar os dados recebidos
        # Exemplo: verificar o tipo de evento
        event_type = data.get('event')
        
        if event_type == 'message':
            # Processar mensagem recebida
            message = data.get('message')
            print(f"Mensagem recebida: {message}")
            return jsonify({"status": "message processed"}), 200
        else:
            return jsonify({"status": "event not handled"}), 200
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)