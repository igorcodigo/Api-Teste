from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Habilita CORS para todas as rotas

# Lista de tokens válidos
valid_tokens = ["4422313123", "123213551"]
debit_tokens = ["88412246", "991230241"]
person_tokens = ["igor","trincado","gabriel","cesar","bolacha"]

@app.route('/get_status', methods=['GET'])
def get_status():
    # Obter o token da solicitação
    token = request.args.get('token')

    # Verificar se o token é válido
    if token in valid_tokens:
        # Seu código existente aqui
        # Por exemplo: retornar o status de uma variável booleana
        status = True
        return jsonify({"status": status})
    elif token in debit_tokens:
        status = "Debito Pendente"
        return jsonify({"status": status})
    elif token in person_tokens:
        status = "Pessoa presente"
        return jsonify({"Frequencia": status})
    else:
        return jsonify({"error": "Token invalido ou pessoa ausente na lista"}), 401

if __name__ == '__main__':
    app.run(debug=True)
