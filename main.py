from flask import Flask, render_template, request, redirect
from classes import *
from datetime import datetime
import pandas as pd

app = Flask(__name__)

usuario = User
cartas = []
data_atual = datetime.now()

credentials_dict = {}

@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None

    with open('users/users.txt', 'r') as arquivo:
        for linha in arquivo:
            user, passw = linha.strip().split(": ")
            credentials_dict[user] = passw

    if request.method == "POST":
        user = request.form.get("name")
        passw = request.form.get("password")

        if user in credentials_dict and credentials_dict[user] == passw:
            return redirect(f"/carta/{user}")
        else:
            error = "Credenciais inválidas. Tente novamente."

    return render_template("login.html", error=error)


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    if request.method == "POST":
        name = request.form.get("name_c")
        passw = request.form.get("passw_c")
        usuario.cadastrar(name, passw)
        
        return redirect("/login")

    return render_template("cadastro.html")

@app.route("/carta/<user>", methods=['GET', 'POST'])
def pagina_carta(user):
    df = pd.read_csv(f"users/{user}_log.txt", delimiter=':', header=None, names=['Remetente', 'Mensagem'])
    tabela_html = df.to_html(classes='table table-striped', index=False)
    
    if request.method == "POST":
        data_atual = f"{datetime.now()}"
        mensagem = request.form.get("mensagem")
        destinatario = request.form.get("destinatario")

        if "gerar" in request.form:
            newl = len(cartas)
            carta = Carta(newl, data_atual, destinatario, mensagem, user)
            cartas.append(carta)
            carta.write()

    return render_template("carta.html", tabela_html=tabela_html)

if __name__ == "__main__":
    app.run(debug=True)
