from flask import *
from classes import Carta

app = Flask(__name__)

carta = []
number_of_letter = len(carta)

@app.route("/login")
def login():
    if method == ["POST"]:
        global user; user = request.form.get("nome")
        passw = request.form.get("password")
        return render_template("login.html")

@app.route("/carta")
def pagina_carta():
    if method == ["POST"]:
        data = 
        mensagem = request.form.get("mensagem")
        destinatario = request.form.get("destinatario")
        remetente = request.form.get("remetente")
        carta[number_of_letter] = Carta(number_of_letter, data, destinatario, mensagem, user)
        carta[number_of_letter].write()
        number_of_letter = len(carta)
        return render_template("carta.html")

if __name__ == "__main__":
    app.run()
