import PySimpleGUI as sg

sg.theme = ("DarkTeal2")

janela_principal_layout = [
    [sg.Text("E-mail"), sg.Input(key="E-mail"), ],
    [sg.Text("Senha"), sg.Input(key="Senha", password_char="*")],
    [sg.FolderBrowse("Escolher pasta anexos", target="input_anexos")],
    [sg.FolderBrowse("Escolher pasta planilha", target="input_planilha")],
    [sg.Button("Salvar")]
]

janela = sg.Window("Principal",layout=janela_principal_layout)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == ("Salvar"):
       email = values["E-mail"]
       senha = values["Senha"]
       caminho_pasta_anexos = values['input_anexos']
       caminho_pasta_planilha = values['input_planilha']
