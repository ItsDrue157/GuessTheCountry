import random

def escolhaMapa():
    escolhaMapas = input("Escolha um mapa para adivinhar: Escolhas: africa, europa, america do sul  ").lower()
    paises_africa = [
        "egito", "nigeria", "africa do sul", "marrocos", "quenia",
        "angola", "mocambique", "tanzania", "gana", "etiopia",
        "camaroes", "senegal", "argelia", "tunisia", "uganda"
    ]
    
    paises_europa = [
        "portugal", "espanha", "franca", "alemanha", "italia",
        "inglaterra", "suica", "suecia", "noruega", "holanda",
        "grecia", "polonia", "russia", "dinamarca", "irlanda"
    ]

    paises_america_sul = [
        "brasil", "argentina", "chile", "colombia", "peru",
        "uruguai", "paraguai", "bolivia", "equador", "venezuela"
    ]

    if escolhaMapas == "africa":
        print("Mapa escolhido: Africa")
        return paises_africa
    elif escolhaMapas == "europa":
        print("Mapa escolhido: Europa")
        return paises_europa
    elif escolhaMapas == "america do sul":
        print("Mapa escolhido: America do Sul")
        return paises_america_sul
    else:
        print("Escolha de mapa inválida. Tente novamente.")
        return escolhaMapa()  # Chama a função novamente até o usuário inserir uma entrada válida

def escolhaPais():
    lista_paises = escolhaMapa()
    escolhaPais = random.choice(lista_paises)
    return escolhaPais

def jogo():
    totalTentativas = 5
    tentativas = 0
    pais = escolhaPais()
    print(pais)
    print("Um país foi escolhido, Tente adivinhar.")

    while tentativas < totalTentativas:
        pais_digitado = input("Digite o nome do País: ").lower()
        tentativas += 1

        if pais_digitado == pais:
            print(f"Parabéns! Você acertou! O país era: {pais}")
            break
        else:
            tentativas_restantes = totalTentativas - tentativas
            if tentativas_restantes > 0:
                print(f"Tentativa incorreta. Você tem {tentativas_restantes} tentativas restantes.")
            else:
                print(f"Acabaram as tentativas! O país correto era: {pais}")


jogo()

