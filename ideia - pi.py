## um pouco de ideias pra edição do layout

import PySimpleGUI as sg

infos = [
    ['PROF 1','MATERIA1','HORA-AULA'],
    ['PROF 2','MATERIA5','HORA-AULA'],
    ['PROF 3','MATERIA2','HORA-AULA'],
]

layout = [
    [sg.Text('Textão aq OI GNT BEM VINDO!', size=(30, 1), font=("Helvetica", 25), text_color='white')],
    [sg.Text('um pouco do codigo')],
    [sg.InputText()],
    [sg.Checkbox('check'), sg.Checkbox('check de novo!', default=True)],
    [sg.Radio('?     ', "R1", default=True), sg.Radio('!', "R2")],
    [sg.InputCombo(['andre', 'gustavo', 'rafinha','tito'], size=(20, 3)),
     sg.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=85)],
    [sg.Listbox(values=['A', 'B', 'C'], size=(30, 6)),
     sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=10)],
    [sg.Text('_'  * 100, size=(70, 1))],
    [sg.Text('as pastas e tals', size=(35, 1))],
    [sg.Text('pasta de origem', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Origem'),
     sg.FolderBrowse()],
    [sg.Text('pasta de destino', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Destino'),
     sg.FolderBrowse()],
    [sg.Submit(), sg.Cancel(), sg.SimpleButton('customise', button_color=('white', 'green'))],
    [sg.Table(values=infos,headings=matriz,max_col_width=35,
            auto_size_columns=True,
            display_row_numbers= True,
            num_rows = 10,
            key = '-TABLE-',
            row_height=35)]]

janela = sg.Window('Test', layout, element_justification = 'center')
janela.read()