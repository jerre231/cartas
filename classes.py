from fpdf import FPDF
import os

class Carta():
    def __init__(self, carta_id, data, destinatario, mensagem, remetente):
        self.id = carta_id
        self.dt = data
        self.dst = destinatario
        self.msg = mensagem
        self.rmt = remetente
        
        self.escrever = f"{self.dt}\n{self.dst}\n{self.msg}\n{self.rmt}"
        
        self.pdf = FPDF()
        self.pdf.add_page() 
        self.pdf.set_font("Arial", size = 12)


    def write(self):
        with open(f"banco_dt/carta_{self.id}.txt", 'w+') as arquivo:
            arquivo.write(self.escrever)

        self.pdf.cell(200, 10, txt = self.dt, ln = 1, align = 'C')
        self.pdf.cell(200, 10, txt = self.dst, ln = 2, align = 'C')
        self.pdf.cell(200, 10, txt = self.msg, ln = 3, align = 'C')
        self.pdf.cell(200, 10, txt = self.rmt, ln = 4, align = 'C')
        self.pdf.output(f"banco_dt/carta_{self.id}.pdf")

class User():
    def __init__(self, us, pw):
        self.username = us
        self.passw = pw

    def cadastrar(self):
        with open("users.txt", 'a') as arquivo:
            arquivo.write(f"{self.username}: {self.passw}")



#sim, essa função é fora do User. Não tocar, obrigado.                                 #TODO: implementar uma janela em "cartas.html" para poder ler a "mensagem"!
def encontrar_cartas(username):
    for arquivo in os.listdir("banco_dt"):
        if arquivo.endswith(".txt"):
            with open(os.path.join("banco_dt", arquivo), "r") as txt:
                nome_arquivo = txt.readline(2)

                if nome_arquivo == username:
                    mensagem = txt.readline(3)