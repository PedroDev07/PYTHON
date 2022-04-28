from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    nome = request.form.get("nome")
    empresa = request.form.get("empresa")
    return render_template("index.html"), nome, empresa


@app.route("/homepage/<nome>")
def homepage(nome):
    return render_template("homepage.html")


@app.route("/historia")
def historia():
    return render_template("historia.html")


@app.route("/contato")
def contato():
    return render_template("contato.html")




#coloca o site no ar
if __name__ == "__main__":
    app.run(debug=True)
