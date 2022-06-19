import PySimpleGUI as sg
import back

sg.theme("DarkTeal4")
def list_profs():
    filtros = {'professores':back.professores, 'disciplinas':back.disciplinas,}
    k_filtros = []
    for i in filtros:
        k_filtros.append(i)

    lt1 = [
        [[sg.Combo(k_filtros, k='filtros', enable_events=True)], sg.Listbox( [] , enable_events=True, key='profs', size=(10,5)),sg.Text('' , enable_events = True, k ='disc') ],
        [sg.Button('Editar Professores')],
        [sg.Button('Editar Disciplinas')],

        [sg.Text(f'_'*300)],
        [sg.Text('Selecione sua pasta:'), sg.InputText(key = 'TargetFolder'), sg.FolderBrowse('Pesquisar')],
        [sg.Submit(), sg.Exit()]
    ]
    w1 = sg.Window(title='Consultas', layout=lt1, size=(580,300))
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
                        if dados['filtros'] == 'professores':
                            disci.update(f'Disciplina(s): .......')
            if evento == 'profs':
                print('opa')
                w1.refresh()
            if evento == 'Editar Professores':
                back.profs_lista()
            elif evento == 'Editar Disciplinas':
                back.disc_list()
            elif evento == sg.WIN_CLOSED or evento == 'Exit':
                break
            elif evento == 'Submit':
                back.criartxt(dados['TargetFolder'], back.professores)
                w1.close()
        except PermissionError:
            pass
list_profs()