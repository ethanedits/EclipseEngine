import Eclipse

scrWidth = 1366 #1366
scrHeight = 768 #768
win = Eclipse.setScreen(scrWidth, scrHeight)
Eclipse.setIcon('Assets/EclipseLogo.png')

Eclipse.setTitle("Eclipse Engine Demo")

walkRight = [Eclipse.loadImage('Assets/R1.png'), Eclipse.loadImage('Assets/R2.png'), Eclipse.loadImage('Assets/R3.png'), Eclipse.loadImage('Assets/R4.png'), Eclipse.loadImage('Assets/R5.png'), Eclipse.loadImage('Assets/R6.png'), Eclipse.loadImage('Assets/R7.png'), Eclipse.loadImage('Assets/R8.png'), Eclipse.loadImage('Assets/R9.png')]
walkLeft = [Eclipse.loadImage('Assets/L1.png'), Eclipse.loadImage('Assets/L2.png'), Eclipse.loadImage('Assets/L3.png'), Eclipse.loadImage('Assets/L4.png'), Eclipse.loadImage('Assets/L5.png'), Eclipse.loadImage('Assets/L6.png'), Eclipse.loadImage('Assets/L7.png'), Eclipse.loadImage('Assets/L8.png'), Eclipse.loadImage('Assets/L9.png')]
bg = Eclipse.loadImage('Assets/bg.png')
char = Eclipse.loadImage('Assets/standing.png')
watermarkImg = Eclipse.loadImage('Assets/eclipsewatermark.png')
watermarkImgBlack = Eclipse.loadImage('Assets/eclipsewatermarkblack.png')

clock = Eclipse.clock()

def doOnTrigger():
	#DO WHATEVER YOU NEED WHEN IT IS ONTRIGGER:
    Eclipse.playSound("SFX/test.mp3")

def doOnTrigger2():
	#DO WHATEVER YOU NEED WHEN IT IS ONTRIGGER:
	print("Trigger2")

def doOnTrigger3():
	#DO WHATEVER YOU NEED WHEN IT IS ONTRIGGER:
	print("Trigger3")

#mainloop
man = Eclipse.player(200, 410, 60,64,3,False,char,walkLeft,walkRight)

watermarkblack = Eclipse.sprite(1040, 650, watermarkImgBlack)
watermark = Eclipse.sprite(1050, 650, watermarkImg)

#WE CREATE A LIST WITH ALL THE COLLIDERS (WALLS) WE WANT:
#last TRUE or FALSE, for on trigger or not.
colliders = [Eclipse.wall(360, 435, 200, 150,False, 1), Eclipse.wall(0,0,200, 1000,False), Eclipse.wall(590,0,160, 345,False), Eclipse.wall(590,438,160, 345,False), Eclipse.wall(1140,0, 250, 1000, False), Eclipse.wall(940,170,160,140, False)]
sprites = [Eclipse.sprite(1058, 650, watermarkImgBlack), Eclipse.sprite(1060, 650, watermarkImg)]#, Eclipse.text(100, 100, "Text Demo", 25, 255, 0, 0)]
run = True
while run:
    clock.tick(60)
    for event in Eclipse.getEvents():
        if event.type == Eclipse.quit():
            run = False
    man.movement(scrWidth,scrHeight,colliders)
    #Execute onTrigger
    if man.funcOnTrigger == 1:
    	doOnTrigger()
    elif man.funcOnTrigger == 2:
    	doOnTrigger2()
    elif man.funcOnTrigger == 3:
    	doOnTrigger3()

    Eclipse.redrawGameWindow(win,bg,man,sprites,colliders)
