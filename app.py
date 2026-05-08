from flask import Flask, redirect
from flask_cors import CORS

from routes.livros import livros_bp

app = Flask(__name__)

CORS(app)

app.register_blueprint(
    livros_bp,
    url_prefix="/livros"
)

@app.route("/")
def home():
    return redirect("/livros/")

if __name__ == "__main__":
    app.run(debug=True)