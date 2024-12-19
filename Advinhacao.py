import random
print("*********************************************************")
print("         Bem vindo ao jogo de advinhação                 ")
print("*********************************************************")
def jogo():
    numero_secreto = random.randint(1, 100)
    total_tentivas = 4
    for rodada in range(1, total_tentivas + 1):
        chute_str = input ("Informe o numero de advinhação de 0 a 100: ")
        print("Você digitou", chute_str)
        chute_str = int(chute_str)
        if (chute_str < 1 or chute_str > 100):
            print("DEVE INFORMAR UM ACIMA DE 1 E A MENOS DE 100")
            continue

        acertou = chute_str == numero_secreto
        maior = chute_str > numero_secreto
        menor = chute_str < numero_secreto

        if(acertou):
            print("Acertoou")
            break
        elif (maior):
            print("O seu chute foi maior do que o esperado")

        elif(menor):
            print("O seu chute foi menor do que o esperado")

        else:
            print("Valor invalido")
    print("fim de jogo")
if __name__ == '__main__':jogo()
