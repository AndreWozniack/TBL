import PySimpleGUI as sg
import back

sg.theme("DarkTeal4")

def root():
    """
    Função principal para a execução do aplicativo
    """
    filtros = {'professores':back.professores, 'disciplinas':back.disciplinas,}
    k_filtros = []
    for i in filtros:
        k_filtros.append(i)

    botoes = [
        [sg.Button('Editar Professores', s=(15,1))],
        [sg.Button('Editar Disciplinas', s=(15,1))],
        [sg.Button('Gerar Relatório', s=(15,1))],
        [sg.Button('Sair', s=(15,1))], [sg.Button('Créditos', s=(15,1))]
    ]
   
    combo = [
        [sg.Listbox( [] , enable_events=True, key='profs',size=(15,5))],
        [sg.Combo(k_filtros, k='filtros', enable_events=True,s=(15,1))],
        [sg.Text('' , enable_events = True, k ='disc', size=(15,1))]
    ]

    opcoes = [[sg.Frame('Opções',botoes, element_justification='c')]]
    lista_filtro = [[sg.Frame('Lista',combo)]]
    layout = [[sg.Column(lista_filtro),sg.Column(opcoes)]]
    
    w1 = sg.Window(title='Consultas', layout=layout, size=(330,220))
    while True:
        try:
            evento, dados = w1.read()
            filtro = w1.find_element('filtros')
            profs = w1.find_element('profs')
            disci = w1.find_element('disc')
            if evento == 'filtros':
                for i in filtros:
                    if i == dados['filtros']:
                        profs.update(back.nomes(filtros[i]))
                w1.refresh()
            if evento == 'Editar Professores':
                back.profs_lista()
            elif evento == 'Créditos':
                back.creditos()    
            elif evento == 'Editar Disciplinas':
                back.disc_list()
            elif evento == 'Gerar Relatório':
                back.relatorio()
            elif evento == sg.WIN_CLOSED or evento == 'Sair':
                break
        except PermissionError:
            pass

root()