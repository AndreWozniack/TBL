import googlemaps
from datetime import datetime
import PySimpleGUI as sg
from lxml import html


def strip_html(s):
    return str(html.fromstring(s).text_content())

# =============

def limpar_respostas():
    janela['origem_ajustada'].Update('')
    janela['destino_ajustado'].Update('')
    janela['distancia_total'].Update('')
    janela['tempo_total'].Update('')
    janela['rota'].Update('')

# =============

def limpar_tudo():
    janela['origem'].Update('')
    janela['destino'].Update('')
    limpar_respostas()

# =============

def preencher_respostas(info):
    origem_ajustada = info[0]['legs'][0]['start_address']
    destino_ajustado = info[0]['legs'][0]['end_address']
    distancia_total = info[0]['legs'][0]['distance']['text']
    tempo_total = info[0]['legs'][0]['duration']['text']
    janela['origem_ajustada'].Update(origem_ajustada)
    janela['destino_ajustado'].Update(destino_ajustado)
    janela['distancia_total'].Update(distancia_total)
    janela['tempo_total'].Update(tempo_total)
    impar = True

    for s in info[0]['legs'][0]['steps']:
      distancia = s['distance']['text']
      duracao = s['duration']['text']
      instrucoes = s['html_instructions']

    i = 1
    for s in info[0]['legs'][0]['steps']:
        if impar:
            cor_texto = 'black'
            cor_back = 'white'
        else:
            cor_texto = 'blue'
            cor_back = 'yellow'
        impar = not impar
        janela['rota'].print('(', i, ')',  s['distance']['text'], ' ===> ',
                             s['duration']['text'],
                             text_color=cor_texto, background_color=cor_back)
        janela['rota'].print(strip_html(s['html_instructions']),
                             text_color=cor_texto, background_color=cor_back)
        i = i + 1

# =============


def descobrir_rota():
    limpar_respostas()
    origem = dados['origem']
    destino = dados['destino']
    if   dados['modo_veiculo']:   modo_escolhido = 'driving'
    elif dados['modo_bicicleta']:  modo_escolhido = 'bicycling'
    elif dados['modo_caminhada']: modo_escolhido = 'walking'
    now = datetime.now()
    info = gmaps.directions(origem, destino, mode=modo_escolhido,
                            departure_time=now, language='pt-BR')
    if len(info) > 0:
        preencher_respostas(info)
    else:
        janela['rota'].print('NADA ENCONTRADO', text_color='red')

# =============


FONTE = 'Helvetica 8'

layout = [
    [sg.Text('Origem:', size=(10, 1), font=FONTE)],
    [sg.Input(size=(32, 1), key='origem', font=FONTE)],
    [sg.Text(size=(32, 3), key='origem_ajustada', font=FONTE, text_color='black', background_color='yellow')],
    [sg.Text('Destino:', size=(10, 1), font=FONTE)],
    [sg.Input(size=(32, 1), key='destino', font=FONTE)],
    [sg.Text(size=(32, 3), key='destino_ajustado', font=FONTE, text_color='black', background_color='yellow')],
    [sg.Radio('Veículo', 'modos', default=True, key='modo_veiculo', font=FONTE),
     sg.Radio('Caminhada', 'modos', default=False, key='modo_caminhada', font=FONTE),
     sg.Radio('Bicicleta', 'modos', default=False, key='modo_bicicleta', font=FONTE)],
    [sg.Button('DESCOBRIR ROTA', button_color='black', font=FONTE)],
    [sg.Text('Distância:', size=(8, 1), font=FONTE),
     sg.Text(size=(22, 1), key='distancia_total', font=FONTE,
             text_color='black', background_color='yellow')],
    [sg.Text('Tempo: ', size=(8, 1), font=FONTE),
     sg.Text(size=(22, 1), key='tempo_total', font=FONTE,
             text_color='black', background_color='yellow')],
    [sg.Text('Rota:', font=FONTE)],
    [sg.MLine(size=(32, 13), key='rota', font=FONTE, write_only=True, no_scrollbar=False)],
    [sg.Button('LIMPAR', font=FONTE, size=(12, 1)),
     sg.Button('FINALIZAR', button_color='red', font=FONTE, size=(12, 1))]
]

janela = sg.Window('MyWay', layout, location=(0, 0))

gmaps = googlemaps.Client(key='AIzaSyAriFz-sb8mY6oA5wh9ViiKMlfTggk-BaE')

evento, dados = janela.read()
while not (evento == sg.WIN_CLOSED or evento == 'FINALIZAR'):
    if evento == 'DESCOBRIR ROTA': descobrir_rota()
    elif evento == 'LIMPAR': limpar_tudo()
    evento, dados = janela.read()