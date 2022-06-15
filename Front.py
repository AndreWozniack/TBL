import PySimpleGUI as sg
import back

sg.theme("DarkTeal4")
def add_prof(x): 
    layout = [
        [sg.Text('Nome'),sg.Input(key='Nome')],
        [sg.Listbox(values=back.areas_atuac, select_mode=True, key='Area Atuação' )],
        [],
        [sg.Button(button_text='Adicionar'), sg.Exit()]
    ]
    while True:
        window = sg.Window(title='Adicionar Professor', layout=layout)
        evento, dados = window.read()
        nome = dados['Nome']
        area_atuac = dados['Area Atuação']
        disps = dados['Disciplinas']
        print(nome, area_atuac)
        if evento == 'Adicionar':
            back.professores.append(back.Professor(nome=nome, area_atuacao=area_atuac, disciplinas=disps))
        elif evento == sg.WIN_CLOSED or evento == 'Exit':
            break

def list_profs():
    lt1 = [
        [sg.Text('Professores:'),sg.Button(button_text='Add Prof')],
        [sg.Listbox(values=back.nomes(back.professores), key='Professor', size=(20,10))],
        [sg.Submit(), sg.Exit()]
    ]
    while True:
        w1 = sg.Window(title='Consultas', layout=lt1, size=(500,300))
        evento, dados = w1.read()
        if evento == 'Add Prof':
            add_prof(back.professores)
            print(dados['Professor'])
        elif evento == sg.WIN_CLOSED or evento == 'Exit':
            break
list_profs()