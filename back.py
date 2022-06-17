import PySimpleGUI as sg
from numpy import size

class Professor:
    def __init__(self, **kwargs) -> None:
        self.nome = kwargs['nome']
        self.area_atuacao = kwargs.pop('area_atuacao', 'ND')
        self.disciplinas = []
        for i in kwargs['disciplinas']:
            self.disciplinas.append(i)
    def contaCarga(self) -> int:
        total = 0
        for i in self.disciplinas:
            total += i.cargaHoraria
        return total

class Disciplina:
    def __init__(self, **kwargs):
        self.nome = kwargs['nome']
        self.cargaHoraria = int(kwargs.pop('carga', 0))

disp1 = Disciplina(nome='MAS',carga=120)
disp2 = Disciplina(nome = 'EAP', carga = 120)
disp3 = Disciplina(nome = 'CSBA', carga = 80)
disp4 = Disciplina(nome='EI',carga=80)
disp5 = Disciplina(nome = 'MS', carga = 120)
disp6 = Disciplina(nome='CAE',carga=120)
disp7 = Disciplina(nome='Ética',carga=60)
disp8 = Disciplina(nome='MSMF',carga=120)
disp9 = Disciplina(nome='QM',carga=80)

prof1 = Professor(nome = 'Karla', area_atuacao = 'Exatas', disciplinas = [disp1, disp5, disp8])
prof2 = Professor(nome = 'Roveredo', area_atuacao = 'Programacao', disciplinas = [disp3, disp6])
prof3 = Professor(nome = 'Mariana', area_atuacao = 'Exatas', disciplinas = [disp2])
prof4 = Professor(nome = 'Glauco', area_atuacao = 'Negocios', disciplinas = [disp4])
prof5 = Professor(nome = 'Fred', area_atuacao = 'Humanas', disciplinas = [disp7])
prof6 = Professor(nome = 'Camila', area_atuacao = 'Exatas', disciplinas = [disp9])
prof7 = Professor(nome='Marli', area_atuacao='Exatas', disciplinas = [disp5,disp8])

areas_atuac = ['Calculo', 'Programação', 'Negócios', 'Humanas']
professores = [prof1, prof2, prof3, prof4, prof5, prof6, prof7]
disciplinas = [disp1, disp2, disp3, disp4, disp5, disp6, disp7, disp8, disp9]

def cira_disp():
    """
    nome = dados['nome']
    carga = dados['carga']
    return Disciplina(nome=nome,carga=carga)
"""
def nomes(x):
    nomes = []
    for i in x:
        nomes.append(i.nome)
    return nomes

def escolha_disp(x:list):
    import PySimpleGUI as sg
    for i in disciplinas: 
            x.insert(2,[sg.Checkbox(text=f'{i.nome}', key=f'{i.nome}')])
    return x

def add_prof(x:list): 
    nome_prof = sg.Input(key='Nome', size=(20,10))
    layout = [
        [sg.Text('Nome'),nome_prof],
        [sg.Combo(values=areas_atuac, key='Area Atuação',default_value='')],
        [],
        [sg.Button(button_text='Adicionar'), sg.Button('Voltar', key='Voltar')]
    ]
    lt_pop = [
        [sg.Text('Professor adicionado com sucesso!')],
        [sg.Button(button_text='Add Outro', k='Add outro'), sg.Button(button_text='Sair', k='Sair')]
    ]
    popup = sg.Window('Adicionado', layout=lt_pop)
    layout = escolha_disp(layout)
    window = sg.Window(title='Adicionar Professor', layout=layout)
    while True:
        try:
            evento, dados = window.read()
            nome = dados['Nome']
            area_atuac = dados['Area Atuação']
            dados['Disciplinas'] = []
            for i in disciplinas:
                if dados[i.nome] == True:
                    dados['Disciplinas'].append(i)
            if  evento == 'Adicionar':
                x.append(Professor(nome=nome, area_atuacao=area_atuac, disciplinas=dados['Disciplinas']))
                nome_prof.update('')
                for i in disciplinas:
                    y = window.find_element(f'{i.nome}')
                    y.update(False)
                z = window.find_element('Area Atuação')
                z.update('')
                while True:
                    p_event , p_dados = popup.read()
                    if p_event == 'Add Outro':
                        popup.close()
                        break
                    elif p_event == 'Sair' or p_event == sg.WIN_CLOSED:
                        popup.close()
                        break
                    break
                window.refresh()
            elif evento == sg.WIN_CLOSED or evento == 'Voltar':
                window.close()
                break
        except TypeError:
            pass

def criartxt(pasta, listaprofs):
    texto = ''
    for i in listaprofs:
        d = []
        for j in i.disciplinas:
            d.append(j.nome)
        texto += f"Nome: {i.nome}    | Disciplinas: {d}  | Carga Horária: {i.contaCarga()} horas\n"
    try:
        file = open(f"{pasta}/DadosProfessor.txt", "x")
        file.write(texto)
    except FileExistsError:
        file = open(f'{pasta}/DadosProfessor.txt', "w")
        file.write(texto)

def cancel():
    cancel = [
        []
    ]

def profs_lista():
    lt_profs = [
        [sg.Listbox(nomes(professores), enable_events=True, key='profs', change_submits=True, size=(12,5)),sg.Text(f'Area de atuação:\n----', k='area_atuac')],
        [sg.Button('Add Prof'), sg.Button('Excluir Prof')],
        [sg.Exit(button_text='Sair')]
    ]  
    w2 = sg.Window('Lista de Professores', layout=lt_profs, size=(300,300))
    while True:
        evento, dados = w2.read()
        area = w2.find_element('area_atuac')
        profs = w2.find_element('profs')
        if evento == 'profs':
            print(dados['profs'])
            for i in professores:
                if len(dados['profs']) > 0  and i.nome == dados['profs'][0]:
                    area.update(f'Area de atuação:\n{i.area_atuacao}')
        if evento == 'Sair' or evento == sg.WIN_CLOSED :
            w2.close()
            break
        elif evento == 'Add Prof':
                add_prof(professores)
                combo = w2.find_element('profs')
                combo.update(values=nomes(professores))
                for i in professores:
                    print(i.nome, end=', ')
                w2.refresh()
        elif evento == 'Excluir Prof':
            for i in professores:
                if len(dados['profs']) > 0  and i.nome == dados['profs'][0]:
                        sg.popup(f'Tem certeza que deseja excluir o professor(a): {dados["profs"][0]}',title='Aviso!')
                        professores.remove(i)
                        profs.update(nomes(professores))
                        area.update(f'Area de atuação:\n----')
                        w2.refresh()
