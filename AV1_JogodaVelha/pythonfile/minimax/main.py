import os

from colorama import Back, Fore, Style
from func_jogo_da_velha import (criarBoard, fazMovimento, getInputValido,
                                printBoard, verificaGanhador,
                                verificaMovimento)
from minimax import movimentoIA


def novoJogo():
    jogador = 0
    board = criarBoard()
    ganhador = verificaGanhador(board)
    return jogador, board, ganhador


jogador, board, ganhador = novoJogo()
jogarNovamente = "s"
while jogarNovamente == "s":
    while not ganhador:
        printBoard(board)
        if jogador == 0:
            i, j = movimentoIA(board, jogador)
            # i = getInputValido("Digite a Linha.: ")
            # j = getInputValido("Digite a Coluna: ")
        else:
            i, j = movimentoIA(board, jogador)
            # i = getInputValido("Digite a Linha.: ")
            # j = getInputValido("Digite a Coluna: ")

        if verificaMovimento(board, i, j):
            fazMovimento(board, i, j, jogador)
            jogador = (jogador + 1) % 2
        else:
            print("A posição informada já está ocupada!")
            os.system("pause")

        ganhador = verificaGanhador(board)
    printBoard(board)
    print("\n")
    if ganhador == "X" or ganhador == "O":
        print(f"O resultado foi vitoria de {ganhador}!")
    else:
        print(f"O resultado foi {ganhador}!")
    print("-----------------------------")
    jogarNovamente = input(
        Fore.BLUE + "Jogar Novamente? [s/n]: " + Fore.RESET)
    if jogarNovamente == "s":
        jogador, board, ganhador = novoJogo()
