import os
from flask import Flask
from flask_cors import CORS

from routes.livros import livros_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(livros_bp, url_prefix="/livros")

@app.route("/")
def home():
    return {
        "status": "API rodando com sucesso",
        "service": "livraria"
    }

@app.route("/test")
def test():
    return {
        "message": "Teste OK",
        "status": 200
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)