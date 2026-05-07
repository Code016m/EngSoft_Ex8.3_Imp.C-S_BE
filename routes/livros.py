from flask import Blueprint, request, jsonify
from models.livro import Livro

livros_bp = Blueprint("livros", __name__)

livros = []


# GET - listar livros
@livros_bp.route("/", methods=["GET"])
def listar():
    return jsonify([livro.to_dict() for livro in livros]), 200


# POST - adicionar livro
@livros_bp.route("/", methods=["POST"])
def adicionar():

    data = request.get_json()

    if not data:
        return jsonify({"erro": "JSON inválido"}), 400

    titulo = data.get("titulo")
    autor = data.get("autor")
    preco = data.get("preco")

    if not titulo or not autor or preco is None:
        return jsonify({
            "erro": "Campos obrigatórios: titulo, autor, preco"
        }), 400

    try:
        preco = float(preco)

    except ValueError:
        return jsonify({
            "erro": "Preço deve ser numérico"
        }), 400

    # cria objeto Livro
    novo_livro = Livro(titulo, autor, preco)

    # salva objeto na lista
    livros.append(novo_livro)

    print("Livro adicionado:", novo_livro.to_dict())

    return jsonify({
        "msg": "Livro adicionado com sucesso",
        "livro": novo_livro.to_dict()
    }), 201
