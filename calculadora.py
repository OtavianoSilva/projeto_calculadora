from tkinter import *

class Calculadora(Tk):
    def __init__(self):
        super().__init__()

        self.botoes = [
            'C', '+/-', '<', '/',
            7, 8, 9, '*',
            4, 5, 6, '-',
            1, 2, 3, '+',
            0, '.', '='
        ]

        self.variavel_calculo = StringVar()
        self.valor_previo = ''
        self.valor = ''
        self.operador = ''

        self.title('Calculadora')
        self.cria_entry()
        self.cria_botoes()
        self.mainloop()



    def cria_entry(self):

        self.frame_principal = Frame(self)
        self.frame_principal.pack(padx= 10, pady= 10)

        entry = Entry(
            self.frame_principal, justify= 'right', textvariable= self.variavel_calculo,
            state= 'disabled'
            )
        entry.pack(fill= 'x')

    def cria_botoes(self):
        frame = Frame(self.frame_principal)
        frame.pack()

        controle_linha = 0
        controle_coluna = 0

        for botao_legena in self.botoes:
            if controle_coluna == 4:
                controle_linha += 1
                controle_coluna = 0

            botao_calculadora = Button(frame, command= lambda botao = botao_legena:
                self.acao_botao(botao), text= botao_legena, height= 2, width= 3
                )
            botao_calculadora.grid(row= controle_linha, column= controle_coluna)

            controle_coluna += 1

    def acao_botao(self, calculo):
        resultado = self.pre_calculo(calculo)

        self.variavel_calculo.set(resultado)

    def pre_calculo(self, calculo):
        try:
            if calculo == 'C':
                self.valor_previo = ''
                self.valor = ''
            
            elif calculo == '+/-':
                self.valor = self.valor[1:] if self.valor[0] == '-' else '-' + self.valor

            elif calculo == '<':
                self.valor = self.valor[:len(self.valor)-1]

            elif calculo == '.':
                if not calculo in self.valor:
                    self.valor += calculo

            elif calculo == '=':
                self.valor = str(self.calcular())

            elif isinstance(calculo, int):
                self.valor += str(calculo)

            else:
                if self.valor:
                    
                    self.operador = calculo
                    self.valor_previo = self.valor
                    self.valor = ''

            return self.valor
        except: pass
    
    def calcular(self):
        return eval(self.valor_previo + self.operador + self.valor)
    
if __name__ == '__main__':
    calculadora = Calculadora()