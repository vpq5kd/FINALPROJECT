#Sophia Spaner VPQ5KD & Jana Rodriguez  kay7ze
'''Sophia Spaner, VPQ5KD Jana Rodriguez (kay7ze)
Description: This game is a simple version of Super Mario Bros (1985 ver.). It will contain a player, the mario character, trying to get all the coins on the way. There also will be Goombas trying to get “mario.” The game is won by getting to the end without being killed. The 1985 version does not contain a health bar, however, when touched by a goomba Mario will appear smaller for a duration of time, causing the user to know that he is hurt. For convenience of the player, we will also include a basic three heart health bar (see additional features).

Basic Features:

User Input: The player can use the up, down, right, left, and space keys to move “Mario” through the level.

Game over: The game will end when Mario encounters the Goombas three times or if the timer runs out.

Graphics/Images: Mariosprite, Goombas, Background, Castle, Flag, Bricks, Coins
Additional Features:

Timer: The timer will allow the player to track how much time they have left. There will be a 30 second countdown,  for the player to go through the level. If the timer runs out, then game over.
Enemies: The “goombas” will be in brown to distinguish the difference between the player and the goombas. If the player is touched by a goomba, then it will restart to where they left.
Collectibles: The user must collect the coins in order to successfully win the game without letting the timer end.
Health bar: the health bar will be a visual of three hearts. If the user touches the “goombas” three times, then the game ends. However, if the user maintains at least one bar and makes it all the way to the end, the player wins.
Scrolling Level: game runs far beyond the screen
CHANGES SINCE C2: finished game, added castle and flag instead of coins to 100.

'''
#imports:
import uvage
#camera:
camera = uvage.Camera(1920,1080)
camera.center = [400,300]
#globals
global backgroundlist #holds all the information for drawing the background
backgroundlist = []
global bricklist #holds all the bricks
bricklist = []
global bricklist_tick #holds all the bricks currently drawn in game
bricklist_tick = []
global speedlist #list to hold necessary speeds of certain sprites
speedlist = []
global score #holds current score
score = []
global liveslist #holds total times killed
liveslist = []
global goombalist #holds 10000 goombas for calling at anypoint within game creation
goombalist = []
global goombalist_tick #holds goombas currently in game
goombalist_tick = []
global goombaintlist #holds interaction calls for mario based goombas
goombaintlist = []
global interactionlist #holds interactions of the flag and other things with mario, allow for certain test cases
interactionlist = []
global finalmariocordlist #holds final mario cords
finalmariocordlist = []
global timerlist #holds one tick per each frame
timerlist = []
global timersubtractlist #holds the actual timer
timersubtractlist = []
global startlist #holds the value 'start', called after first screen
startlist = []
global coinindexlist #used for creation of 3 block coins
global coinindexlist_1brick #used for creation of 1 block coins

#outside functions
for i in range(0,101): #generates the basic mario background for game play
    c = (400+(i*1920))
    background = uvage.from_image(c,300, 'mariobackground.jpg')
    backgroundlist.append(background)
flag = uvage.from_image(7960,400,'marioflag.png') #generates final flag
flag.scale_by(.5)
flagpole = uvage.from_image(7960,400,'marioflagpole.png') #generates flag pole for interacting
flagpole.scale_by(.5)
castle = uvage.from_image(8300,550, 'mariocastle.png') #generates final castle
castle.scale_by(.25)
castleinteractor = uvage.from_color(8300,600,'pink',100,175) #generates color for castle interaction
for i in range(0, 101): #generates the bricks for mario to jump on ***WORK IN PROGRESS***
    c = i*400
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
heartlist = [] #stores the values for drawing hearts
for i in range(0,120,40):
    heart = uvage.from_image((camera.topright[0]-60)-i,camera.topright[1]+100,'mariohearts.png')
    heart.scale_by(.1)
    heartlist.append(heart)
mariosprite = uvage.from_image(400,675,'mariosprite.png') #mario generation
mariosprite.scale_by(.03)
goomba = uvage.from_image(1000,0,'goomba.png') #goomba for copying
goomba.scale_by(.3)
#opening screen func:
def openingscreen():
    if 'start' not in startlist: #if game hasn't been started
        for item in backgroundlist: #draws background
            camera.draw(item)
        mario = uvage.from_text(camera.center[0],camera.center[1]-200,'MARIO, THE UVAGE EDITION',50, 'pink',bold=True ) #all the following draw the first text
        computer1 = uvage.from_text(camera.center[0],camera.center[1]-150,'FOR BEST GAMEPLAY, PLEASE ENSURE 1920X1080 COMPUTER WINDOW',15, 'black',bold=False )
        rules = uvage.from_text(camera.center[0],camera.center[1]-100,'USE ARROWS TO MOVE \n COINS = 1 POINT, JUMP ON GOOMBA = 2 POINTS \n GOOMBAS KILL, DO NOT LET THEM HIT YOU THRICE \n YOU HAVE 30 SECONDS \n GOODLUCK!',30, 'black', )
        computer = uvage.from_text(camera.center[0],camera.center[1]-50,'FOR BEST GAMEPLAY, PLEASE ENSURE 1920X1080 COMPUTER WINDOW',15, 'black',bold=False )
        start = uvage.from_text(camera.center[0],camera.center[1],'PRESS SPACE TO START',50, 'pink',bold=True )
        camera.draw(mario)
        camera.draw(rules)
        camera.draw(computer)
        camera.draw(computer1)
        camera.draw(start)
        if uvage.is_pressing('space') and len(timerlist)==0: #allows game to start
            startlist.append('start')
        camera.display()
#goombawrite func:
def goombawrite(x,y): #creates goombas to be called
    goombainside = uvage.from_image(1000,0,'goomba.png')
    goombainside.scale_by(.3)
    goombareturn = goombainside.copy_at(x,y)
    return goombareturn

#outside func that creates 10000 goombas, used in game creation:
for i in range(0,10001):
    goomba2 = goombawrite(i,0)
    goombalist.append(goomba2)
coinlist = [] #list of all coins
coin = uvage.from_image(400,300,'coin image.png')
coin.scale_by(.15)
coinlist.append(coin)
coinindexlist = [8,10,12,14,16,23,25,27,35,37,39,47,49] #index for drawing the coins above the 3 brick rows and drawing the 3 brick rows (from bricklist)
coinindexlist_1brick = [46,48,55,57] #same but for one brick rows
def coincreate(index): #creates the coins above the 3 brick rows
    for i in range(0,3):
        c = 200 * i
        coin2 = coin.copy_at(bricklist[index][0].center[0] + c, bricklist[index][0].center[1]-75) #center of each brick
        coinlist.append(coin2)
def coincreate_1brick(index): #creates the coins above the 1 brick rows

    coin2 = coin.copy_at(bricklist[index][0].center[0], bricklist[index][0].center[1] - 75)
    coinlist.append(coin2)
for item in coinindexlist: #creates coins for each index
    coincreate(item)
for item in coinindexlist_1brick:
    coincreate_1brick(item)

bottomborder = uvage.from_color(-500,700, 'black', 50000, 10) #used as a way to get mario to 'interact' with the floor of the picture background


#trialjump:
def trialjump(sprite): #defined as sprite because its also used as a gravity function for goombas
    if sprite == mariosprite:#next iteration of jump, based on the jump function in b_ball_shot.py
        if sprite.bottom_touches(bottomborder):
            if uvage.is_pressing('space'):
                sprite.speedy = -25
    if 'flag touch' not in interactionlist: #kills gravity if touching flag
        sprite.speedy +=.5
        sprite.move_speed()
        sprite.move_to_stop_overlapping(bottomborder)
#brick jump
def brickjump(sprite, brick):#same as jump just for bricks
    if sprite == mariosprite:#next iteration of jump, based on the jump function in b_ball_shot.py
        if sprite.bottom_touches(brick):
            if uvage.is_pressing('space'):
                sprite.speedy = -25
    if 'flag touch' not in interactionlist:
        sprite.speedy +=.5
        sprite.move_speed()
        sprite.move_to_stop_overlapping(brick)
#coin_count:
def coin_count(coin_): #counts the amount of coins hit, appends to score, gets rid of coin

    if mariosprite.touches(coin_):
        score.append(1)
        coin_.move(0,1000)
#goombamove:
def goombamove(goomba,heart):  #movement and interactions for goombas
    goomba.speedx = -1 #goombas always moving 1 towards the left

    goomba.move_speed()
    if mariosprite.bottom_touches(goomba): #if mario kills goomba
        goomba.move(0,1500)#gets rid of goomba
        score.append(1)#gives two score
        score.append(1)
    elif goomba.touches(mariosprite):#if goomba kills mario
        if len(liveslist) == 2: #if last life, appends cords for closing screen
            finalmariocordlist.append(mariosprite.center[0])
            finalmariocordlist.append(mariosprite.center[1])
        liveslist.append(1) #adds one death
        goomba.move(0,1500)#gets rid of goomba
        heart[-len(liveslist)].move(0,1500) #gets rid of heart
#goombadraw:
def goombadraw(goomba):
    camera.draw(goomba)
    goombalist_tick.append(goomba) #appends to the tick list


#brick touch:
def bricktouch(brick,sprite): #defines interactions for goomba and mario with bricks
    for i in range(0,3): #allows mario or goomba to land on brick but not jump through *glitch with brick corners, but makes game more fun (original mario has glitches)
        if brick.bottom_touches(sprite):
            sprite.move_to_stop_overlapping(brick)
        if brick.top_touches(sprite):
            sprite.move_to_stop_overlapping(brick)
            trialjump(sprite) #gravity, jump
            brickjump(sprite, brick) #gravity, jump

#drawbrick:
def drawbrick(index):
    for j in range(0, 3):  #generates bricks
        camera.draw(bricklist[index][j])
        bricklist_tick.append(bricklist[index][j]) #appends into tick list for inter tick interaction
    #drawbrick_1brick:
def drawbrick_1brick(index):#same but for the single bricks
    camera.draw(bricklist[index][0])
    bricklist_tick.append(bricklist[index][0])

        #print(bricklist[index][j])


#mechanicsfunc
def mechanicsfunc(sprite,Goomba,brick = bricklist_tick): #all the individual mechanics in one func
    trialjump(sprite) #gravity and jump function (jump only for mario)
    trialjump(Goomba)
    coin_count(coin)
    for i in range(0,len(coinlist)): #applys coin mechanics to all coins
        coin_count(coinlist[i])
    for bricks in bricklist_tick: #brick mechanics for sprite and goomba
        bricktouch(bricks, sprite)
        bricktouch(bricks, Goomba)


def move(scoreboard,timer): #movement for mario
    if 'flag touch' not in interactionlist: #tests to make sure that its not end of game
        if uvage.is_pressing('right arrow') or uvage.is_pressing('d'): #mimicks mario gameplay, camera moves to the right but not to the left
            mariosprite.move(10,0) #moves mario faster than camera, keeps mario from getting stuck
            scoreboard.move(8,0) #moves timer and scoreboard with camera
            timer.move(8,0)
            camera.move(8,0)

            for heart in heartlist: #moves hearts with camera
                heart.move(8,0)
        if uvage.is_pressing('left arrow') or uvage.is_pressing('a'):
            mariosprite.move(-5,0)
#flaginteraction:
def flaginteraction(flag):
    if mariosprite.touches(flag): #appends tells to interactionlist for end of game
        interactionlist.append('flag touch')
        interactionlist.append('flag move')
        mariosprite.speedy = 3 #moves mario down flag
        mariosprite.move_speed()
    elif mariosprite.touches(flag) == False: #prevents flagtouch from being there if not touching flag
        if 'flag touch' in interactionlist:
            interactionlist.remove('flag touch')
    mariosprite.move_to_stop_overlapping(bottomborder) #stops mario at border

#Tick:
def tick():
    openingscreen() #runs opening screen
    if len(liveslist) != 3 and mariosprite.touches(castleinteractor)==False and 30-len(timersubtractlist) != 0 and 'start' in startlist: #starts game
        timerlist.append(1) #one per frame, 60 frames per second, each second one subtracted from 30
        if len(timerlist) >= 60:
            if len(timerlist) % 60 == 0 and 'flag touch' not in interactionlist: #stops timer if hits flag as well
                timersubtractlist.append(1)
        timer = uvage.from_text(camera.topleft[0]+75, camera.topleft[1]+30, str(30-len(timersubtractlist)), 40, 'black')
        if 30-len(timersubtractlist) == 1:
            finalmariocordlist.append(mariosprite.center) #gets cords of mario if timer runs out
        goombalist_tick.clear() #clears ticklists each time, that way they don't get duplicates
        bricklist_tick.clear()
        camera.draw(bottomborder) #draws the bottom border before background so it isn't seen

        for i in range(0,101): #draws the background onto the camera
            camera.draw(backgroundlist[i])
        camera.draw(flag) #draws flag, flagpole, castle interactor, and castle
        camera.draw(flagpole)
        camera.draw(castleinteractor)
        camera.draw(castle)

        for index in coinindexlist: #draws all the bricks(based on earlier index)
            drawbrick(index)
        for index in coinindexlist_1brick: #draws all the single bricks
            drawbrick_1brick(index)

        camera.draw(mariosprite)#draws mario
        goombadraw(goomba) #first three draw starter goombas
        goombadraw(goombalist[800])
        goombadraw(goombalist[2500])
        #the following draw goombas granted certain conditions of mario, allows for rapid enemies
        if 1990 <= mariosprite.center[0] <= 2000:
            goombaintlist.append('goomba 0')
        if 'goomba 0' in goombaintlist:
            goombadraw(goombalist[2800])
        if 3060<= mariosprite.center[0] <=3070:
            goombaintlist.append('goomba 1')
        if 'goomba 1' in goombaintlist:
            goombadraw(goombalist[3600])
        if 4331<= mariosprite.center[0]<=4341:
            goombaintlist.append('goomba 2')
        if 'goomba 2' in goombaintlist:
            goombadraw(goombalist[4900])
        if 6050 <= mariosprite.center[0] <= 6060:
            goombaintlist.append('goomba 3')
        if 'goomba 3' in goombaintlist: #goombaintlist checks to see if the goomba was created by mario presence
            goombadraw(goombalist[6600])
        for i in range(0,len(coinlist)):#draws all coins
            camera.draw(coinlist[i])
        scoreboard = uvage.from_text(camera.topright[0]-60, camera.topright[1]+30, str(int(len(score))), 40, 'black') #defines scoreboard
        for i in heartlist:#draws hearts
            camera.draw(i)
        camera.draw(scoreboard) #draws scoreboard

        camera.draw(timer) #draws timer
        move(scoreboard,timer) #move function for scoreboard and timer
        for Goomba in goombalist_tick: #for goombas present in game, mechanics for goombas
            goombamove(Goomba,heartlist)
            mechanicsfunc(mariosprite,Goomba)
        flaginteraction(flagpole) #checks for flag interaction
        if len(interactionlist)!= 0: #flag movement to castle
            if 633<= mariosprite.center[1] <= 634 and mariosprite.touches(castleinteractor)==False:
                finalmariocordlist.append(mariosprite.center)
                mariosprite.speedx = 10
                mariosprite.move_speed()

        camera.display()
    elif mariosprite.touches(castleinteractor): #if you win the game
        camera.clear('black')
        camera.center = [7960,300]
        for item in backgroundlist:
            camera.draw(item)
        holdmario = mariosprite.copy_at(finalmariocordlist[len(finalmariocordlist)-1][0], finalmariocordlist[len(finalmariocordlist)-1][1])
        camera.draw(flag)
        camera.draw(castle)
        camera.draw(holdmario)

        finaltext = uvage.from_text(camera.center[0], camera.center[1], 'GAME OVER: YOU WON!', 100, 'pink', bold=True)
        finalscore = uvage.from_text(camera.center[0], camera.center[1] + 100, 'SCORE =' + ' ' + str(len(score)), 80,
                                     'pink', bold=True)
        camera.draw(finalscore)
        camera.draw(finaltext)
        camera.display()
    elif len(liveslist) == 3: #if you run out of lives
        camera.clear('black')
        for item in backgroundlist:
            camera.draw(item)
        holdmario = mariosprite.copy_at(finalmariocordlist[0],finalmariocordlist[1])
        camera.draw(holdmario)
        finaltext = uvage.from_text(camera.center[0],camera.center[1],'GAME OVER: YOU DIED',100,'pink',bold = True)
        finalscore = uvage.from_text(camera.center[0], camera.center[1]+100, 'SCORE ='+' '+str(len(score)), 80,'pink',bold = True)
        camera.draw(finalscore)
        camera.draw(finaltext)
        camera.display()
    elif 30-len(timersubtractlist) == 0: #if you run out of time
        camera.clear('black')
        for item in backgroundlist:
            camera.draw(item)
        holdmario = mariosprite.copy_at(finalmariocordlist[len(finalmariocordlist)-1][0], finalmariocordlist[len(finalmariocordlist)-1][1])
        finaltext = uvage.from_text(camera.center[0], camera.center[1], "GAME OVER: YOU'RE OUT OF TIME!", 100, 'pink', bold=True)
        finalscore = uvage.from_text(camera.center[0], camera.center[1] + 100, 'SCORE =' + ' ' + str(len(score)), 80,
                                     'pink', bold=True)
        camera.draw(holdmario)
        camera.draw(finalscore)
        camera.draw(finaltext)
        camera.display()
    #print(len(goombaintlist))
    print(mariosprite.touches(castleinteractor))
#timerloop
uvage.timer_loop(60,tick)