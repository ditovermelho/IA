# Dependencias, se não insralado, digitar: pip install colorama

# imports
import os
import random
from random import random

from colorama import Fore

# Globais
jogadas = 0
quemJoga = 2
maxJogadas = 9
velha = [["", "", ""], ["", "", ""], ["", "", ""]]
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# funções principais


def tela():
    global velha
    global jogadas  # os.system("clear")

    print(" 0 1 2")
    for i in range(3):
        print(f"{i}: {velha[i][0]} | {velha[i][1]} | {velha[i][2]}")
        if i != 2:
            print(" -----------")
        print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)


def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input("Linha..: "))
            c = int(input("Coluna.: "))
            while velha[l][c] != " ":
                l = int(input("Linha..: "))
                c = int(input("Coluna.: "))
            velha[l][c] = "X"
            matrix[l][c] = -1
            quemJoga = 1
            jogadas += 1
        except:
            print("Jogada invalida!")
            os.system("pause")


def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga == 1 and jogadas < maxJogadas:
        l = random.randrange(0, 3)
        c = random.randrange(0, 3)
        while velha[l][c] != " ":
            l = random.randrange(0, 3)
            c = random.randrange(0, 3)
        velha[l][c] = "O"
        matrix[l][c] = 1
        quemJoga = 2
        jogadas += 1


def redefinir():
    global velha, matrix
    global jogadas
    global quemJoga
    global maxJogadas
    jogadas = 0
    quemJoga = 2
    maxJogadas = 9
    velha = [["", "", ""], ["", "", ""], ["", "", ""]]
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def verificador():
    # Principio é multiplicar uma matriz 1x3 e 3x3, e 3x3 3 3x1
    # cada multiplicação verificar se soma 3 ou -3,
    # dado que (velha e matrix) possuem valores equivalentes a: X = -1 e O = 1
    # O mesmo é feito nas diagonais: 3 ou -3
    global matrix

    # Ver cada coluna:
    for i in range(1):
        for j in range(3):
            soma = 0
            for k in range(3):
                soma = soma + matrix[k][j]
            if soma == -3:
                return "X"
            if soma == 3:
                return "O"

    # Ver cada linha:
    for i in range(3):
        for j in range(1):
            soma = 0
            for k in range(3):
                soma = soma + matrix[k][j]
            if soma == -3:
                return "X"
            if soma == 3:
                return "O"

    # Ver diagonais
    if matrix[0][0]+matrix[1][1]+matrix[2][2] == -3:
        return "X"
    if matrix[0][0]+matrix[1][1]+matrix[2][2] == 3:
        return "O"
    if matrix[0][2]+matrix[1][1]+matrix[2][0] == -3:
        return "X"
    if matrix[0][2]+matrix[1][1]+matrix[2][0] == 3:
        return "O"

    return "n"

    # Por para rodar:
    def run():
        jogarNovamente = "s"
        while jogarNovamente == "s":
            while True:
                tela()
                jogadorJoga()
                cpuJoga()

                tela()
                vit = verificador()
                if vit != "n" or jogadas >= maxJogadas:
                    break
            print(Fore.RED + "Fim de Jogo" + Fore.YELLOW)
            if vit == "X" or vit == "O":
                print("Resultado: Jogador" + vit + " venceu")
            else:
                print("Resultado: Empate")
            jogarNovamente = raw_input(
                Fore.BLUE + "Jogar Novamente? [s/n]: " + Fore.RESET)
            redefinir()


run()
