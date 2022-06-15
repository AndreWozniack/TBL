import PySimpleGUI as sg
import back

sg.theme("DarkTeal4")
def list_profs():
    lt1 = [
        [sg.Text('Professores:'),sg.Button(button_text='Add Prof')],
        [sg.Combo(values=back.nomes(back.professores), key='Professor', size=(20,10)), sg.Text('Carga Horaria'), sg.Input()],
        [sg.Text('_____________________________________________________________________________')],
        [sg.Text('Selecione sua pasta:'), sg.InputText(key = 'TargetFolder'), sg.FolderBrowse('Pesquisar')],
        [sg.Submit(), sg.Exit()]
    ]
    while True:
        w1 = sg.Window(title='Consultas', layout=lt1, size=(580,320))
        evento, dados = w1.read()
        if evento == 'Add Prof':
            back.add_prof(back.professores)
            print(dados['Professor'])
        elif evento == sg.WIN_CLOSED or evento == 'Exit':
            break
        elif evento == 'Submit':
            back.criartxt(dados['TargetFolder'], back.professores)
            w1.close()
list_profs()