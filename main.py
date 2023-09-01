from flask import *
import classes
from date import datetime

app = Flask(__name__)

carta = []
newl = len(carta)
data_atual = date.today()

@app.route("/login", methods=['GET', 'POST'])
def login():
    if method == ["POST"]:
        user = request.form.get("nome")
        global username; username = user
        passw = request.form.get("password")

        with open('users.txt', 'r') as arquivo:
            linhas = arquivo.readlines()
            arquivo.seek(0)

            for i in linhas:
                if linha == f"{user}: {passw}":
                    return redirect("carta/<username>")

                else:
                    return redirect("/login")
            

        return render_template("login.html")

@app.route("/carta/<username>", methods=['GET', 'POST'])
def pagina_carta(username):
    if method == ["POST"]:
        
        data = data_atual.strftime("%d/%m/%Y, %H:%M:%S")
        mensagem = request.form.get("mensagem")
        destinatario = request.form.get("destinatario")
        #remetente = request.form.get("remetente")
        gerar_carta = rquest.form.get("gerar")

        if gerar_carta:                 #Não sei qual condição coloca
            carta[newl] = Carta(number_of_letter, data, destinatario, mensagem, user)
            carta[newl].write()
        
        return render_template("carta.html")

if __name__ == "__main__":
    app.run(debug=True)
