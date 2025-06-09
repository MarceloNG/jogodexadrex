import pygame
import chess

WIDTH, HEIGHT = 480, 480
SQUARE_SIZE = WIDTH // 8

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

PIECE_IMAGES = {}


def load_piece_images():
    pieces = ['r', 'n', 'b', 'q', 'k', 'p']
    for color in ['w', 'b']:
        for piece in pieces:
            name = f"{color}{piece}"
            try:
                image = pygame.image.load(f"assets/{name}.png")
                PIECE_IMAGES[name] = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
            except pygame.error:
                # Fallback to simple text rendering if images are missing
                font = pygame.font.SysFont(None, SQUARE_SIZE)
                surf = font.render(name, True, BLACK if color == 'w' else WHITE)
                PIECE_IMAGES[name] = surf


def draw_board(screen, board):
    colors = [LIGHT_BROWN, DARK_BROWN]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            pygame.draw.rect(screen, color, rect)

            piece = board.piece_at(chess.square(col, 7 - row))
            if piece:
                name = ('w' if piece.color == chess.WHITE else 'b') + piece.symbol().lower()
                image = PIECE_IMAGES.get(name)
                if image:
                    screen.blit(image, rect)
                else:
                    font = pygame.font.SysFont(None, SQUARE_SIZE)
                    text = font.render(name, True, BLACK)
                    text_rect = text.get_rect(center=rect.center)
                    screen.blit(text, text_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Jogo de Xadrez')
    load_piece_images()

    board = chess.Board()
    selected_square = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                col = x // SQUARE_SIZE
                row = 7 - (y // SQUARE_SIZE)
                clicked_square = chess.square(col, row)
                if selected_square is None:
                    if board.piece_at(clicked_square) and board.piece_at(clicked_square).color == board.turn:
                        selected_square = clicked_square
                else:
                    move = chess.Move(selected_square, clicked_square)
                    if move in board.legal_moves:
                        board.push(move)
                    selected_square = None

        draw_board(screen, board)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
