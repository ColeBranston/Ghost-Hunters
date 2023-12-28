
#Importing all libraries
import pygame, sys, math, time, random
from pygame.locals import *

#Initializing the screen
pygame.init()
fps = 30
fpsclock = pygame.time.Clock()

#set the size of the display window
window_size = pygame.display.set_mode((800, 600))


#change the caption of the display window
pygame.display.set_caption("Ghost Hunters")

icon = pygame.image.load("IconFolder/Icon.png")
icon = pygame.transform.scale(icon, (32,32))

pygame.display.set_icon(icon)

#Initializing variables
if True:
    mcX = 350
    mcY = 250
    mc_centerX = mcX+ 50
    mc_centerY = mcY +50
    bkX = -250
    bkY = -300
    movement = "None"
    counter1 = 0
    counter2 = 0
    counter3 = 0
    start_screen_counter = 0
    ghost_counter = 0
    OnSwitch = 1
    ghost_list = []
    background_moving = True
    angle = 300
    click = (0,0)
    hover = (0,0)
    points = 0
    ghost_ros = 1
    clock = pygame.time.Clock()
    minutes = 0
    seconds = 0
    milliseconds = 0
    death_variable = False
    restart = True
    start = True
    hit = False
    controlstoggle = False
    choice = True

#Loading images animations frames
if True:
    Forward1 = pygame.image.load("Main Character/mc_Forward1.png")
    Forward2 = pygame.image.load("Main Character/mc_Forward2.png")
    Forward3 = pygame.image.load("Main Character/mc_Forward3.png")
    Forward4 = pygame.image.load("Main Character/mc_Forward4.png")
    Forward1 = pygame.transform.scale(Forward1, (100,100))
    Forward2 = pygame.transform.scale(Forward2, (100,100))
    Forward3 = pygame.transform.scale(Forward3, (100,100))
    Forward4 = pygame.transform.scale(Forward4, (100,100))
    forward_Animation = [Forward1, Forward2, Forward3, Forward4]
    Backword1 = pygame.image.load("Main Character/mc_Backword1.png")
    Backword2 = pygame.image.load("Main Character/mc_Backword2.png")
    Backword3 = pygame.image.load("Main Character/mc_Backword3.png")
    Backword4 = pygame.image.load("Main Character/mc_Backword4.png")
    Backword1  = pygame.transform.scale(Backword1, (100,100))
    Backword2  = pygame.transform.scale(Backword2, (100,100))
    Backword3  = pygame.transform.scale(Backword3, (100,100))
    Backword4  = pygame.transform.scale(Backword4, (100,100))
    backword_Animation = [Backword1, Backword2, Backword3, Backword4]
    Right1 = pygame.image.load("Main Character/mc_Right1.png")
    Right2 = pygame.image.load("Main Character/mc_Right2.png")
    Right3 = pygame.image.load("Main Character/mc_Right3.png")
    Right4 = pygame.image.load("Main Character/mc_Right4.png")
    Right1 = pygame.transform.scale(Right1, (100,100))
    Right2 = pygame.transform.scale(Right2, (100,100))
    Right3 = pygame.transform.scale(Right3, (100,100))
    Right4 = pygame.transform.scale(Right4, (100,100))
    right_Animation = [Right1, Right2, Right3, Right4]
    Left1 = pygame.image.load("Main Character/mc_Left1.png")
    Left2 = pygame.image.load("Main Character/mc_Left2.png")
    Left3 = pygame.image.load("Main Character/mc_Left3.png")
    Left4 = pygame.image.load("Main Character/mc_Left4.png")
    Left1 = pygame.transform.scale(Left1, (100,100))
    Left2 = pygame.transform.scale(Left2, (100,100))
    Left3 = pygame.transform.scale(Left3, (100,100))
    Left4 = pygame.transform.scale(Left4, (100,100))
    left_Animation = [Left1, Left2, Left3, Left4]
    Rest1 = pygame.image.load("Main Character/mc_RestingState1.png")
    Rest2 = pygame.image.load("Main Character/mc_RestingState2.png")
    Rest1 = pygame.transform.scale(Rest1, (100,100))
    Rest2 = pygame.transform.scale(Rest2, (100,100))
    rest_Animation = [Rest1, Rest2]
    main_3connector = pygame.image.load("Rooms/Lit/3room_connector.png")
    main_3connector = pygame.transform.scale(main_3connector, (1250, 1250))
    background = main_3connector
    flashlight = pygame.image.load("Main Character/flashlight.png")
    flashlight = pygame.transform.scale(flashlight, (2000, 2000))
    ghosts_hover1 = pygame.image.load("Enemy_Ghost/Ghost1.png")
    ghosts_hover2 = pygame.image.load("Enemy_Ghost/Ghost2.png")
    ghosts_hover3 = pygame.image.load("Enemy_Ghost/Ghost3.png")
    ghosts_hover4 = pygame.image.load("Enemy_Ghost/Ghost4.png")
    ghosts_hover1 = pygame.transform.scale(ghosts_hover1, (80, 80))
    ghosts_hover2 = pygame.transform.scale(ghosts_hover2, (80, 80))
    ghosts_hover3 = pygame.transform.scale(ghosts_hover3, (80, 80))
    ghosts_hover4 = pygame.transform.scale(ghosts_hover4, (80, 80))
    Ghost_Death1 = pygame.image.load("Enemy_Ghost/Ghost_Death1.png")
    Ghost_Death2 = pygame.image.load("Enemy_Ghost/Ghost_Death2.png")
    Ghost_Death3 = pygame.image.load("Enemy_Ghost/Ghost_Death3.png")
    Ghost_Death4 = pygame.image.load("Enemy_Ghost/Ghost_Death4.png")
    Ghost_Death5 = pygame.image.load("Enemy_Ghost/Ghost_Death5.png")
    Ghost_Death6 = pygame.image.load("Enemy_Ghost/Ghost_Death6.png")
    Ghost_Death7 = pygame.image.load("Enemy_Ghost/Ghost_Death7.png")
    Ghost_Death8 = pygame.image.load("Enemy_Ghost/Ghost_Death8.png")
    Ghost_Death9 = pygame.image.load("Enemy_Ghost/Ghost_Death9.png")
    Ghost_Death10 = pygame.image.load("Enemy_Ghost/Ghost_Death10.png")
    Ghost_Death11= pygame.image.load("Enemy_Ghost/Ghost_Death11.png")
    Ghost_Death12= pygame.image.load("Enemy_Ghost/Ghost_Death11.png")
    Ghost_Death1 = pygame.transform.scale(Ghost_Death1, (80, 80))
    Ghost_Death2 = pygame.transform.scale(Ghost_Death2, (80, 80))
    Ghost_Death3 = pygame.transform.scale(Ghost_Death3, (80, 80))
    Ghost_Death4 = pygame.transform.scale(Ghost_Death4, (80, 80))
    Ghost_Death5 = pygame.transform.scale(Ghost_Death5, (80, 80))
    Ghost_Death6 = pygame.transform.scale(Ghost_Death6, (80, 80))
    Ghost_Death7 = pygame.transform.scale(Ghost_Death7, (80, 80))
    Ghost_Death8 = pygame.transform.scale(Ghost_Death8, (80, 80))
    Ghost_Death9 = pygame.transform.scale(Ghost_Death9, (80, 80))
    Ghost_Death10 = pygame.transform.scale(Ghost_Death10, (80, 80))
    Ghost_Death11= pygame.transform.scale(Ghost_Death11, (80, 80))
    Ghost_Death12= pygame.transform.scale(Ghost_Death12, (80, 80))
    game_font = pygame.font.Font("pixelFont.ttf", 32)
    game_font2 = pygame.font.Font("pixelFont.ttf", 50)
    game_font3 = pygame.font.Font("pixelFont.ttf", 20)
    death_screen = pygame.image.load("DeathScreen.jpg")
    death_screen = pygame.transform.scale(death_screen, (800, 600))
    start_screen1 = pygame.image.load("StartScreen/StartScreen1.png")
    start_screen2 = pygame.image.load("StartScreen/StartScreen2.png")
    start_screen3 = pygame.image.load("StartScreen/StartScreen3.png")
    start_screen4 = pygame.image.load("StartScreen/StartScreen4.png")
    start_screen1 = pygame.transform.scale(start_screen1, (800, 600))
    start_screen2 = pygame.transform.scale(start_screen2, (800, 600))
    start_screen3 = pygame.transform.scale(start_screen3, (800, 600))
    start_screen4 = pygame.transform.scale(start_screen4, (800, 600))
    start1 = pygame.image.load("StartScreen/Buttons1.png")
    start2 = pygame.image.load("StartScreen/Buttons2.png")
    controls1 = pygame.image.load("StartScreen/Buttons3.png")
    controls2 = pygame.image.load("StartScreen/Buttons4.png")
    quit1 = pygame.image.load("StartScreen/Buttons5.png")
    quit2 = pygame.image.load("StartScreen/Buttons6.png")
    restart1 = pygame.image.load("StartScreen/Buttons7.png")
    restart2 = pygame.image.load("StartScreen/Buttons8.png")
    start1 = pygame.transform.scale(start1, (200, 200))
    start2 = pygame.transform.scale(start2, (200, 200))
    controls1 = pygame.transform.scale(controls1, (200, 200))
    controls2 = pygame.transform.scale(controls2, (200, 200))
    quit1 = pygame.transform.scale(quit1, (200, 200))
    quit2 = pygame.transform.scale(quit2, (200, 200))
    restart1 = pygame.transform.scale(restart1, (200, 200))
    restart2 = pygame.transform.scale(restart2, (200, 200))
    logo = pygame.image.load("StartScreen/logo.png")
    logo = pygame.transform.scale(logo, (300, 300))
    cursor = pygame.image.load("StartScreen/Cursor.png")
    cursor = pygame.transform.scale(cursor, (50, 50))
    cursor2 = pygame.image.load("StartScreen/Cursor2.png")
    cursor2 = pygame.transform.scale(cursor2, (50, 50))
    controlsIMG = pygame.image.load("ControlsIMG.PNG")
    controlsIMG = (pygame.transform.scale(controlsIMG, (800, 600)))
    pygame.mixer.music.load('GhostHuntersSoundtrack.wav')
    pygame.mixer.music.play(-1, 0.0)

#Defining Colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,128,0)
lime = (0,255,0)
yellow = (255, 255, 0)

#Defining Functions used in the game

#Character Animations
def character_animation():

    #Taking in all neccessary variables
    global  counter1, movement, mcX, mcY, animation_Reset1, background, angle, character_Hitbox

    #Resetting the animation timer
    animation_Reset1 = counter1/50

    #Displaying the background
    window_size.blit(background, (bkX, bkY))

    #Moving the player forward if w is pressed by and displaying corresponding animations
    if movement == "forward":
        if animation_Reset1 < 0.25:
            window_size.blit(Forward1, (mcX, mcY))
        
        elif animation_Reset1 < 0.5:
            window_size.blit(Forward2, (mcX, mcY))

        elif animation_Reset1 < 0.75:
            window_size.blit(Forward3, (mcX, mcY))

        elif animation_Reset1 < 1:
            window_size.blit(Forward4, (mcX, mcY))

        else:
            window_size.blit(Forward1, (mcX, mcY))
            counter1 = 0

    #Moving the player downward if s is pressed by displaying corresponding animations
    elif movement == "downward":
        if animation_Reset1 < 0.25:
            window_size.blit(Backword1, (mcX, mcY))
        
        elif animation_Reset1 < 0.5:
            window_size.blit(Backword2, (mcX, mcY))

        elif animation_Reset1 < 0.75:
            window_size.blit(Backword3, (mcX, mcY))

        elif animation_Reset1 < 1:
            window_size.blit(Backword4, (mcX, mcY))

        else:
            window_size.blit(Backword1, (mcX, mcY))
            counter1 = 0
            
    #Moving the player left if a is pressed by displaying the corresponding animations
    elif movement == "left":
        if animation_Reset1 < 0.25:
            window_size.blit(Left1, (mcX, mcY))
        
        elif animation_Reset1 < 0.5:
            window_size.blit(Left2, (mcX, mcY))

        elif animation_Reset1 < 0.75:
            window_size.blit(Left3, (mcX, mcY))

        elif animation_Reset1 < 1:
            window_size.blit(Left4, (mcX, mcY))

        else:
            window_size.blit(Left1, (mcX, mcY))
            counter1 = 0
            
    #Moving the player right if d is pressed by displaying the corresponding animations
    elif movement == "right":
        if animation_Reset1 < 0.25:
            window_size.blit(Right1, (mcX, mcY))
        
        elif animation_Reset1 < 0.5:
            window_size.blit(Right2, (mcX, mcY))

        elif animation_Reset1 < 0.75:
            window_size.blit(Right3, (mcX, mcY))

        elif animation_Reset1 < 1:
            window_size.blit(Right4, (mcX, mcY))

        else:
            window_size.blit(Right1, (mcX, mcY))
            counter1 = 0
        
    #If no key is pressed, stop the player from moving, stop displaying any passed animations, and displaying the corresponding animations
    elif movement == "None":

            if animation_Reset1 < 0.5:
                window_size.blit(Rest1, (mcX, mcY))

            elif animation_Reset1 < 1:
                window_size.blit(Rest2, (mcX, mcY))

            else:
                window_size.blit(Rest1, (mcX, mcY)) 
                counter1 = 0

#Character movement
def character_movement():

    #Taking in all of the neccessary variables into the function
    global bkX, bkY, mcY, mcX, character_Hitbox, r_left, r_right, r_top, r_bottom, background_moving, character_Hitbox

    #Initializing the player's hitbox
    character_Hitbox = pygame.draw.rect(window_size, red, (mcX, mcY, 100, 100))

    #Intializing the hitboxes around the room
    r_left = pygame.draw.rect(window_size, red, (bkX+140, bkY+150, 1, 1100))
    r_right = pygame.draw.rect(window_size, red, (bkX+1100, bkY+150, 1, 1100))
    r_top = pygame.draw.rect(window_size, red, (bkX+165, bkY+150, 1100, 1))
    r_bottom = pygame.draw.rect(window_size, red, (bkX+165, bkY+1120, 1100, 1))

    #Moving the background according to the direction the player is moving

    #Moving the player and background according to the direction they are moving

    #Moving the background down is the player is moving up
    if movement == "forward" and bkY != -104:
        bkY += 7
        background_moving = True

    #Stopping the player from moving any farther up if they have reached the top of the room
    elif movement == "forward" and character_Hitbox.colliderect(r_top) != True:
        mcY -=7
        background_moving = False
    
    #Moving the background up if the player is moving downwards
    if movement == "downward" and bkY != -538:
        bkY -= 7
        background_moving = True
    
    #Stopping the player from moving any father down if they have reached the bottom of the room
    elif movement == "downward" and character_Hitbox.colliderect(r_bottom) != True:
        mcY +=7
        background_moving = False
    
    #Moving the background right if the player is moving left
    if movement == "left" and bkX != -89:
        bkX += 7
        background_moving = True

    #Stopping the player from moving any farther left after they have reached the left wall of the room
    elif movement == "left" and character_Hitbox.colliderect(r_left) != True:
        mcX -=7
        background_moving = False
    
    #Moving the background left if the player is moving right
    if movement == "right" and bkX != -348:
        bkX -= 7
        background_moving = True

    #Stopping the player from moving any farther right after they have reached the right wall in the room
    elif movement == "right" and character_Hitbox.colliderect(r_right) != True:
        mcX +=7
        background_moving = False

#Using the flashlight
def flashlight_function():

    #Taking in all of the neccessary variables used in this function
    global OnSwitch, mouse_position, mc_centerX, mc_centerY, angle, flashlight, mcX, mcY

    #If the left mouse button is clicked and the flashlight is turned on
    if OnSwitch == -1:

        #Finding the postion of the player's mosue
        mouse_position = pygame.mouse.get_pos()

        #Calculating the angle of the flashlight or where it should be facing relative to the player's mouse postion (Does this by rotating the black background allowing for the player to see through the other side)
        angle = 360 - math.atan2(mouse_position[1] - (mcY+50), mouse_position[0] - (mcX+50)) * 180 / math.pi
        rotimage = pygame.transform.rotate(flashlight,angle - 100)

        #Rotating the flashlight relative to the player (Rotating the black background relative to the player's location in the game)
        rect = rotimage.get_rect(center=(mcX+50, mcY+50))
        
        #Displaying that black background when the flashlight is on
        window_size.blit(rotimage,rect)
    
    #If the flashlight is turned off then display a full black screen
    else: 
        window_size.fill(black)

#Changing the characters stance relative to the flashlight's angle
def flashlight_character_movement():

    #Taking in the neccessary variables
    global movement, angle, mcX, mcY

    #When the player has stopped moving
    if movement == "None":

            #Displaying the background
            window_size.blit(background, (bkX, bkY))

            #If the flashlight is to the left of the player, the player should face left
            if angle-100 < 110 or angle-100 > 400:
                window_size.blit(Left1, (mcX, mcY))

            #If the flashlight is below the player, the player should face down
            elif angle-100 < 220:
                window_size.blit(Backword1, (mcX, mcY))

            #If the flashlight is to the right of the player, the player should face right
            elif angle-100 < 295:
                window_size.blit(Right1, (mcX, mcY))

            #If the flashlight is above the player, the player should face up
            elif angle-100 < 400:
                window_size.blit(Forward1, (mcX, mcY))

#Spawning in Ghosts/enemies
def ghost_spawn(): 

    #Taking in all neccessary variables used in this function
    global ghost_counter, bkX, bkY, ghost_hitbox, counter3, points, death_variable, character_Hitbox, hit

    #Adding a new ghost every 100 ticks of the counter (1-2 seconds)
    if ghost_counter >= 100:
        ghost_list.append([random.randint(bkX, bkX+1250), random.randint(bkY, bkY+1250)])
        ghost_counter = 0

    #Displaying each ghost
    for x in ghost_list:
        ghost_hitbox = pygame.draw.rect(window_size, red, (x[0], x[1], 80, 80))

        #What happens when you click on a ghost, AKA when it is killed
        if ghost_hitbox.collidepoint(click) and x in ghost_list:

                #Removing the ghost from the display list therefore stopping it from being displayed, and also adding to the player's score
                ghost_list.remove(x)
                points += 10

        #What happens when the player runs into a ghost, AKA how the player dies
        if character_Hitbox.colliderect(ghost_hitbox):
            death_variable = True

#Ghost AI and tracking towards the character and ghost animations         
def ghost_swarm():

    #Taking in all neccessay variables used in the function
    global background_moving, mcX, mcY, bkX, bkY, counter2, animation_Reset2, movement, click, ghost_hitbox, ghost_list

    #Resetting the aniamation counter for the ghost
    animation_Reset2 = counter2/50

    #Iterating through each ghost and changing what direction and by how much the ghost is travelling relative to the location of the player in the game
    for x in ghost_list:

        #Taking into account the movement of the player
        if background_moving == True:

            #Moving the ghosts relative to the direction the player is moving 
            if movement == "forward":
                x[1] += 7
            
            if movement == "downward":
                x[1] -= 7

            if movement == "left":
                x[0] += 7
            
            if movement == "right":
                x[0] -= 7

            #
            else:
                if x[0] < mcX:
                    x[0] += 1

                if x[0] > mcX:
                    x[0] -= 1

                if x[1] < mcY:
                    x[1] += 1

                if x[1] > mcY:
                    x[1] -= 1
        
        #Moving the ghosts towards the player even if the player is not moving
        else:
            if x[0] < mcX:
                x[0] += 1

            if x[0] > mcX:
                x[0] -= 1

            if x[1] < mcY:
                x[1] += 1

            if x[1] > mcY:
                x[1] -= 2

        #recturning the data type to a tuple so I a blit the animations
        x = tuple(x)

        #Ghost animations relative to its animation counter
        if animation_Reset2 < 0.25:
            window_size.blit(ghosts_hover1, (x[0], x[1]))

        elif animation_Reset2 < 0.5:
            window_size.blit(ghosts_hover2, (x[0], x[1]))

        elif animation_Reset2 < 0.75:
            window_size.blit(ghosts_hover3, (x[0], x[1]))

        elif animation_Reset2 < 1:
            window_size.blit(ghosts_hover4, (x[0], x[1]))
        else:
            window_size.blit(ghosts_hover1, (x[0], x[1]))
            counter2 = 0

#Displaying the score and time
def menu_GUI():

    #Taking in all neccessary variables
    global points, game_font, score, seconds, milliseconds, minutes, timelabel

    #Determining the score
    score = game_font.render(str(points), True,red)

    #Displaying the score
    window_size.blit(score, (10, 10))

    #fills the area
    cover = pygame.surface.Surface((160,40)).convert()
    cover.fill((220, 220, 220))

    #The counter system for the amount of time the player has survived
    if milliseconds > 1000 and death_variable != True:
        seconds += 1
        milliseconds -= 1000
        pygame.display.update()

    #Changing the seconds to minutes when necessary
    if seconds > 60 and death_variable != True:
        minutes += 1
        seconds -= 60

    #time system that takes seconds and minutes and turns into a correct format
    milliseconds += clock.tick_busy_loop(60)
    timelabel = game_font.render("{}:{}".format(minutes, seconds), True, red)
    window_size.blit(timelabel,(10, 50))

#Displaying menu on death
def death():
    
    #Taking in all necessary variables used in this function
        global ghost_hitbox, character_Hitbox, ghost_list, death_variable, game_font2, restart, hover, click, start, seconds, minutes, points

        #What happens when the player had died in game
        if death_variable == True:

            #Getting the postion of the mouse
            hover = pygame.mouse.get_pos()

            ###Displaying the neccessary elements that pop up once the player has died###
            restart_hitbox = pygame.draw.rect(window_size, red, (300, 500, 200, 60))
            window_size.blit(death_screen, (0, 0))

            #Telling the user they died
            death_text= game_font2.render("You Died", True, red)
            window_size.blit(death_text, (300, 20))

            #Telling the player how they did (Time lasted in game, and the score they acheived)
            timelasted = game_font.render("You lasted for: "+str(minutes)+":"+str(seconds), True, red)
            pointstext = game_font.render("Ghost Points: "+str(points), True, red)
            window_size.blit(timelasted, (100, 100))
            window_size.blit(pointstext, (100, 150))

            #If the restart button is hovered over change the appearence of the button
            if restart_hitbox.collidepoint(hover):
                window_size.blit(restart2, (300, 450))

            #Displaying the restart button
            else:
                window_size.blit(restart1, (300, 450))

            #If the restart button is clicked restart the game
            if restart_hitbox.collidepoint(click):
                death_variable = False
                restart = True
                start = True

#Combines nearly every other function to produce the core of the game
def main_game():

    #Taking in all neccessary variables used in the function
    global character_Hitbox

    #Initializing the player's hitbox
    character_Hitbox = pygame.draw.rect(window_size, red, (mcX, mcY, 100, 100))

    #Calling all major functions which make up this gaem
    ghost_spawn() 
    character_movement()
    character_animation()
    flashlight_character_movement() 
    ghost_swarm()
    flashlight_function()      
    menu_GUI()
    death() 

#Start Screen
def start_screen():

    #Taking in all neccessary variables
    global start_screen_counter, hover, click, restart, death_variable, quit_hitbox, start, ghost_list, start, mcX, mcY, bkX, bkY, movement, counter1, counter2, counter3, ghost_counter, OnSwitch, background_moving, angle, points, ghost_ros, clock, minutes, seconds, milliseconds, hit, choice

    #Getting the postion of the mouse
    hover = pygame.mouse.get_pos()
    
    #Resetting/Initialising all the neccessary variables used throughout the game
    if start == True:
        ghost_list.clear()
        minutes = 0
        seconds = 0
        milliseconds = 0
        points = 0
        mcX = 350
        mcY = 250
        bkX = -250
        bkY = -300
        OnSwitch = 1
        hit = False

        #Intitialising the hitboxes on the start screen so that they can be interacted with by the player
        start_hitbox = pygame.draw.rect(window_size, red, (320, 290, 160, 60))
        controls_hitbox = pygame.draw.rect(window_size, red, (300, 370, 200, 60))
        quit_hitbox = pygame.draw.rect(window_size, red, (320, 450, 160, 60))

        #Animations for the startscreen relative to its corresponding animations counter
        if start_screen_counter < 5:
            window_size.blit(start_screen1, (0,0))

        elif start_screen_counter < 10:
            window_size.blit(start_screen2, (0,0))

        elif start_screen_counter < 15:
            window_size.blit(start_screen3, (0,0))

        elif start_screen_counter < 20:
            window_size.blit(start_screen4, (0,0))

        else:
            window_size.blit(start_screen1, (0,0))
            start_screen_counter = 0

        #if hover collides with start button change the image the blitted into the butten location
        if start_hitbox.collidepoint(hover):
            window_size.blit(start2, (300,240))

        else:
            window_size.blit(start1, (300,240))

        #if hover collides with controls button change the image the blitted into the butten location
        if controls_hitbox.collidepoint(hover):
            window_size.blit(controls2, (300, 320))

        else:
            window_size.blit(controls1, (300, 320))

        #if hover collides with quit button change the image the blitted into the butten location
        if quit_hitbox.collidepoint(hover):
            window_size.blit(quit2, (300, 400))

        else:
            window_size.blit(quit1, (300, 400))


        #redefined variables
        if start_hitbox.collidepoint(click):
            start = False
            restart = False

        #blit logo on title screen
        window_size.blit(logo, (250, 30))


        #if controls_hitbox collide of click, blit controls image, time.sleep(), redefine click
        if controls_hitbox.collidepoint(click):
            window_size.blit(controlsIMG, (0,0))
            pygame.display.update()
            time.sleep(4)
            click = [0, 0]
            
        #checking if the choice variable is equal to the True   
        if choice == True:

            #redefineing choice so at not repeat the group
            choice = False


#Main loop
while True:

    #Getting the mouse postion
    hover = pygame.mouse.get_pos()

    #If the restart button is clicked after death
    if restart == True:
        start_screen()

    #If the player is still playing and hasn't died yet
    if restart != True:

        #Running the game, and core of ghost hunters
        main_game()

        #Restarting the background music
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1, 0.0)

    #Making the default mouse invisible on screen and replacing the standard image with a custom one
    pygame.mouse.set_visible(False)

    if OnSwitch == -1:
        window_size.blit(cursor2, (hover[0]-20, hover[1]-20))
        
    else:
        window_size.blit(cursor, (hover[0]-5, hover[1]-5))

    #call functions and update varibles here
    
    #check events that occurs
    for event in pygame.event.get():

        #If a key is pressed down
        if event.type == KEYDOWN:

            #If that key is w
            if event.key == K_w:

                #Setting the corresponding direction of the player
                movement = "forward"

            #If that key is a
            if event.key == K_a:

                #Setting the corresponding direction of the player
                movement = "left"
                
            #If that key is s
            if event.key == K_s:

                #Setting the corresponding direction of the player
                movement = "downward"

            #If that key is d
            if event.key == K_d:

                #Setting the corresponding direction of the player
                movement = "right"
                
                
        #If a key is lifted up
        if event.type == KEYUP:

            #Stopping all movement of the player
            movement = "None"

        #If a button on the mouse is clicked
        if event.type == MOUSEBUTTONDOWN:

            #If that is left click
            if event.button == 1:

                #Getting the postion of the mouse on the click of the mouse
                click = pygame.mouse.get_pos()

            #If that is right click
            if event.button == 3:

                #Turning on the flashlight
                OnSwitch *= -1
        
        #checking if user closes the window
        if event.type == QUIT or quit_hitbox.collidepoint(click):
            pygame.quit()
            sys.exit()

    #update the display window
    pygame.display.update()
    fpsclock.tick(fps)
    
    #Updating all animation timers
    counter1 += 1
    counter2 += 1
    ghost_counter += 2
    start_screen_counter += 1
    