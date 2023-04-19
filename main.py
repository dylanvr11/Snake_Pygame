import pygame, sys, time, random
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")
fps = pygame.time.Clock()
font = pygame.font.Font(None, 30)
BG = pygame.image.load("assets/Background.png")


def food():
    random_pos = random.randint(0,49)*10
    food_pos = [random_pos, random_pos]
    return food_pos


def snake():

    snake_pos = [100, 50]
    snake_body = [[100,50],[90,50],[80,50]]
    change = "RIGHT"
    run = True
    food_pos = food()
    score = 0

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change = "RIGHT"
                if event.key == pygame.K_LEFT:
                    change = "LEFT"
                if event.key == pygame.K_UP:
                    change = "UP"
                if event.key == pygame.K_DOWN:
                    change = "DOWN"
        if change == "RIGHT":
            snake_pos[0] += 10
        if change == "LEFT":
            snake_pos[0] -= 10
        if change == "UP":
            snake_pos[1] -= 10
        if change == "DOWN":
            snake_pos[1] += 10

        snake_body.insert(0, list(snake_pos))

        if snake_pos == food_pos:
            food_pos = food()
            score += 1
            print(score)
        else:
            snake_body.pop()
        
        head = snake_body[-1]
        for i in range(len(snake_body) - 1): 
            part = snake_body[i]
            if head[0] == part[0] and head[1] == part[1]:
                run = False
                print("YOU LOSE")

        SCREEN.fill((0,0,0))

        for pos in snake_body:
            pygame.draw.rect(SCREEN,(200,200,200), pygame.Rect(pos[0], pos[1], 10, 10))
        
        pygame.draw.rect(SCREEN,(169,6,6), pygame.Rect(food_pos[0], food_pos[1], 10, 10))
        
        text = font.render(str(score),0,(200,60,80))
        SCREEN.blit(text, (1260,20))

        if score < 10:
            fps.tick(10)
        if score >= 10:
            fps.tick(20)

        if snake_pos[0] <= 0 or snake_pos[0] >= 1280:
            run = False
            print("YOU LOSE")
        if snake_pos[1] <= 0 or snake_pos[1] >= 720:
            run = False
            print("YOU LOSE")

        pygame.display.flip()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    #play()
                    snake()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()