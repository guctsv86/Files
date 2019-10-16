# Pedra-papel-tesoura-lagarto-Spock

# A chave deste programa é igualar as strings
# "pedra", "papel", "tesoura", "lagarto", "Spock"
# em números a seguir:

# 0 - pedra
# 1 - Spock
# 2 - papel
# 3 - lagarto
# 4 - tesoura

import random

# Funções auxiliares:
def number_to_name(number):
    # converter número em nome usando if/elif/else

    if number == 0:
        return "pedra"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "papel"
    elif number == 3:
        return "lagarto"
    elif number == 4:
        return "tesoura"
    else:
        print("BURRO!!!!!")

def name_to_number(name):
    # converter nome em número usando if/elif/else

    if name == "pedra":
        return 0
    elif name == "Spock":
        return 1
    elif name == "papel":
        return 2
    elif name == "lagarto":
        return 3
    elif name == "tesoura":
        return 4
    else:
        print("Errou!!!!!")

def pptls(escolha):
    # converter nome para player_number usando name_to_number
    player_number = name_to_number(escolha)

    # calcular random guess para comp_number usando random.randrange()
    comp_number = random.randrange(0, 5)

    # calcular diferença de player_number e comp_number modulo five
    diferenca = (comp_number - player_number) % 5

    # converter comp_number para nome usando number_to_name
    comp_escolha = number_to_name(comp_number)

    # Expor escolhas
    print("Jogador escolheu " + escolha)
    print("Computador escolheu " + comp_escolha)
    
    # if/elif/else para determinar o vencedor
    if diferenca == 0:
        print("Ninguém venceu.")
    elif diferenca == 1 or diferenca == 2:
        print("Computador venceu.")
    elif diferenca == 3 or diferenca == 4:
        print("Jogador venceu.")

# Testar código
#pptls("pedra")
pptls("papel")
#pptls("tesoura")
#pptls("lagarto")
#pptls("Spock")
