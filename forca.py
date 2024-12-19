import random


def jogo():
    imprimir()
    palavra_secreta = puxa_os_arquivo()
    lista = inicializa_palavras_acertada(palavra_secreta)

    erros = 0
    enforcou = False
    acertou = False

    print(lista)
    while not enforcou and not acertou:
        chute = entrada_do_chute()

        if chute in palavra_secreta:
            indx = 0

            for letra in palavra_secreta:
                if chute == letra:
                    lista[indx] = letra
                indx += 1
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 6
        acertou = '_' not in lista
        print(lista)

    ganhador_or_perdedor(acertou, palavra_secreta)


def imprimir():
    print("*********************************************************")
    print("         Bem vindo ao jogo da forca                      ")
    print("*********************************************************")


def puxa_os_arquivo():
     # Na linha 45, tem que colocar um arquivo txt, Exemplo: arquivo = open("Teste.txt", "r")
    arquivo = open(" ", "r")
    palavra = []

    for linha in arquivo:
        palavra.append(linha.strip())
    arquivo.close()
    numero = random.randrange(0, len(palavra))
    palavra_secreta = palavra[numero].upper()
    return palavra_secreta


def inicializa_palavras_acertada(palavra_secreta):
    return ['_' for letra in palavra_secreta]


def entrada_do_chute():
    chute = input("Forneça uma palavra:").strip().upper()
    return chute


def ganhador_or_perdedor(acertou, palavra_secreta):
    if acertou:
        print("Parabéns, você ganhou!")
        print(r"       ___________      ")
        print(r"      '._==_==_=_.'     ")
        print(r"      .-\\:      /-.    ")
        print(r"     | (|:.     |) |    ")
        print(r"      '-|:.     |-'     ")
        print(r"        \\::.    /      ")
        print(r"         '::. .'        ")
        print(r"           ) (          ")
        print(r"         _.' '._        ")
        print(r"        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print(f'A palavra era {palavra_secreta}')
        print(r"    _______________         ")
        print(r"   /               \       ")
        print(r"  /                 \      ")
        print(r"//                   \/\  ")
        print(r"\|   XXXX     XXXX   | /   ")
        print(r" |   XXXX     XXXX   |/     ")
        print(r" |   XXX       XXX   |      ")
        print(r" |                   |      ")
        print(r" \__      XXX      __/     ")
        print(r"   |\     XXX     /|       ")
        print(r"   | |           | |        ")
        print(r"   | I I I I I I I |        ")
        print(r"   |  I I I I I I  |        ")
        print(r"   \_             _/       ")
        print(r"     \_         _/         ")
        print(r"       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(r" |      (_)   ")
        print(r" |            ")
        print(r" |            ")
        print(r" |            ")

    if erros == 2:
        print(r" |      (_)   ")
        print(r" |      \     ")
        print(r" |            ")
        print(r" |            ")

    if erros == 3:
        print(r" |      (_)   ")
        print(r" |      \|    ")
        print(r" |            ")
        print(r" |            ")

    if erros == 4:
        print(r" |      (_)   ")
        print(r" |      \|/   ")
        print(r" |            ")
        print(r" |            ")

    if erros == 5:
        print(r" |      (_)   ")
        print(r" |      \|/   ")
        print(r" |       |    ")
        print(r" |            ")

    if erros == 6:
        print(r" |      (_)   ")
        print(r" |      \|/   ")
        print(r" |       |    ")
        print(r" |      /     ")

    if erros == 7:
        print(r" |      (_)   ")
        print(r" |      \|/   ")
        print(r" |       |    ")
        print(r" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == '__main__':
    jogo()
