def carregar_board():
    arquivo = open('./pythonfile/minimax/board.txt', "r")
    conteudo = arquivo.read()
    arquivo.close()
    return conteudo


def salvar_conteudo(conteudo):
    arquivo = open("./pythonfile/minimax/board.txt", "a")
    arquivo.write(conteudo)
    arquivo.close()


score = {
    "X": 0,
    "O": 1
}


def converter(board):
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                matrix[i][j] = 1
            elif board[i][j] == "X":
                matrix[i][j] = 0
            else:
                matrix[i][j] = 0
    return matrix


def converter_string(board):
    matrix = converter(board)
    string = ','.join(map(str, matrix))
    return string
