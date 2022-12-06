import pygame
def player_text():
    global player_turn
    if player == 'A':
        player_turn = font.render('Player 1, its your turn',True,white)
    if player == 'B':
        player_turn = font.render('Player 2, its your turn',True,white)
def get_mouse_position():
    global mouseX,mouseY    
    mouseX,mouseY = pygame.mouse.get_pos()
def cross_executor():
    if player == 'A':
        if mouseX >= 0 and mouseX < 212 and mouseY >= 100 and mouseY <257 and board[0] == ' ':
            board[0] = 'X'
            return True
        if mouseX >= 224 and mouseX < 422 and mouseY >= 100 and mouseY <258 and board[1] == ' ':
            board[1] = 'X'
            return True
        if mouseX >= 433 and mouseX < 640 and mouseY >= 100 and mouseY <259 and board[2] == ' ':
            board[2] = 'X'
            return True
        if mouseX >= 0 and mouseX < 213 and mouseY >= 267 and mouseY <437 and board[3] == ' ':
            board[3] = 'X'
            return True
        if mouseX >= 224 and mouseX < 421 and mouseY >= 269 and mouseY <439 and board[4] == ' ':
            board[4] = 'X'
            return True
        if mouseX >= 433 and mouseX < 640 and mouseY >= 269 and mouseY <439 and board[5] == ' ':
            board[5] = 'X'
            return True
        if mouseX >= 0 and mouseX < 213 and mouseY >= 449 and mouseY <580 and board[6] == ' ':
            board[6] = 'X'
            return True
        if mouseX >= 225 and mouseX < 421 and mouseY >= 450 and mouseY <580 and board[7] == ' ':
            board[7] = 'X'
            return True
        if mouseX >= 433 and mouseX < 640 and mouseY >= 451 and mouseY <580 and board[8] == ' ':
            board[8] = 'X'
            return True
    if player == 'B':
        if mouseX >= 0 and mouseX < 212 and mouseY >= 100 and mouseY <257 and board[0] == ' ':
            board[0] = 'O'
            return True
        if mouseX >= 224 and mouseX < 422 and mouseY >= 100 and mouseY <258 and board[1] == ' ':
            board[1] = 'O'
            return True
        if mouseX >= 433 and mouseX < 640 and mouseY >= 100 and mouseY <259 and board[2] == ' ':
            board[2] = 'O'
            return True
        if mouseX >= 0 and mouseX < 213 and mouseY >= 267 and mouseY <437 and board[3] == ' ':
            board[3] = 'O'
            return True
        if mouseX >= 224 and mouseX < 421 and mouseY >= 269 and mouseY <439 and board[4] == ' ':
            board[4] = 'O'
            return True
        if mouseX >= 433 and mouseX < 640 and mouseY >= 269 and mouseY <439 and board[5] == ' ':
            board[5] = 'O'
            return True
        if mouseX >= 0 and mouseX < 213 and mouseY >= 449 and mouseY <580 and board[6] == ' ':
            board[6] = 'O'
            return True
        if mouseX >= 225 and mouseX < 421 and mouseY >= 450 and mouseY <580 and board[7] == ' ':
            board[7] = 'O'
            return True
        if mouseX >= 433 and mouseX < 640 and mouseY >= 451 and mouseY <580 and board[8] == ' ':
            board[8] = 'O'
            return True
    else: 
        return False
def board_redraw():
    if board[0] == 'X':
        window.blit(cross,(22,123))
    if board[1] == 'X':
        window.blit(cross,(239,121))
    if board[2] == 'X':
        window.blit(cross,(449,122))
    if board[3] == 'X':
        window.blit(cross,(24,303))
    if board[4] == 'X':
        window.blit(cross,(238,302))
    if board[5] == 'X':
        window.blit(cross,(452,309))
    if board[6] == 'X':
        window.blit(cross,(26,461))
    if board[7] == 'X':
        window.blit(cross,(236,460))
    if board[8] == 'X':
        window.blit(cross,(447,456))
    if board[0] == 'O':
        window.blit(circle,(38,123))
    if board[1] == 'O':
        window.blit(circle,(254,118))
    if board[2] == 'O':
        window.blit(circle,(465,120))
    if board[3] == 'O':
        window.blit(circle,(36,295))
    if board[4] == 'O':
        window.blit(circle,(253,297))
    if board[5] == 'O':
        window.blit(circle,(466,297))
    if board[6] == 'O':
        window.blit(circle,(35,455))
    if board[7] == 'O':
        window.blit(circle,(245,456))
    if board[8] == 'O':
        window.blit(circle,(468,454))
def redrawGameWindow():
    player_text()
    window.blit(player_turn,(0,0))
    window.blit(tic_diagram,(0,100))
    board_redraw()
    pygame.display.update()
    window.fill(black)
def win_window():
    window.fill(black)
    if player == 'B':
        winner = font.render('Player 1 you won',True,white)
    else:
        winner = font.render('Player2 you won',True,white)
    window.blit(winner,(0,0))
    pygame.display.update()
def draw_window():
    window.fill(black)
    draw_text = font.render('The Game ended in a draw',True,white)
    window.blit(draw_text,(0,0))    
    pygame.display.update()
def game_win_check():   
    Game = False
    if(board[0] == board[1] and board[1] == board[2] and board[0] != ' '):    
        Game = True    
    elif(board[3] == board[4] and board[4] == board[5] and board[3] != ' '):    
        Game = True    
    elif(board[6] == board[7] and board[7] == board[8] and board[6] != ' '):    
        Game = True      
    elif(board[0] == board[3] and board[3] == board[6] and board[0] != ' '):    
        Game = True    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = True    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game= True        
    elif(board[0] == board[4] and board[4] == board[8] and board[4] != ' '):    
        Game = True    
    elif(board[2] == board[4] and board[4] == board[6] and board[4] != ' '):    
        Game= True
    if Game == True:
        return True
    else:
        return False

        
pygame.init()
window = pygame.display.set_mode((640,580))
pygame.display.set_caption("Tic Tac Toe")

black = (0,0,0)
white = (255,255,255)
font = pygame.font.Font('data/fonts/font.otf', 32)
font = pygame.font.Font('data/fonts/font.otf', 32)
player_turn = font.render('Player 1, its your turn',True,white)

clock = pygame.time.Clock()
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
mouseX = 0
mouseY = 0
tic_diagram = pygame.image.load('Data/Sprites/tic.png')
cross = pygame.image.load('Data/Sprites/cross.png')
circle = pygame.image.load('Data/Sprites/circle.png')
run = True
player = 'A'
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        if cross_executor():
            if player == 'A':
                player = 'B'
            else:
                player = 'A'
    if game_win_check():
        run2 = True
        while run2 == True:
            pygame.time.delay(100)
            win_window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run2 = False
                    run = False
    if ' ' not in board and run != False:
        run2 = True
        while run2 == True:
            pygame.time.delay(100)
            draw_window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run2 = False
                    run = False
    get_mouse_position()
    redrawGameWindow()
print(board)
pygame.quit()