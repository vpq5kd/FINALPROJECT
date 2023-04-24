
#Sophia Spaner, VPQ5KD
#CS1111
#Last Edited: 4/19/2023
#Purpose: To use UVAGE to create a simple falldown game
#Imports:
import uvage
import random
#Camera:
camera = uvage.Camera(800,600)
camera.center = [400,300]
#Globals:
global boundaries
boundaries = []
global score
score = []
#Functions:
#Line creation function:
def lines():

    for i in range(0,80000,100): #creates 800 lines for fall down, very low probability they'll reach the end. If they do, they win.
        randomx = random.randint(100, 700) #creates random sized lines
        line1 = uvage.from_color((randomx / 2), i, 'red', randomx, 40)

        line2randomx = 840 - randomx
        line2 = uvage.from_color(875 - (line2randomx / 2), i, 'red', 785 - randomx, 40)
        boundarieslist = [line1,line2] #appends the 'line', in a form of a nested list, to a large list used for iteration later.
        boundaries.append(boundarieslist)

lines() #calls the line function, creates all of the lines for the game
moveablebox = uvage.from_color(400,260, 'pink', 40,40) #creates the box
#Tick Function:
def tick():

    if len(boundaries) != 0: #test to make sure that the game isn't over
        score.append(1) #adds a number into the score list, len of score list is used to get the score.
        camera.clear('black') #clears for each frame
        #if uvage.is_pressing('down arrow'):
            #camera.move(0,10)
        for i in range(0,len(boundaries)): #draws all the lines from the list
            camera.draw(boundaries[i][0])
            camera.draw(boundaries[i][1])
        camera.draw(moveablebox) #draws the box
        c=0 #number used to test if the box is on the given line
        for i in range(0,len(boundaries)):
            if boundaries[i][0].top_touches(moveablebox) or boundaries[i][1].top_touches(moveablebox):
                c += i #figures out which line the box is touching
                #print('true')

        if boundaries[c][0].top_touches(moveablebox) == False and boundaries[c][1].top_touches(moveablebox) == False: #checks if the box is in the gap
            moveablebox.move(0,20) #drops the box down if it's in the gap

        if uvage.is_pressing('right arrow'): #left and right arrow tests which move the box
            if moveablebox.right != camera.right: #makes sure that the box can't go beyond the bounds of the camera
                moveablebox.speedx = 5
                moveablebox.move_speed()
            elif moveablebox.right == camera.right:
                moveablebox.speedx = 0
                moveablebox.move_speed()
        if uvage.is_pressing('left arrow'):
            if moveablebox.left != camera.left:
                moveablebox.speedx = -5
                moveablebox.move_speed()
            elif moveablebox.right == camera.left:
                moveablebox.speedx = 0
                moveablebox.move_speed()
        camera.move(0,2) #keeps the blocks 'moving' (relatively) prepetually

        midscore = len(score) #gets the score
        scoreboard = uvage.from_text(camera.center[0],camera.center[1],str(midscore),40,'white')
        camera.draw(scoreboard) #draws the score in the middle of the camera
        camera.display()
        if moveablebox.top == camera.top: #triggers the kill protocol if the box touches the top of the camera
            camera.clear('black')
            boundaries.clear() #clears boundaries, tested at the beginning of each tick
            camera.display()
    elif moveablebox.center[1]+20 == 79920 : #only triggers if one makes it to the end of the lines
        camera.clear('black')
        gameover = uvage.from_text(camera.center[0], camera.center[1] - 100, 'GAME OVER: YOU MADE IT TO THE END!', 60,
                                   'pink', bold=True)
        midscore = len(score)
        scoreboard = uvage.from_text(camera.center[0], camera.center[1], 'FINAL SCORE:' + ' ' + str(midscore), 40,
                                     'pink', bold=True)
        camera.draw(scoreboard)
        camera.draw(gameover)
        camera.display()
    else: #game over screen if you loose
        camera.clear('black')
        gameover = uvage.from_text(camera.center[0],camera.center[1]-100,'GAME OVER: at least you tried :)',60,'pink',bold=True)
        midscore = len(score)
        scoreboard = uvage.from_text(camera.center[0],camera.center[1],'FINAL SCORE:'+' '+str(midscore),40,'pink',bold=True)
        camera.draw(scoreboard)
        camera.draw(gameover)
        camera.display()

    #print(score)
uvage.timer_loop(60, tick) #tick call



