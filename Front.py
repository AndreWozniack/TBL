import PySimpleGUI as sg
import back

sg.theme("DarkTeal4")
def list_profs():
    carga = sg.Text('Carga', k='carga')
    add_prof_bt = sg.Button(button_text='Add Prof')
    lt1 = [
        [sg.Combo(values=back.nomes(back.professores), key='Professor', size=(20,10), enable_events=True), sg.Text('Carga Horaria'), carga],
        [add_prof_bt],
        [sg.Text(f'_'*300)],
        [sg.Text('Selecione sua pasta:'), sg.InputText(key = 'TargetFolder'), sg.FolderBrowse('Pesquisar')],
        [sg.Submit(), sg.Exit()]
    ]
    while True:
        w1 = sg.Window(title='Consultas', layout=lt1, size=(580,320))
        evento, dados = w1.read()
        if evento == 'Professor':
            for i in back.professores:
                if i.nome == dados['Professor']:
                    carga.update(f'{i.contaCarga()}')
                    w1.refresh()
            print(dados['Professor'])
            w1.refresh()
        elif evento == 'Add Prof':
            back.add_prof(back.professores)
        elif evento == sg.WIN_CLOSED or evento == 'Exit':
            break
        elif evento == 'Submit':
            back.criartxt(dados['TargetFolder'], back.professores)
            w1.close()
list_profs()