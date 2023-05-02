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
import numpy as np
#camera:
camera = uvage.Camera(1920,1080)
camera.center = [400,300]
#globals
global backgroundlist
backgroundlist = []
global bricklist
bricklist = []
global bricklist_tick
bricklist_tick = []
global speedlist
speedlist = []
global score
score = []
global liveslist
liveslist = []
global goombalist
goombalist = []
global goombalist_tick
goombalist_tick = []
global goombaintlist
goombaintlist = []
global coinindexlist
global coinindexlist_1brick

#outside functions
for i in range(0,101): #generates the basic mario background for game play
    c = (400+(i*1920))
    background = uvage.from_image(c,300, 'mariobackground.jpg')
    backgroundlist.append(background)
flag = uvage.from_image(7960,400,'marioflag.png')
flag.scale_by(.5)
castle = uvage.from_image(8300,550, 'mariocastle.png')
castle.scale_by(.25)
for i in range(0, 101): #generates the bricks for mario to jump on ***WORK IN PROGRESS***
    c = i*400
    r = random.randint(0,300)
    brick = uvage.from_image(0 + c, 100, 'mariobrick.png')
    brick.scale_by(0.4)
    brick2 = uvage.from_image(200 + c, 100, 'mariobrick.png')
    brick2.scale_by(.4)
    brick3 = uvage.from_image(400 + c, 100, 'mariobrick.png')
    brick3.scale_by(.4)
    nestedbricklist = [brick, brick2, brick3]
    brick = uvage.from_image(0+c,300, 'mariobrick.png')
    brick.scale_by(0.4)
    brick2 = uvage.from_image(200+c,300, 'mariobrick.png')
    brick2.scale_by(.4)
    brick3 = uvage.from_image(400+c,300, 'mariobrick.png')
    brick3.scale_by(.4)
    nestedbricklist1 = [brick,brick2,brick3]
    brick = uvage.from_image(0 + c, 500, 'mariobrick.png')
    brick.scale_by(0.4)
    brick2 = uvage.from_image(200 + c, 500, 'mariobrick.png')
    brick2.scale_by(.4)
    brick3 = uvage.from_image(400 + c, 500, 'mariobrick.png')
    brick3.scale_by(.4)
    nestedbricklist2 = [brick,brick2,brick3]
    bricklist.append(nestedbricklist)
    bricklist.append(nestedbricklist1)
    bricklist.append(nestedbricklist2) #stores everything into a list that can be called to eventually 'draw' the map
heartlist = []
for i in range(0,120,40):
    heart = uvage.from_image((camera.topright[0]-60)-i,camera.topright[1]+100,'mariohearts.png')
    heart.scale_by(.1)
    heartlist.append(heart)
mariosprite = uvage.from_image(400,675,'mariosprite.png') #mario generation
mariosprite.scale_by(.03)
goomba = uvage.from_image(1000,0,'goomba.png')
goomba.scale_by(.3)

def goombawrite(x,y):
    goombainside = uvage.from_image(1000,0,'goomba.png')
    goombainside.scale_by(.3)
    goombareturn = goombainside.copy_at(x,y)
    return goombareturn


for i in range(0,10001):
    goomba2 = goombawrite(i,0)
    goombalist.append(goomba2)
coinlist = []
coin = uvage.from_image(400,300,'coin image.png')
coin.scale_by(.15)
coinlist.append(coin)
coinindexlist = [8,10,12,14,16,23,25,27,35,37,39,47,49]
coinindexlist_1brick = [46,48,55,57]
def coincreate(index):
    for i in range(0,3):
        c = 200 * i
        coin2 = coin.copy_at(bricklist[index][0].center[0] + c, bricklist[index][0].center[1]-75)
        coinlist.append(coin2)
def coincreate_1brick(index):

    coin2 = coin.copy_at(bricklist[index][0].center[0], bricklist[index][0].center[1] - 75)
    coinlist.append(coin2)
for item in coinindexlist:
    coincreate(item)
for item in coinindexlist_1brick:
    coincreate_1brick(item)

bottomborder = uvage.from_color(-500,700, 'black', 50000, 10) #used as a way to get mario to 'interact' with the floor of the picture background


#trialjump:
def trialjump(sprite):
    if sprite == mariosprite:#next iteration of jump, based on the jump function in b_ball_shot.py
        if sprite.bottom_touches(bottomborder):
            if uvage.is_pressing('space'):
                sprite.speedy = -25
    sprite.speedy +=.5
    sprite.move_speed()
    sprite.move_to_stop_overlapping(bottomborder)
def brickjump(sprite, brick):
    if sprite == mariosprite:#next iteration of jump, based on the jump function in b_ball_shot.py
        if sprite.bottom_touches(brick):
            if uvage.is_pressing('space'):
                sprite.speedy = -25
    sprite.speedy +=.5
    sprite.move_speed()
    sprite.move_to_stop_overlapping(brick)

def coin_count(coin_):

    if mariosprite.touches(coin_):
        score.append(1)
        coin_.move(0,1000)
def goombamove(goomba,heart):
    goomba.speedx = -1

    goomba.move_speed()
    if mariosprite.bottom_touches(goomba):
        goomba.move(0,1500)
        score.append(1)
        score.append(1)
    elif goomba.touches(mariosprite):
        liveslist.append(1)
        goomba.move(0,1500)
        heart[-len(liveslist)].move(0,1500)
def goombadraw(goomba):
    camera.draw(goomba)
    goombalist_tick.append(goomba)



def bricktouch(brick,sprite):
    for i in range(0,3):#TRIAL FOR INTERACTION WITH BRICKS ***major problem with not landing directly on them***
        if brick.bottom_touches(sprite):
            sprite.move_to_stop_overlapping(brick)
        if brick.top_touches(sprite):
            sprite.move_to_stop_overlapping(brick)
            trialjump(sprite)
            brickjump(sprite, brick)


def drawbrick(index):
    for j in range(0, 3):  # TRIAL FOR INTERACTION TESTING -> generates one set of 'bricks'
        camera.draw(bricklist[index][j])
        bricklist_tick.append(bricklist[index][j])
def drawbrick_1brick(index):
    camera.draw(bricklist[index][0])
    bricklist_tick.append(bricklist[index][0])

        #print(bricklist[index][j])



#tick:
def mechanicsfunc(sprite,Goomba,brick = bricklist_tick):
    trialjump(sprite)
    trialjump(Goomba)
    coin_count(coin)
    for i in range(0,len(coinlist)):
        coin_count(coinlist[i])
    for bricks in bricklist_tick:
        bricktouch(bricks, sprite)
        bricktouch(bricks, Goomba)


def move(scoreboard):
    if uvage.is_pressing('right arrow') or uvage.is_pressing('d'): #mimicks mario gameplay, camera moves to the right but not to the left
        mariosprite.move(7,0)
        scoreboard.move(5,0)
        camera.move(5,0)
        for heart in heartlist:
            heart.move(5,0)
    if uvage.is_pressing('left arrow') or uvage.is_pressing('a'):
        mariosprite.move(-5,0)
def tick():
    goombalist_tick.clear()
    bricklist_tick.clear()
    camera.draw(bottomborder)

    for i in range(0,101): #draws the background onto the camera
        camera.draw(backgroundlist[i])
    camera.draw(flag)
    camera.draw(castle)
    for index in coinindexlist:
        drawbrick(index)
    for index in coinindexlist_1brick:
        drawbrick_1brick(index)

    camera.draw(mariosprite)
    goombadraw(goomba)
    goombadraw(goombalist[800])
    goombadraw(goombalist[2500])
    if 3060<= mariosprite.center[0] <=3070:
        goombaintlist.append(1)
    if len(goombaintlist)!= 0:
        goombadraw(goombalist[3300])

    #if 4325<= mariosprite.center[0]<=4330:
        #goombaintlist.clear()
   # if 4331<= mariosprite.center[0]<=4341:
        #goombaintlist.append(1)
    #print(len(goombaintlist))
    #if len(goombaintlist) != 0:
       # goombadraw(goombalist[4600])
        #goombadraw(goombalist[4700])
    #camera.draw(coin)
    for i in range(0,len(coinlist)):
        camera.draw(coinlist[i])
    scoreboard = uvage.from_text(camera.topright[0]-60, camera.topright[1]+30, str(int(len(score))), 40, 'black')
    for i in heartlist:
        camera.draw(i)
    camera.draw(scoreboard)
    move(scoreboard)
    for Goomba in goombalist_tick:
        goombamove(Goomba,heartlist)
        mechanicsfunc(mariosprite,Goomba)

    camera.display()
    #print(len(goombaintlist))
    print(mariosprite.center)
uvage.timer_loop(60,tick)