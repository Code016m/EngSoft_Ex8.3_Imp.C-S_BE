from flask import Blueprint, request, jsonify
from models.livro import Livro

livros_bp = Blueprint("livros", __name__)

# banco em memória
livros = []


# GET /livros
@livros_bp.route("/", methods=["GET"])
def listar_livros():

    return jsonify(
        [livro.to_dict() for livro in livros]
    ), 200


# POST /livros
@livros_bp.route("/", methods=["POST"])
def adicionar_livro():

    data = request.get_json()

    if not data:
        return jsonify({
            "erro": "JSON inválido"
        }), 400

    titulo = data.get("titulo")
    autor = data.get("autor")
    preco = data.get("preco")

    if not titulo or not autor or preco is None:
        return jsonify({
            "erro": "Campos obrigatórios"
        }), 400

    try:
        preco = float(preco)

    except ValueError:
        return jsonify({
            "erro": "Preço inválido"
        }), 400

    novo_livro = Livro(
        titulo,
        autor,
        preco
    )

    livros.append(novo_livro)

    return jsonify({
        "msg": "Livro cadastrado",
        "livro": novo_livro.to_dict()
    }), 201