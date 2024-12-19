import random
print("*********************************************************")
print("         Bem vindo ao jogo de adivinhação                 ")
print("*********************************************************")
def jogo():
    numero_secreto = random.randint(1, 101)
    total_tentivas = 4
    for rodada in range(1, total_tentivas + 1):
        chute_str = input ("Informe o numero de advinhação de 0 a 100: ")
        print("Você digitou", chute_str)
        chute_str = int(chute_str)
        if (chute_str < 1 or chute_str > 100):
            print("Jogo com uma regra, por gentileza informe um numero de 1 a 100.")
            continue

        acertou = chute_str == numero_secreto
        maior = chute_str > numero_secreto
        menor = chute_str < numero_secreto

        if(acertou):
            print("PARABÉNNNNNSSSS")
            break
        elif (maior):
            print(f"Tente novamente, o seu numero {chute_str} foi maior do que esperado")

        elif(menor):
            print(f"Tente novamente, o seu numero {chute_str} foi maior do que esperado")

        else:
            print(f"Valor inserido invalido {numero_secreto}")
    print("fim de jogo")
if __name__ == '__main__':jogo()
