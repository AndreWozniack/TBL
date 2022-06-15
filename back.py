import PySimpleGUI as sg

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
        self.cargaHoraria = kwargs.pop('carga', 0)

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



    
def criartxt(pasta, listaprofs):
    try:
        file = open(f"{pasta}/DadosProfessor.txt", "x")
        for i in listaprofs:
            d = ''
            for j in i.disciplinas:
                d += j.nome + ', '
            file.write(f"Nome: {i.nome}    | Disciplinas: {d}  | Carga Horária: {i.contaCarga}\n")
    except FileExistsError:
        sg.popup_error('Arquivo já existente!')

def escolha_disp(x:list):
    import PySimpleGUI as sg
    for i in disciplinas: 
            x.insert(2,[sg.Checkbox(text=f'{i.nome}', key=f'Disciplinas')])
    return x

def add_prof(x): 
    layout = [
        [sg.Text('Nome'),sg.Input(key='Nome', size=(20,10))],
        [sg.Combo(values=areas_atuac, key='Area Atuação' )],
        [],
        [sg.Button(button_text='Adicionar'), sg.Button('Voltar', key='Voltar')]
    ]
    layout = escolha_disp(layout)
    while True:
        window = sg.Window(title='Adicionar Professor', layout=layout)
        evento, dados = window.read()
        nome = dados['Nome']
        area_atuac = dados['Area Atuação']
        disps = dados['Disciplinas']
        print(nome, area_atuac)
        if evento == 'Adicionar':
            professores.append(Professor(nome=nome, area_atuacao=area_atuac, disciplinas=disps))
        elif evento == sg.WIN_CLOSED or evento == 'Voltar':
            break

