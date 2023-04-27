#Sophia Spaner VPQ5KD & Jana Rodriguez  kay7ze
'''Sophia Spaner, VPQ5KD Jana Rodriguez (kay7ze)
Description: This game is a simple version of Super Mario Bros (1985 ver.). It will contain a player, the mario character, trying to get all the coins on the way. There also will be brown circles, representing the “Goombas,” trying to get “mario.” The game is won by collecting 100 coins and it ends if the player is touched by a “Goomba” three times. The 1985 version does not contain a health bar, however, when touched by a goomba Mario will appear smaller for a duration of time, causing the user to know that he is hurt. For convenience of the player, we will also include a basic three heart health bar (see additional features).

Basic Features:

User Input: The player can use the up, down, right, left, and space keys to move “Mario” through the level.

Game over: The game will end when Mario encounters the Goombas three times or if the timer runs out.

Graphics/images: The graphics used in this game are the background. There will be brown circles that represent the Goombas that will randomly appear as Mario goes through the level. There will also be coins for Mario to collect along the way. A timer will appear at the top right or left of the screen and a counter for the amount of coins collected. Further, we will also attempt to use the animation feature to have Mario look the way he does in the original ns64 games (i.e. 2d position changes based on what he is doing in game).

Additional Features:

Timer: The timer will allow the player to track how much time they have left. There will be a 5 minute countdown, displayed as 300 seconds,  for the player to go through the level. If the timer runs out, then game over.
Enemies: The “goombas” will be in brown to distinguish the difference between the player and the goombas. If the player is touched by a goomba, then it will restart to where they left.
Collectibles: The user must collect the coins in order to successfully win the game without letting the timer end.
Health bar: the health bar will be a visual of three hearts. If the user touches the “goombas” three times, then the game ends. However, if the user maintains at least one bar, and collects all the coins with enough time, then the user wins the game.
'''
#imports:
import uvage
import random
#camera:
camera = uvage.Camera(1920,1080)
camera.center = [400,300]
#globals
global backgroundlist
backgroundlist = []
global bricklist
bricklist = []
global speedlist
speedlist = []
#outside functions
for i in range(0,101): #generates the basic mario background for game play
    c = (400+(i*1920))
    background = uvage.from_image(c,300, 'mariobackground.jpg')
    backgroundlist.append(background)
for i in range(0, 101): #generates the bricks for mario to jump on ***WORK IN PROGRESS***
    c = i*400
    r = random.randint(0,300)
    brick = uvage.from_image(0+c,300, 'mariobrick.png')
    brick.scale_by(0.4)
    brick2 = uvage.from_image(200+c,300, 'mariobrick.png')
    brick2.scale_by(.4)
    brick3 = uvage.from_image(400+c,300, 'mariobrick.png')
    brick3.scale_by(.4)
    nestedbricklist = [brick,brick2,brick3]
    brick = uvage.from_image(0 + c, 500, 'mariobrick.png')
    brick.scale_by(0.4)
    brick2 = uvage.from_image(200 + c, 500, 'mariobrick.png')
    brick2.scale_by(.4)
    brick3 = uvage.from_image(400 + c, 500, 'mariobrick.png')
    brick3.scale_by(.4)
    nestedbricklist2 = [brick,brick2,brick3]
    bricklist.append(nestedbricklist)
    bricklist.append(nestedbricklist2) #stores everything into a list that can be called to eventually 'draw' the map
mariosprite = uvage.from_image(400,675,'mariosprite.png') #mario generation
mariosprite.scale_by(.03)
bottomborder = uvage.from_color(-500,700, 'black', 10000, 10) #used as a way to get mario to 'interact' with the floor of the picture background
# Jump Function:
def jump(): #THIS IS A TRIAL, IT DIDN'T WORK. problems arose with jumping more than once

    if uvage.is_pressing('space') and mariosprite.center[1]<=630:
        mariosprite.speedy -=.5
        mariosprite.move_speed()
    elif uvage.is_pressing('space') and mariosprite.center[1]>=630:
        mariosprite.speedy -=.5
        speedlist.append(mariosprite.speedy)
        mariosprite.move_speed()

    elif uvage.is_pressing('space') == False and mariosprite.center[1] <630:
        mariosprite.speedy +=.5
        mariosprite.move_speed()
    elif uvage.is_pressing('space') == False and mariosprite.center[1] >= 630:
        if len(speedlist) != 0:
            mariosprite.speedy-= speedlist[len(speedlist)-1]
            speedlist.clear()
#trialjump:
def trialjump(): #next iteration of jump, based on the jump function in b_ball_shot.py
    if mariosprite.bottom_touches(bottomborder):
        if uvage.is_pressing('space'):
            mariosprite.speedy = -35
    mariosprite.speedy +=1.25
    mariosprite.move_speed()
    mariosprite.move_to_stop_overlapping(bottomborder)






#tick:
def tick():

    if uvage.is_pressing('right arrow'): #mimicks mario gameplay, camera moves to the right but not to the left
        mariosprite.move(13,0)
        camera.move(9,0)
    if uvage.is_pressing('left arrow'):
        mariosprite.move(-10,0)
    camera.draw(bottomborder)
    for i in range(0,101): #draws the background onto the camera
        camera.draw(backgroundlist[i])
    for i in range(0,3): #TRIAL FOR INTERACTION TESTING -> generates one set of 'bricks'
        camera.draw(bricklist[5][i])

    camera.draw(mariosprite) #draws mario
    #jump()
    trialjump()
    for i in range(0,3):#TRIAL FOR INTERACTION WITH BRICKS ***major problem with not landing directly on them***
        if bricklist[5][i].top_touches(mariosprite):
            mariosprite.move_to_stop_overlapping(bricklist[5][i])
            #mariosprite.move(0,120)
    camera.display()
    print(mariosprite.speedy)#these are just here for help with testing
    print(mariosprite.center)
#timer call:
uvage.timer_loop(30,tick)