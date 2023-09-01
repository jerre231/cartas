from fpdf import FPDF

class Carta():
    def __init__(self, carta_id, data, destinatario, mensagem, remetente):
        self.id = carta_id
        self.dt = data
        self.dst = destinatario
        self.msg = mensagem
        self.rmt = remetente
        
        escrever = f"{self.dt}\n{self.dst}\n{self.msg}\n{self.rmt}"
        
        pdf = FPDF()
        pdf_set_font("Arial", size = 12)


    def write(self):
        with open(f"carta_{self.id}.txt", 'w+') as arquivo:
            arquivo.write(escrever)

        pdf.cell(200, 10, txt = self.dt, ln = 1, align = 'C')
        pdf.cell(200, 10, txt = self.dst, ln = 2, align = 'C')
        pdf.cell(200, 10, txt = self.msg, ln = 3, align = 'C')
        pdf.cell(200, 10, txt = self.rmt, ln = 4, align = 'C')
        pdf.output(f"carta_{self.id}.pdf")

class User():
    def __init__(self, user, passw):
        self.username = user
        self.passw = passw

    def cadastrar(self):
        with open('users.txt', 'a') as arquivo:
            linha = f"{self.username}: {self.passw}\n"
            arquivo.write(linha)
