from flask import *
import classes
from datetime import date

app = Flask(__name__)

carta = []
newl = len(carta)
data_atual = date.today()

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        user = request.form.get("nome")
        global username
        username = user
        passw = request.form.get("password")

        with open('users.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

            for linha in linhas:
                if linha.strip() == f"{user}: {passw}":
                    return redirect(f"/carta/{username}")

        return redirect("/login")

    return render_template("login.html")

@app.route("/carta/<username>", methods=['GET', 'POST'])
def pagina_carta(username):
    if request.method == "POST":
        
        data = data_atual.strftime("%d/%m/%Y, %H:%M:%S")
        mensagem = request.form.get("mensagem")
        destinatario = request.form.get("destinatario")
        #remetente = request.form.get("remetente")
        gerar_carta = request.form.get("gerar")

        if gerar_carta:                 #Não sei qual condição coloca
            carta.append(Carta(newl, data, destinatario, mensagem, username))
            carta[newl].write()
        
        return render_template("carta.html")

if __name__ == "__main__":
    app.run(debug=True)
