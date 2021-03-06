import pygame

# to get a gui of the board being solved, simply uncomment the lines of code bellow.

# input sudoku board here. place a '0' for empty cells.
board =  [
    [0,2,0,0,0,0,0,0,0],
    [0,0,0,6,0,0,0,0,3],
    [0,7,4,0,8,0,0,0,0],
    [0,0,0,0,0,3,0,0,2],
    [0,8,0,0,4,0,0,1,0],
    [6,0,0,5,0,0,0,0,0],
    [0,0,0,0,1,0,7,8,0],
    [5,0,0,0,0,9,0,0,0],
    [0,0,0,0,0,0,0,4,0]

]
rectCenter  =[
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]
textobj  =[
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
    ]



def drawGrid():
    blockSize = 56
    for i in range(len(board)):
        for j in range(len(board)):
            rect = pygame.Rect(i * blockSize, j* blockSize, blockSize,blockSize)
            rectCenter[i].append(rect)
            if i % 3 == 0 and i != 0:
                pygame.draw.lines(screen, (0,0,0), True, (rect.topleft,rect.bottomleft), 5)
            if j % 3 == 0 and j != 0:
                pygame.draw.lines(screen, (0,0,0), True, (rect.topright,rect.topleft), 5)
            pygame.draw.rect(screen,(0,0,0),rect,1)
    populate()
    return rectCenter

def populate():
    for i in range(len(board)):
        for j in range(len(board)):
            font = pygame.font.SysFont(None, 50)
            text = font.render(str(board[j][i]), True, (25,2,200))
            textobj[i].append(text.get_rect())
            textobj[i][j].center = rectCenter[i][j].center
            screen.blit(text, textobj[i][j])
    return textobj

          



def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0: 
            print("- - - - - - - - - - - - ")
        for j in range (len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else: 
                print(str(bo[i][j]) + " ", end="") 


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)  ## row, column
    return None

def valid(bo, num, pos):

    #check row 
    for i in range(9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    #check column 
    for j in range(9):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False
    
    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def solver(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo,i,(row, col)):
            board[row][col] = i
#             screen.fill((0,255,0), textobj[col][row])
#             font = pygame.font.SysFont(None, 50)
#             text = font.render(str(i), True, (25,2,200))
#             screen.blit(text, textobj[col][row]) 
#             pygame.display.update()
            if solver(bo):
                return True
            bo[row][col] = 0
    return False    
   
# pygame.init()
# screen = pygame.display.set_mode([500, 500])
# screen.fill((255, 255, 255))
# drawGrid()
# populate()
print_board(board)
solver(board)
print("=============================================================")
print_board(board)
# drawGrid()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.display.update()
# pygame.quit()
