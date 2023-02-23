import PySimpleGUI as sg
import os

def visualizar_diario():
    if not os.path.exists("diario.txt"):
        return "O diário está vazio."
    else:
        # Abre o arquivo do diário em modo de leitura e exibe as entradas
        with open("diario.txt", "r") as arquivo_diario:
            return arquivo_diario.read()

def Main():
    sg.set_global_icon('diary-icon.ico')
    sg.theme('Reddit')
    layout = [
        [sg.Text('Diario digital')],
        [sg.Button('Adicionar Diario'), sg.Button('Visualizar Diario')],
        [sg.Text('')],
        [sg.Button('Sair')],
    ]

    janela = sg.Window("Principal", layout, finalize= True)
    return janela

def Adicionar():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Digite a data da entrada (DD/MM/AAAA):")],
        [sg.InputText(key="data")],
        [sg.Text("Digite o conteúdo:")],
        [sg.InputText(key='conteudo')],
        [sg.Button('Enviar'),sg.Button('Voltar')],
    ]

    janela = sg.Window("Adicionando", layout, finalize= True)
    return janela

def Visualizar():
    sg.theme('Reddit')
    layout = [
        [sg.Text(visualizar_diario())],
        [sg.Button('Voltar')],
    ]

    janela = sg.Window("Visualizando", layout, finalize=True)
    return janela


def adicionar_entrada_diario(data, entrada):
    if not os.path.exists("diario.txt"):
        with open("diario.txt", "w") as arquivo_diario:
            arquivo_diario.write("Diário do Isac\n\n")
            arquivo_diario.write(f"{data}: {entrada}\n")
    else:
        with open("diario.txt", "a") as arquivo_diario:
            arquivo_diario.write(f"{data}: {entrada}\n")



janela1, janela2, janela3 = Main(), None, None
while True:
    window, events, valores = sg.read_all_windows()
    if events == sg.WIN_CLOSED or (window == janela1 and events == 'Sair'):
        break
    if events == 'Adicionar Diario' and window == janela1:
        janela2 = Adicionar()
        janela1.hide()
    if window == janela2 and events == 'Voltar':
        janela1.un_hide()
        janela2.hide()
    if window == janela2 and events == 'Enviar':
        adicionar_entrada_diario(valores['data'],valores['conteudo'])
        janela1.un_hide()
        janela2.hide()
    if window == janela2 and events == 'Enviar':
        adicionar_entrada_diario(valores['data'],valores['conteudo'])
        janela1.un_hide()
        janela2.hide()
    if window == janela1 and events == 'Visualizar Diario':
        janela3 = Visualizar()
        janela1.hide()
    if window == janela3 and events == 'Voltar':
        janela1.un_hide()
        janela3.hide()
    
        
