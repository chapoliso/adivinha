import random 
import time
import os

def titulo():
    print("#################################")
    print("     ADIVINHA AE SEU MERDA       ")
    print("#################################")

def gerar_numero():
    numero_gerado = random.randrange(1, 101)
    return numero_gerado

def adivinha(numero, tentativa):
    while True:
        try:
            chute = int(input("\nAdivinha o numero entre 1 a 100.\n Resposta: "))
            if chute > 100 or chute < 1:
                time.sleep(1)
                print("\nLesado, apenas numero entre 1 a 100 sabe ler nao, tente novamente:")
            elif chute > numero:
                time.sleep(1)
                print(f"O numero que pensei é menor que {chute}, tente novamente:")
                tentativa += 1
                time.sleep(1)
            elif chute < numero:
                time.sleep(1)
                print(f"O numero que pensei é maior que {chute}, tenta novamente bestao:")
                tentativa += 1
                time.sleep(1)
            elif chute == numero:
                time.sleep(1)
                print(f" o numero é {numero}")
                print(f"PARABAUIS, você acertou com {tentativa} tentativas\n")
                time.sleep(1)
                opcao = input("Vai jogar de novo burro: ( s / n )")
                if opcao.lower() == "s":
                    print("\n Reincinando jogo....")
                    numero = gerar_numero()
                    tentativa += 0
                    os.system("clear")
                    titulo()
                    continue
                elif opcao.lower() == "n" or "nao":
                    time.sleep(1)
                    print("\nOK, vai te embora...")
                    break
        except ValueError:
            print("\nDigite um numero intero kst!!")
            time.sleep(1)


titulo()
input("Digite ENTER para iniciar seu merda...")
numero = gerar_numero()
tentativas = 0
adivinha(numero, tentativas)