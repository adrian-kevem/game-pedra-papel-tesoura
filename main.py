import random
import os

JOGADOR = 0
COMPUTADOR = 0

def boas_vindas():
    print(" ========================")
    print("| Pedra, Papel e Tesoura |")
    print(" ========================")

def placar():
    global JOGADOR, COMPUTADOR
    print("\n(PLACAR)")
    print(f"Jogador -> {JOGADOR}")
    print(f"Computador -> {COMPUTADOR}")

def jogar():
    global JOGADOR, COMPUTADOR
    print("\n1 - Pedra | 2 - Papel | 3 - Tesoura")
    jogada_jogador = int(input(">>>>> Escolha sua jogada: "))
    if(jogada_jogador == 1):
        print("Você jogou: Pedra")
    elif(jogada_jogador == 2):
        print("Você jogou: Papel")
    elif(jogada_jogador == 3):
        print("Você jogou: Tesoura")
    else:
        print("Jogada inválida!")
        return
    jogada_computador = random.randint(1, 3)
    if(jogada_computador == 1):
        print("Computador jogou: Pedra")
    elif(jogada_computador == 2):
        print("Computador jogou: Papel")
    elif(jogada_computador == 3):
        print("Computador jogou: Tesoura")
    else:
        print("Jogada inválida!")
        return
    
    if((jogada_jogador == 1) and (jogada_computador == 1)):
        print("Ninguém venceu, pois pedra anula pedra!")
    elif((jogada_jogador == 2) and (jogada_computador == 2)):
        print("Ninguém venceu, pois papel anula papel!")
    elif((jogada_jogador == 3) and (jogada_computador == 3)):
        print("Ninguém venceu, pois tesoura anula tesoura!")
    elif((jogada_jogador == 1) and (jogada_computador == 2)):
        print("Você perdeu, pois papel vence pedra!")
        COMPUTADOR += 1
    elif((jogada_jogador == 1) and (jogada_computador == 3)):
        print("Você venceu, pois pedra vence tesoura!")
        JOGADOR += 1
    elif((jogada_jogador == 2) and (jogada_computador == 1)):
        print("Você venceu, pois papel vence pedra!")
        JOGADOR += 1
    elif((jogada_jogador == 2) and (jogada_computador == 3)):
        print("Você perdeu, pois tesoura vence papel!")
        COMPUTADOR += 1
    elif((jogada_jogador == 3) and (jogada_computador == 1)):
        print("Você perdeu, pois pedra vence tesoura!")
        COMPUTADOR += 1
    elif((jogada_jogador == 3) and (jogada_computador == 2)):
        print("Você venceu, pois tesoura vence papel!")
        JOGADOR += 1
    else:
        print("Jogada inválida!")
    
if __name__ == "__main__":
    while True:
        primeira_rodada = True
        if primeira_rodada == True:
            boas_vindas()
            primeira_rodada == False
        placar()
        jogar()
        input("Continuar...")
        os.system("cls" if os.name == "nt" else "clear")
