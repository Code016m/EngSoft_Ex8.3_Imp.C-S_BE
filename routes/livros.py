from flask import Blueprint, request, jsonify

livros_bp = Blueprint("livros", __name__)

livros = []

@livros_bp.route("/", methods=["GET"])
def listar():
    return jsonify(livros), 200

@livros_bp.route("/", methods=["POST"])
def adicionar():
    data = request.get_json()

    if not data:
        return jsonify({"erro": "JSON inválido"}), 400

    titulo = data.get("titulo")
    autor = data.get("autor")
    preco = data.get("preco")

    if not titulo or not autor or preco is None:
        return jsonify({"erro": "Campos obrigatórios: titulo, autor, preco"}), 400

    try:
        preco = float(preco)
    except ValueError:
        return jsonify({"erro": "Preço deve ser numérico"}), 400

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "preco": preco
    }

    livros.append(novo_livro)

    print("Livro adicionado:", novo_livro)

    return jsonify({
        "msg": "Livro adicionado com sucesso",
        "livro": novo_livro
    }), 201
