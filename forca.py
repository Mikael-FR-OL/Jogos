import random


def jogo():
    imprimir()
    palavra_secreta = puxa_os_arquivo()
    lista = inicializa_palavras_acertada(palavra_secreta)

    erros = 0
    enforcou = False
    acertou = False

    print(len(palavra_secreta))
    print(lista)
    while (not enforcou and not acertou):

        chute = entrada_do_chute()

        if (chute in palavra_secreta):
            indx = 0

            for letra in palavra_secreta:
                if chute == letra:
                    lista[indx] = letra
                indx += 1
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 6
        acertou = "_" not in lista
        print(lista)

    ganhador_or_perdedor(acertou, palavra_secreta)


def imprimir():
    print("*********************************************************")
    print("         Bem vindo ao jogo da forca                      ")
    print("*********************************************************")


def puxa_os_arquivo():
    arquivo = open("teste.txt", "r")
    palavra = []

    for linha in arquivo:
        linha.strip()
        palavra.append(linha)
    arquivo.close()
    numero = random.randrange(0, len(palavra))
    palavra_secreta = palavra[numero].upper()
    return palavra_secreta


def inicializa_palavras_acertada(palavra_secreta):
    return ["_" for list in palavra_secreta]


def entrada_do_chute():
    chute = input("Forneça uma palavra: ")
    chute = chute.strip().upper()
    return chute


def ganhador_or_perdedor(acertou, palavra_secreta):
    if (acertou):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == '__main__':
    jogo()
