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
    for i in range(8):
        
        if(i%2 == 1):
            pygame.draw.rect(screen, 'gray', pygame.Rect(i * (WIDTH // 8), count * ((WIDTH // 8)), WIDTH//8, WIDTH//8))
        else: 
            pygame.draw.rect(screen, 'white', pygame.Rect(i * (WIDTH // 8), count * ((WIDTH // 8)), WIDTH//8, WIDTH//8))

def createOddRow(screen, count):
    for i in range(8):
        if(i % 2 == 0):
            pygame.draw.rect(screen, 'gray', pygame.Rect(i * (WIDTH // 8), count * ((WIDTH // 8)), WIDTH//8, WIDTH//8))
        else: 
            pygame.draw.rect(screen, 'white', pygame.Rect(i * (WIDTH // 8), count * ((WIDTH // 8)), WIDTH//8, WIDTH//8))

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
    sqSelected = () #Keeps track of selected square
    playerClicks = [] #keep track of player clicks (two tuples: [(x1,y1). (x2,y2)])
    while running:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                col = location[0] // (WIDTH // 8)
                row = location[1] // (WIDTH // 8)
                if sqSelected == (row,col):
                    sqSelected = ()
                    playerClicks = []
                else:
                    sqSelected = (row, col)
                    print(sqSelected)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    move = chessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    gs.makeMove(move)
                    sqSelected = ()
                    playerClicks = []


        drawSquares(screen)
        drawPieces(screen, gs.board)
        clock.tick(MAX_FPS)
        pygame.display.flip()



if __name__ == "__main__":
    main()
    