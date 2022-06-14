import PySimpleGUI as sg

layout = [
        [sg.Text('Hello World!')], #escreve o texto 
        [sg.Text('matricula: ', size= ('10', '1')), sg.Input(key = 'matricula')], #define o input com nome ('key' é o nome da chave do dicionario 'dados')
        [sg.Text(('Senha: '), size = ('10', '1')), sg.Input(key = 'senha')],
        [sg.Button('Entrar', button_color='green'), sg.Button('Cancelar', button_color = 'red')] #cria 2 botoes que definem o evento
         ]

janela = sg.Window('Test', layout, element_justification = 'center' '''centraliza tudo''')
evento, dados = janela.read() #captura os eventos (botão) e dados (inputs) do usuário

print(f'evento = {evento}') 
print(f'dados = {dados}')

print(dados['matricula'])
print(dados['senha'])