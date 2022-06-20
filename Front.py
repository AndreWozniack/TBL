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
    lt1 = [
        [sg.Combo(k_filtros, k='filtros', enable_events=True,
        s=(16,1)),sg.Listbox( [] , enable_events=True, key='profs',
        size=(16,5))],
        [sg.Text('' , enable_events = True, k ='disc', size=(16,1))],
        [sg.Button('Editar Professores', s=(15,1))],
        [sg.Button('Editar Disciplinas', s=(15,1))],
        [sg.Button('Gerar Relatório', s=(15,1))],
        [sg.Button('Sair', s=(15,1)), sg.Button('Créditos')]
    ]

    w1 = sg.Window(title='Consultas', layout=lt1, size=(300,280))
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
            if evento == 'profs':        
                    #if dados['filtros'] == 'professores':
                        for a in back.professores:
                            if len(dados['profs']) > 0 and a.nome == dados['profs'][0]:
                                disci.update(f'Disciplina(s): {a.disciplinas[0].nome}')               
                    #if dados['filtros'] == 'disciplinas':
                        #disci.update('')
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
            elif evento == 'Créditos':
                sg.popup_no_buttons(size = (300,300), image = 'gato.png')
        except PermissionError:
            pass

root()