from flask import Blueprint, request, jsonify

livros_bp = Blueprint("livros", __name__)

livros = []

@livros_bp.route("/", methods=["GET"])
def listar_livros():
    return jsonify(livros)

@livros_bp.route("/", methods=["POST"])
def adicionar_livro():
    dados = request.json

    novo_livro = {
        "titulo": dados["titulo"],
        "autor": dados["autor"],
        "preco": dados["preco"]
    }

    livros.append(novo_livro)

    return jsonify({
        "msg": "Livro adicionado com sucesso",
        "livro": novo_livro
    }), 201