# ~~~~Desafio 01 - Detetive.
# O programa fará 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# • "Você telefonou para a vítima?"
# • " Você esteve no local do crime?"
# • " Você mora perto da vítima?"
# • " Você devia para a vítima?"
# • " Você já trabalhou com a vítima?"

# Se a pessoa responder positivamente a:
# • 2 questões ela deve ser classificada como "Suspeita",
# • Entre 3 e 4 como "Cúmplice"
# • 5 como "Assassino". 
# • Caso contrário, ele será classificado como "Inocente".

# váriaveis para armazenar quantas respostas foram positivas ou negativas.
respostaSim = 0
respostaNao = 0
# váriaveis para armazenas as perguntas. (As perguntas poderiam estar direto no print)
pergunta1 = 'Você telefonou para a vítima?'
pergunta2 = 'Você esteve no local do crime?'
pergunta3 = 'Você mora perto da vítima?'
pergunta4 = 'Você devia para a vítima?'
pergunta5 = 'Você já trabalhou com a vítima?'
# explicar para o úsuario o que ele irá faze.
print('Por favor responda com "Sim" ou "Não" as próximas 5 perguntas.')
# fazer a primeira pergunta.
while True:
    resposta = input(f'{pergunta1}\nSim ou Não: ').upper()
    # verificamos se a resposta é sim ou não.
    if resposta=='SIM' or resposta=='NÃO' or resposta=='NAO':
        # se a resposta for sim alimentamos a var respostaSim
        if resposta=='SIM':
            respostaSim+=1
            break
        # se a resposta for não alimentamos a var respostaNao    
        else:
            respostaNao+=1
            break
    # se a resposta não for 'sim' ou 'não', pedimos para o úsuario responder novamente
    else:
        print('Resposta incorreta. por favor responda "Sim" ou "Não".')




    


