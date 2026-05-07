class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "preco": self.preco
        }
