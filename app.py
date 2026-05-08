from flask import Flask
from flask_cors import CORS

from routes.livros import livros_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(
    livros_bp,
    url_prefix="/livros"
)

@app.route('/')
def index():
    return jsonify({"msg": "Bem-vindo à API de livros!"})

if __name__ == "__main__":
    app.run(debug=True)