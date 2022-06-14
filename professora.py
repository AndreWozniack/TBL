import PySimpleGUI as sg
# Janela popup com UMA LINHA
sg.popup('Concepção de Soluções Baseadas em Aplicativos', title='CSBA')
sg.popup('Concepção de Soluções Baseadas em Aplicativos', title='CSBA',
         text_color='red', background_color='yellow', location=(200, 80))
# OLHA O DICIONÁRIO AÍ GENTE!!!!!

# Janela popup com várias linhas de texto
sg.popup('Concepção de', 'Soluções', 'Baseadas em', 'Aplicativos', title='CCPE',
         text_color='white', background_color='blue', location=(200, 80))
# janela popup que contenha um campo de texto para que o usuário digite 
# na forma de string e que, quando encerrada, transfira a string digitada para o programa

# Exemplo de janela popup para entrada de um dado textual
nome_do_cliente = sg.popup_get_text('Nome', title='Cadastro de Cliente')
print(nome_do_cliente)
# janela popup para confirmação de dado de entrada textual
sg.popup('O seguinte cliente será inserido no sistema:', nome_do_cliente,
         title='Notificação')

#janela popup para entrada de um dado numérico
preco_textual = sg.popup_get_text('Preço', title='Cadastro de Produto')
preco_do_produto = float(preco_textual)
# popup de confirmação
sg.popup('O seguinte preço será inserido no sistema:', preco_do_produto,
         title='Notificação')

# encerramento abrupto do programa 
# evitar isso é inserir tratamento de exceção no programa
while True:
    preco_textual = sg.popup_get_text('Preço', title='Cadastro de Produto')

    try:
        preco_do_produto = float(preco_textual)
        sg.popup('O seguinte preço será inserido no sistema:', preco_do_produto,
                title='Notificação')
        break
    except ValueError:
        sg.popup_error('Dado inválido')


# JANELA E LAYOUT

# formatos específicos necessários para a aplicação

#	A primeira linha contém apenas um elemento do tipo Text \
    # com o valor "Concepção de Soluções Baseadas em Aplicativos".
#	A segunda linha contém dois elementos:
#     	Um elemento do tipo Text com o valor "Matrícula:"
#	    Um elemento do tipo Input (caixa de entrada)
#	A terceira linha contém dois elementos:
#   	Um elemento do tipo Text com o valor "Senha:"
#   	Um elemento do tipo Input (caixa de entrada)
#	A quarta linha contém dois elementos:
#   	Um elemento do tipo Button na cor verde e com o rótulo "entrar"
#   	Um elemento do tipo Button na cor vermelha e com o rótulo "cancelar"

# layout é expresso no programa por meio de uma LISTA de LISTAS DE ELEMENTOS 

layout = [
    [sg.Text('Concepção de Soluções Baseadas em Aplicativos')],
    [sg.Text('Matrícula: ', size=(10, 1)), sg.Input()],
    [sg.Text('Senha:     ', size=(10, 1)), sg.Input()],
    [sg.Button('entrar', button_color='green'), sg.Button('cancelar', button_color='red')]
]

# parâmetro size na criação dos elementos do tipo Text é usado
# a fim de padronizar os tamanhos das caixas de entrada

janela = sg.Window('Bem-vindo ao Curso!', layout)

# função Window requer, no mínimo, dois parâmetro: o título 
# (uma string) e o layout (uma lista de listas de elementos) da janela.
# element_justification centraliza os elementos da janela

# A captura do evento gerado e dos dados fornecidos é 
# realizada por meio da chamada da função read, como segue.
evento, dados = janela.read()
print(evento)      #mostra o evento selecionado  entrar
print(dados)       #mostra os dados usando dicionário
                   #exemplo: {0: '01010101', 1: '1234'}
matricula = dados[0]
senha = dados[1]
janela.Close()

# PORÉM....... usar forma mais simbólica de indexação, baseada em chaves 
# que o programador define
import PySimpleGUI as sg

layout = [
    [sg.Text('Concepção de Soluções Baseadas em Aplicativos')],
    [sg.Text('Matrícula: ', size=(10, 1)), sg.Input(key='matricula')],
    [sg.Text('Senha:     ', size=(10, 1)), sg.Input(key='senha')],
    [sg.Button('entrar', button_color='green'), sg.Button('cancelar', \
                                                          button_color='red')]
]

janela = sg.Window('Bem-vindo ao Curso!', layout,
                   element_justification='center')
evento, dados = janela.read()

matricula = dados['matricula']
senha = dados['senha']

print(matricula, senha)
janela.close()

# função close() apenas para que o sistema de execução destrua o 
# objeto da classe Window, fazendo a liberação de memória


# construção de uma interface gráfica simples 

# BOTÃO CALENDÁRIO
# campo referente à data pode ser feito com auxílio de um calendário 
# que é exibido numa janela popup
layout = [
    [sg.Text('Nome:', size=(22, 1)), sg.Input()],
    [sg.Text('Data do nascimento:', size=(22, 1)),
     sg.Input(key='nascimento'),
     sg.CalendarButton(button_text='Escolher')],
    [sg.Button('OK', button_color='purple')]
]

# A data escolhida é, inserida na caixa de entrada imediatamente 
# anterior (com key igual a 'nascimento') no formato YYYY-MM-DD.  
# porém traz a hora também
# para tirá-la usa o comando split
janela = sg.Window('Registro de Nascimento', layout)
evento, dados = janela.read()
nascimento = dados['nascimento']

# por garantia, verificar se a lista campos contém algum elemento; 
# a lista será vazia caso o usuário pressione o botão OK sem que a 
# caixa de entrada para a data de nascimento esteja preenchida.
campos = nascimento.split()    # split separa o 1ª do 2º campo
if len(campos) > 0:
    data = campos[0]
    print(data)

janela.close()

# lista pré-determinada de valores - LISTBOX
cidades = ['Londres', 'Paris', 'Barcelona', 'Roma', 'Praga']

layout = [
    [sg.Listbox(values=cidades, size=(30, 6), key='cidade')],
    [sg.Button('OK')]
]
# após escolha do usuário e botão OK, a escolha é retornada pela função read
janela = sg.Window('Cidades', layout)
evento, dados = janela.read()
if len(dados) > 0:
    cidade_escolhida = dados['cidade'][0]
    print(cidade_escolhida)
janela.close()

# Caixa de seleção - CHECKBOX - escolha de uma ou mais opções

# Janela com uma lista de valores para assinalamento

layout = [
    [sg.Text('Assinale as doenças que teve na infância:')],
    [sg.Checkbox('Sarampo', key='sarampo'),
     sg.Checkbox('Rubéola', key='rubeola'),
     sg.Checkbox('Caxumba', key='caxumba'),
     sg.Checkbox('Catapora', key='catapora')],
    [sg.Button('OK')]
]
janela = sg.Window('Avaliação de Imunidade', layout)
evento, dados = janela.read()
teve_sarampo = dados['sarampo']
teve_rubeola = dados['rubeola']
teve_caxumba = dados['caxumba']
teve_catapora = dados['catapora']
if teve_sarampo and teve_rubeola and teve_caxumba and teve_catapora:
    sg.popup('Você tem imunidade completa.', title='Conclusão')
else:
    sg.popup('Fique atento a sinais de doenças!', title='Conclusão')
janela.close()


#Barra de Seleção (Slider)
# permite ao usuário definir um valor numérico dentro de um intervalo específico
# volume pode variar entre 0 e 100, enquanto o balance pode variar entre
# -50 e 50
# valor inicial do volume é 20
# valor inicial do balance é 0.

# Janela com barras de seleção
# range determina os valores mínimo e máximo para a barra
layout = [
    [sg.Text('Volume (0 a 100):', size=(20, 1)),
     sg.Slider(range=(0, 100),
         default_value=20,
         size=(20,15),
         orientation='horizontal',
         key='volume')],
    [sg.Text('Balance (-50 a 50):', size=(20, 1)),
     sg.Slider(range=(-50, 50),
        default_value=0,
        size=(20, 15),
        orientation='horizontal',
        key='balance')],
    [sg.Button('OK')]
]

janela = sg.Window('Configuração do Som', layout)
evento, dados = janela.read()
volume = dados['volume']
balance = dados['balance']
confirmado = sg.popup_yes_no('Alterar volume para ' + str(volume) +
                ' e balance para ' + str(balance),
                title='Alteração')
janela.close()

# JANELA PERSISTENTE -  continua existindo após o comando read
# Janela persistente para digitação de uma sequência de valores 
# em dois momentos: aguardando o primeiro valor da sequência e 
# aguardando o sexto valor

valor = sg.Input(key='valor', size=(30, 1))
ordem = sg.Text('[ 1 ]', size=(5, 1))
lista = sg.Multiline(size=(30, 10))

layout = [
    [sg.Text('Digite um valor:')],
    [valor, ordem],
    [sg.Button('Salvar'), sg.Exit('Finalizar')],
    [lista]
]
janela = sg.Window('Sequência de Valores', layout)
contador = 1
evento, dados = janela.read()
while not (evento == sg.WIN_CLOSED or evento == 'Finalizar'):
    # sg.WIN_CLOSED é forçar o fechamento da janela pelo usuário
    x = dados['valor']
    # variável lista corresponde à caixa de múltiplas linhas
    lista.print(x) # lista é ATUALIZADA pelo print para cada novo valor fornecido
    contador = contador + 1
    ordem.Update('[ ' + str(contador) + ' ]')  #ordem atualizado por Update
    valor.Update('') # valor corresponde à caixa de texto para a digitação 
    # atualizada com uma string vazia a fim de limpar a digitação anterior
    evento, dados = janela.read()

janela.close()