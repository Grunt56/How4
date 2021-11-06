import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Checkbox

class telapyton:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(12,0),key='nome')],
            [sg.Text('Raça',size=(5,0)),sg.Input(size=(12,0),key='raça')],
            [sg.Text('Classe',size=(5,0)),sg.Input(size=(12,0),key='classe')],
            [sg.Text('Alinhamento do Personagem')],
            [sg.Checkbox('Leal',key='leal'),sg.Checkbox('Neutro',key='neutro'),sg.Checkbox('Caotico',key='caotico')],
            [sg.Button('Ok')]
        ]
        # Janela
        janela = sg.Window("Dados do Personagem").layout(layout)
        # Extrair os dados da tela
        self.button, self.values = janela.Read()

    def Iniciar(self):
        nome = self.values['nome']   
        raça = self.values['raça']
        classe = self.values['classe']
        aceita_leal = self.values['leal']
        aceita_neutro = self.values['neutro']
        aceita_caotico = self.values['caotico']
        print(f'nome:{nome}')
        print(f'raça:{raça}')
        print(f'classe:{classe}')
        print(f'leal:{aceita_leal}')
        print(f'neutro:{aceita_neutro}')
        print(f'caotico:{aceita_caotico}')

tela = telapyton()
tela.Iniciar()           