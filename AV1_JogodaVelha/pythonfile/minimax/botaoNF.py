# O botão não funciona

# Importes
import sys

import pygame
from func_jogo_da_velha import (criarBoard, fazMovimento, getInputValido,
                                printBoard, verificaGanhador,
                                verificaMovimento)
from minimax import movimentoIA

pygame.font.init()

# Definir constantes
height = 600
width = 600
size = 600/3
COR_BOTAO = (255, 200, 255)
COR_BOTAO_HOVER = (200, 200, 200)
POS_X_BOTAO = width/2 - 120
POS_Y_BOTAO = height/2 + 50
LARGURA_BOTAO = 200
ALTURA_BOTAO = 50


# Definir a fonte
font = pygame.font.SysFont("comicsans", 100)
font2 = pygame.font.SysFont('Arial', 24)

# Definir a janela
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo da Velha")


def draw_board(win, board):
    global height
    global width
    global size
    global font

    for i in range(1, 3):
        pygame.draw.line(win, (0, 0, 0), (0, i * size), (width, i * size), 3)
        pygame.draw.line(win, (0, 0, 0), (i * size, 0), (i * size, height), 3)

    for i in range(3):
        for j in range(3):

            x = j * size
            y = i * size

            text = font.render(board[i][j], 1, (128, 0, 0))
            win.blit(text, (x + 75, y + 75))


def redraw_window(win, board):
    win.fill((255, 255, 255))
    draw_board(win, board)


def new_jogo():
    board = criarBoard()
    jogador = 0  # Jogador 1
    ganhador = verificaGanhador(board)
    return board, jogador, ganhador


def jogo(jogar_novamente, win, jogador, board, ganhador):
    while not jogar_novamente:
        redraw_window(win, board)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        while not ganhador:
            printBoard(board)
            if jogador == 0:
                jogou = False
                while not jogou:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONUP:
                            pos = pygame.mouse.get_pos()
                            i = int(pos[1]/200)
                            j = int(pos[0]/200)
                            jogou = True
            else:
                i, j = movimentoIA(board, jogador)

            if verificaMovimento(board, i, j):
                fazMovimento(board, i, j, jogador)
                jogador = (jogador + 1) % 2

            ganhador = verificaGanhador(board)
            redraw_window(win, board)
            pygame.display.update()


def jogardenovo(ganhador):
    win.fill((255, 255, 255))
    if ganhador == "X" or ganhador == "O":
        mensagem = font2.render(
            f"O resultado foi vitoria de {ganhador}!", 1, (128, 0, 0))
        win.blit(mensagem, (width/2 - mensagem.get_width() /
                            2, height/2 - mensagem.get_height()/2))
        mensagem2 = font2.render("Jogar Novamente?", 1, (128, 0, 0))
        win.blit(mensagem2, (width/2 - mensagem.get_width() /
                             2, height/2 - mensagem.get_height()/2 + 20))

        # Desenhar botão
        botao_rect = pygame.Rect(
            POS_X_BOTAO, POS_Y_BOTAO, LARGURA_BOTAO, ALTURA_BOTAO)
        botao_rect.center = [50, 50]
        if botao_rect.collidepoint(pygame.mouse.get_pos()):
            main()
            pygame.draw.rect(win, COR_BOTAO, botao_rect)

        else:
            pygame.draw.rect(win, COR_BOTAO, botao_rect)

        pygame.draw.rect(win, COR_BOTAO, botao_rect)
        texto_botao = font2.render("Yes", 1, (0, 0, 0))
        win.blit(texto_botao, (POS_X_BOTAO, POS_Y_BOTAO))
    else:
        mensagem = font2.render(
            f"O resultado foi {ganhador}!", 1, (128, 0, 0))
        win.blit(mensagem, (width/2 - mensagem.get_width() /
                            2, height/2 - mensagem.get_height()/2))
        mensagem2 = font2.render("Jogar Novamente?", 1, (128, 0, 0))
        win.blit(mensagem2, (width/2 - mensagem.get_width() /
                             2 + 20, height/2 - mensagem.get_height()/2 + 20))
        # Desenhar botão
        botao_rect = pygame.Rect(
            POS_X_BOTAO, POS_Y_BOTAO, LARGURA_BOTAO, ALTURA_BOTAO)
        if botao_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(win, COR_BOTAO, botao_rect)
            if pygame.mouse.get_pressed():
                main()
        pygame.draw.rect(win, COR_BOTAO, botao_rect)
        texto_botao = font2.render("Yes", 1, (0, 0, 0))
        win.blit(texto_botao, (POS_X_BOTAO, POS_Y_BOTAO))

        botao_rect2 = pygame.Rect(
            POS_X_BOTAO+60, POS_Y_BOTAO, LARGURA_BOTAO, ALTURA_BOTAO)
        if botao_rect2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(win, COR_BOTAO, botao_rect2)
            if pygame.mouse.get_pressed():
                pygame.quit()
                sys.exit()
        pygame.draw.rect(win, COR_BOTAO, botao_rect2)
        texto_botao2 = font2.render("NOT", 1, (0, 0, 0))
        win.blit(texto_botao2, (POS_X_BOTAO+60, POS_Y_BOTAO))
        pygame.display.flip()


def main():
    global height
    global width
    global font
    global size
    global win

    board, jogador, ganhador = new_jogo()
    jogar_novamente = False

    # Daqui para baixo não funciona

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        jogo(jogar_novamente, win, jogador, board, ganhador)
        jogardenovo(ganhador)

        pygame.display.flip()


main()
