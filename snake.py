import pygame,sys,random,time
# Screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# snake and positions
snake_block = 20
x1= SCREEN_WIDTH/2
y1= SCREEN_HEIGHT/2
snake_speed = 15

pygame.init()

clock = pygame.time.Clock()

# set the screen
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#titles

pygame.display.set_caption("Snake Game")



x1_change =0
y1_change =0


#game state
game_active = True

# you lost message
font_style =pygame.font.Font(None,40)

# [ToDo] center the message
# the x- the half the length of the message
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH/2, SCREEN_HEIGHT/2])

# quit the game
def quit_game():
    pygame.quit()
    sys.exit()

# manage the snake
def snake_manag(snake_block,snake_list):
    for i in snake_list:
        pygame.draw.rect(screen,"Blue",[i[0],i[1],snake_block,snake_block])


def bit_tail():
    head = snake_list[0]
    for i in snake_list[1:]:
        if head[0]==i[0] and head[1]==i[1]:
            return True
            


# to avoid going left when the snake is forwarding
verHor = [False,False]

score_inc =0
# score


    
foodx_list= list(range(0,800,snake_block))
foody_list= list(range(0,600,snake_block))

rand_x = random.randint(0,len(foodx_list)-1)
rand_y = random.randint(0,len(foody_list)-1)
foodx= foodx_list[rand_x]
foody= foody_list[rand_y] 

# create a x_Y if the food and snake are at the same position at the start of the game
while foodx == x1 and foody ==y1:
    foodx= foodx_list[rand_x]
    foody= foody_list[rand_y] 


snake_list=[]
snake_length  =1


while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if verHor[0]:
                    break
                x1_change=0
                y1_change = -snake_block
                verHor[0]=True
                verHor[1]=False
                
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if verHor[0]:
                    break
                x1_change=0
                y1_change =snake_block
                verHor[0]=True 
                verHor[1]=False 
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if verHor[1]:
                    break
                x1_change =-snake_block
                y1_change=0
                verHor[1]=True 
                verHor[0]=False 
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if verHor[1]:
                    break
                x1_change =snake_block
                y1_change=0
                verHor[1]=True 
                verHor[0]=False 

         
    text ="Score : {0}".format(score_inc)
    font_score = pygame.font.Font(None,30)
    score = font_score.render(text,False,"Pink")
    score_rect = score.get_rect(topleft=(0,0))
    
    

    if x1 >= SCREEN_WIDTH or x1 < 0 or y1 >= SCREEN_HEIGHT or y1 < 0:
        game_active = False
    x1 += x1_change
    y1 += y1_change

    screen.fill("white")
    #pygame.draw.rect(screen,"Blue",[x1,y1,snake_block,snake_block])
    screen.blit(score,score_rect)
    pygame.draw.rect(screen,"Red",[foodx,foody,snake_block,snake_block])

    snake_head =[]

    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)

    snake_manag(snake_block,snake_list)
    if len(snake_list) > snake_length:
            del snake_list[0]
    pygame.display.update()
    if bit_tail():
        game_active = False

    # collision food snake
    if foodx == x1 and foody ==y1:
        rand_x = random.randint(0,len(foodx_list)-1)
        rand_y = random.randint(0,len(foody_list)-1)
        foodx= foodx_list[rand_x]
        foody= foody_list[rand_y] 
        snake_length +=1
        score_inc +=1
        
    

    
    if not game_active:
        message("You lost","Red")
        pygame.display.update()
        time.sleep(1)
        quit_game()
        
    
    pygame.display.update()
    clock.tick(snake_speed)
    