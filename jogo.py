import pygame
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Definindo as dimensões da tela
WIDTH = 300
HEIGHT = 300
LINE_WIDTH = 5

# Definindo as posições dos marcadores
X_COLOR = RED
O_COLOR = GREEN
BG_COLOR = BLACK
LINE_COLOR = WHITE

# Criando a tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha")

# Função para desenhar as linhas do jogo
def draw_lines():
    # Linhas horizontais
    pygame.draw.line(screen, LINE_COLOR, (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (300, 200), LINE_WIDTH)
    # Linhas verticais
    pygame.draw.line(screen, LINE_COLOR, (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 300), LINE_WIDTH)

# Função para desenhar X
def draw_x(x, y):
    pygame.draw.line(screen, X_COLOR, (x * 100 + 15, y * 100 + 15), (x * 100 + 85, y * 100 + 85), LINE_WIDTH)
    pygame.draw.line(screen, X_COLOR, (x * 100 + 85, y * 100 + 15), (x * 100 + 15, y * 100 + 85), LINE_WIDTH)

# Função para desenhar O
def draw_o(x, y):
    pygame.draw.circle(screen, O_COLOR, (x * 100 + 50, y * 100 + 50), 40, LINE_WIDTH)

# Função para verificar se há um vencedor
def check_winner(board):
    # Verificando linhas
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            return row[0]
    # Verificando colunas
    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            return check[0]
    # Verificando diagonais
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]
    return 0

# Inicializando variáveis do jogo
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player = 1
game_over = False

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] // 100
            mouseY = event.pos[1] // 100

            if board[mouseY][mouseX] == 0:
                if player == 1:
                    board[mouseY][mouseX] = 1
                    player = 2
                elif player == 2:
                    board[mouseY][mouseX] = 2
                    player = 1

                winner = check_winner(board)
                if winner != 0:
                    game_over = True
                elif all(cell != 0 for row in board for cell in row):
                    game_over = True

    # Preenchendo a tela com a cor de fundo
    screen.fill(BG_COLOR)

    # Desenhando as linhas
    draw_lines()

    # Desenhando X e O
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == 1:
                draw_x(x, y)
            elif board[y][x] == 2:
                draw_o(x, y)

    pygame.display.update()
