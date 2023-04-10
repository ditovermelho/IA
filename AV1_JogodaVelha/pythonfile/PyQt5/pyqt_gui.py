""" 
Neste exemplo, o jogo da velha é criado utilizando uma classe `JogoDaVelha`, que herda de `QWidget`. 
No construtor da classe, são inicializadas as variáveis `jogador`, `ganhador` e `board`, além de criados 
os componentes visuais do jogo, como o `QLabel` que mostra o tabuleiro e os botões que representam as posições do jogo.

As ações de clicar nos botões e iniciar um novo jogo são conectadas aos respectivos métodos da classe `JogoDaVelha`. 
O método `fazMovimento` é responsável por verificar se a posição clicada é válida, fazer o movimento e verificar se 
houve um ganhador ou empate.

Por fim, a instância da classe `JogoDaVelha` é criada e a aplicação é executada com `app.exec_()`.

"""

import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
                             QVBoxLayout, QWidget)


class JogoDaVelha(QWidget):
    def __init__(self):
        super().__init__()

        self.jogador = 0
        self.ganhador = None
        self.board = self.criarBoard()

        self.label = QLabel(self)
        self.label.setFont(QFont("Arial", 20))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFixedSize(200, 200)

        self.novo_jogo_button = QPushButton("Novo Jogo")
        self.novo_jogo_button.clicked.connect(self.novo_jogo)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)

        button_layout = QHBoxLayout()
        for i in range(3):
            for j in range(3):
                button = QPushButton()
                button.setFixedSize(60, 60)
                button.clicked.connect(
                    lambda _, i=i, j=j: self.fazMovimento(i, j))
                button_layout.addWidget(button)
        self.layout.addLayout(button_layout)

        self.layout.addWidget(self.novo_jogo_button)

        self.setLayout(self.layout)

        self.show()

    def criarBoard(self):
        board = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(" ")
            board.append(row)
        return board

    def printBoard(self):
        board_str = " "
        for row in self.board:
            for val in row:
                board_str += f"{val:^3}"
            board_str += "\n"
        self.label.setText(board_str)

    def fazMovimento(self, i, j):
        if self.ganhador:
            return

        if self.board[i][j]:
            return

        if self.jogador == 0:
            self.board[i][j] = "X"
        else:
            self.board[i][j] = "O"
        self.jogador = (self.jogador + 1) % 2

        self.printBoard()

        self.ganhador = self.verificaGanhador()
        if self.ganhador:
            if self.ganhador == "X" or self.ganhador == "O":
                print(f"O resultado foi vitoria de {self.ganhador}!")
            else:
                print(f"O resultado foi {self.ganhador}!")
            print("-----------------------------")

    def verificaGanhador(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] and self.board[i][0]:
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i]:
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        for row in self.board:
            for val in row:
                if not val:
                    return None

        return "Empate"

    def novo_jogo(self):
        self.board = self.criarBoard()
        self.jogador = 0
        self.ganhador = None
        self.printBoard()


"""
Não esta funcionado
"""

app = QApplication(sys.argv)
jogo = JogoDaVelha()
sys.exit(app.exec_())
