import random



def escolhaPais():
    lista_paises = ["brasil", "argentina", "portugal", "japão", "canadá", "egito"]
    escolha_pais = random.choice(lista_paises)
    return escolha_pais





def jogo():
    totalTentativas = 5
    tentativas = 0
    pais = escolhaPais()
    print(pais)
    while tentativas < totalTentativas:
        pais_digitado = input("Digite o nome do Pais ").lower()
        

        print(pais)

        tentativas += 1
        

        if pais_digitado == pais:
            print("escolheu o pais certo debug" + pais)
            break
        
        else:
            tentativas_restantes = totalTentativas - tentativas
            if tentativas_restantes > 0:
                print(f"tenativa incorreta voce tem {tentativas_restantes} tentativas. ")
            else:
                print(f"acabaram as tentativas")
        



        
escolhaPais()
jogo()

