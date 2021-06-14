# váriaveis para armazenar quantas respostas foram positivas ou negativas.
respostaSim = 0
respostaNao = 0 # váriavel não esta sendo útilizada atualmente. 
# váriavel para verificar se as perguntas foram respondidas
nPerguntas = 0
# váriaveis para armazenas as perguntas. (As perguntas poderiam estar direto no print)
pergunta1 = 'Você telefonou para a vítima?'
pergunta2 = 'Você esteve no local do crime?'
pergunta3 = 'Você mora perto da vítima?'
pergunta4 = 'Você devia para a vítima?'
pergunta5 = 'Você já trabalhou com a vítima?'
# explicar para o úsuario o que ele irá faze.
print('\nPor favor responda com "Sim" ou "Não" as próximas 5 perguntas.')
print('De acordo com a suas respostas vamos classificar sua participação no crime.')
# fazer as perguntas.
while True:
    if nPerguntas == 0:
        resposta = input(f'\n{pergunta1}\nSim ou Não: ').upper()
    elif nPerguntas == 1:
        resposta = input(f'\n{pergunta2}\nSim ou Não: ').upper()
    elif nPerguntas == 2:
        resposta = input(f'\n{pergunta3}\nSim ou Não: ').upper()
    elif nPerguntas == 3:
        resposta = input(f'\n{pergunta4}\nSim ou Não: ').upper()
    elif nPerguntas == 4:
        resposta = input(f'\n{pergunta5}\nSim ou Não: ').upper()
    else:
        break
    # verificamos se a resposta é sim ou não.
    if resposta=='SIM' or resposta=='NÃO' or resposta=='NAO':
        # se a resposta for sim alimentamos a var respostaSim
        if resposta=='SIM':
            respostaSim += 1
            nPerguntas += 1
        # se a resposta for não alimentamos a var respostaNao    
        else:
            respostaNao += 1
            nPerguntas += 1
    # se a resposta não for 'sim' ou 'não', pedimos para o úsuario responder novamente
    else:
        print('Resposta incorreta. por favor responda "Sim" ou "Não".')

# agora verificamos se o úsuario é "Suspeito", "Cúmplice", "Assassino" ou "Inocente"
if respostaSim == 5: # 5 respostas positivas, Assassino.
    print("\nVocê foi classificado como 'Assassino'.")
elif respostaSim == 3 or respostaSim == 4: # 3 a 4 respostas positivas, Cúmplice
    print("\nVocê foi classificado como 'Cúmplice'.")
elif respostaSim == 2: # 2 respostas positivas, Suspeito
    print("\nVocê foi classificado como 'Suspeito'.")         
else: # 1 ou 0 resposta positivas, Inocente
    print("\nVocê foi classificado como 'Inocente'.")         
