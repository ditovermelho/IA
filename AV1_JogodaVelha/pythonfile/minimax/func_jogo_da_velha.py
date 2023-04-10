# Definição das funções do jogo da velha
# Importes
import os

from colorama import Back, Fore, Style

branco = " "
token = ["X", "O"]


def criarBoard():
    board = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco]
    ]
    return board


def printBoard(board):
    os.system("cls")
    print(Fore.CYAN + "----Jogo da Velha----" + Fore.RESET)
    print("    0     1     2")
    for i in range(3):
        print(f"{i}:  " + "  |  ".join(board[i]))
        if i != 2:
            print("    -------------")


def getInputValido(mensagem):
    try:
        n = int(input(mensagem))
        if n >= 0 and n <= 2:
            return n
        else:
            print("Número precisa estar entre 0 e 2")
            return getInputValido(mensagem)
    except:
        print("Número não é valido")
        return getInputValido(mensagem)


def verificaMovimento(board, i, j):
    if board[i][j] == branco:
        return True
    else:
        return False


def fazMovimento(board, i, j, jogador):
    board[i][j] = token[jogador]


def verificaGanhador(board):
    # Ver cada linha:
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != branco:
            return board[i][0]

    # Ver cada coluna:
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != branco:
            return board[0][i]

    # Ver diagonais:
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != branco:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != branco:
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if board[i][j] == branco:
                return False

    return "Empate"
