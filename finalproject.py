import uvage
import random
camera = uvage.Camera(1920,1080)
camera.center = [400,300]
global backgroundlist
backgroundlist = []
global bricklist
bricklist = []
global speedlist
speedlist = []
for i in range(0,101):
    c = (400+(i*1920))
    background = uvage.from_image(c,300, 'mariobackground.jpg')
    backgroundlist.append(background)
for i in range(0, 101):
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
    bricklist.append(nestedbricklist2)
mariosprite = uvage.from_image(400,630,'mariosprite.png')
mariosprite.scale_by(.3)
bottomborder = uvage.from_color(-500,730, 'black', 10000, 10)
def jump():

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
def trialjump():
    if mariosprite.bottom_touches(bottomborder):
        if uvage.is_pressing('space'):
            mariosprite.speedy = -35
    mariosprite.speedy +=1.25
    mariosprite.move_speed()
    mariosprite.move_to_stop_overlapping(bottomborder)







def tick():

    if uvage.is_pressing('right arrow'):
        mariosprite.move(13,0)
        camera.move(9,0)
    if uvage.is_pressing('left arrow'):
        mariosprite.move(-10,0)
    camera.draw(bottomborder)
    for i in range(0,101):
        camera.draw(backgroundlist[i])
    for i in range(0,3):
        camera.draw(bricklist[5][i])

    camera.draw(mariosprite)
    #jump()
    trialjump()
    for i in range(0,3):
        if bricklist[5][i].top_touches(mariosprite,-40):
            mariosprite.move_to_stop_overlapping(bricklist[5][i],-40)
            mariosprite.move(0,120)
    camera.display()
    print(mariosprite.speedy)
    print(mariosprite.center)
uvage.timer_loop(30,tick)