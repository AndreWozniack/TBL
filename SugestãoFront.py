import PySimpleGUI as sg


sg.theme("DarkTeal4")
layout = [  
            [sg.Text('Nome: ', size = (10, 1)), sg.Input(key = 'Nome')],
            [sg.Radio('Cálculo', "Matéria", default= False, key = 'calculo'), sg.Radio('Física', "Matéria", default= False, key = 'fisica'), 
            sg.Radio('Programação', "Matéria", default= False, key = 'prog'), sg.Radio('Empreendedorismo', "Matéria", default= False, key = 'emp'),
            sg.Radio('Ética', "Matéria", default= False, key = 'etica')],
            [sg.Button('Adicionar Pessoa')],
            [sg.Button('Encerrar', button_color= 'red')]
            ]

janela = sg.Window('Tela de inicio', layout, element_justification= 'center')
evento, dados = janela.read()
pessoas = []
materia = []
while not (evento == sg.WIN_CLOSED or evento == 'Encerrar'): 
    pessoas.append(dados['Nome'])           #adiciona nome a lista
    if dados['etica'] == True:              #adiciona matéria a outra lista (mesmo índice)
        materia.append('Ética')
    elif dados['calculo'] == True:
        materia.append('Cálculo')
    elif dados['fisica'] == True:
        materia.append('Fisica')
    elif dados['prog'] == True:
        materia.append('Programação')
    elif dados['emp'] == True:
        materia.append('Empreendedorismo')
    else:
        materia.append('NONE')              #adiciona 'NONE' caso matéria não exista
    evento, dados = janela.read()
for i in range(len(pessoas)):               #printa nomes e matérias
    print(f'Professor(a): {pessoas[i]}, Matéria: {materia[i]}')

janela.close()