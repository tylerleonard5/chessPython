import pygame
import chessEngine

WIDTH = HEIGHT = 512

MAX_FPS = 15

images = {}

def loadImages():
    pieces = ['wp', 'bp', 'bR', 'wR', 'bN', 'wN', 'bB', 'wB', 'bQ', 'wQ', 'bK', 'wK']
    for piece in pieces:
        images[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"), ((WIDTH//8), (WIDTH//8)))



def drawSquares(screen):
    
    for i in range(8):
        if (i % 2 == 0):
            createEvenRow(screen, i)
        if (i % 2 == 1):
            createOddRow(screen, i)


def createEvenRow(screen, count):
    for i in [1, 3, 5, 7]:
        
        pygame.draw.rect(screen, 'gray', pygame.Rect(i * (WIDTH // 8), count * ((WIDTH // 8)), WIDTH//8, WIDTH//8))

def createOddRow(screen, count):
    for i in [0, 2, 4, 6]:
        pygame.draw.rect(screen, 'gray', pygame.Rect(i * (WIDTH // 8), count * ((WIDTH // 8)), WIDTH//8, WIDTH//8))

def drawPieces(screen, board):
    for r in range(8):
        for c in range(8):
            piece =  board[r][c]
            if piece != '--':
                screen.blit(images[piece], pygame.Rect(c * (WIDTH // 8), r * ((WIDTH // 8)), WIDTH//8, WIDTH//8))
            



def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock  = pygame.time.Clock()
    screen.fill('white')
    
    loadImages()
    gs = chessEngine.State()

    running = True
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

        drawSquares(screen)
        drawPieces(screen, gs.board)
        clock.tick(MAX_FPS)
        pygame.display.flip()



if __name__ == "__main__":
    main()
    