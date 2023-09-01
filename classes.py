from fpdf import FPDF

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
        with open(f"carta_{self.id}.txt", 'w+') as arquivo:
            arquivo.write(self.escrever)

        self.pdf.cell(200, 10, txt = self.dt, ln = 1, align = 'C')
        self.pdf.cell(200, 10, txt = self.dst, ln = 2, align = 'C')
        self.pdf.cell(200, 10, txt = self.msg, ln = 3, align = 'C')
        self.pdf.cell(200, 10, txt = self.rmt, ln = 4, align = 'C')
        self.pdf.output(f"carta_{self.id}.pdf")
