
import pygame

#Player class:
class player(object):
    def __init__(self,x,y,width,height,speed,draw_PlayerBox,charImage,walkleftImage = [],walkrightImage = []):
        self.x = x # player x position
        self.y = y # player y position
        self.width = width # player width
        self.height = height # player height

        self.vel = speed # player speed

        self.left = False # player facing left
        self.right = False # player facing right

        self.up = False

        self.walkCount = 0 # player walk count for animation

        #I made you need to initiate the images with the object, so you can call the player for other files easily:
        self.walkLeft = walkleftImage # player images
        self.walkRight = walkrightImage # player images
        self.char = charImage # player images

        self.funcOnTrigger = 0

        self.draw_PlayerBox = draw_PlayerBox

    # Updates hitbox:
    def hitbox(self,x,y, hitboxXOffset, hitboxYOffset, hitboxWidthOffset, hitboxHeightOffset, draw_PlayerBox):
        #Put all hitbox vars and stuff in here
        self.hitboxX = self.x + hitboxXOffset
        self.hitboxY = self.y + hitboxYOffset
        self.hitboxWidth = self.width - hitboxWidthOffset
        self.hitboxHeight = self.height - hitboxHeightOffset

        self.draw_PlayerBox = draw_PlayerBox
        #Make the ability to draw the hitbox be a boolean in the hitbox 
        self.rect = pygame.Rect(x, y, 50, 55) #makes player rect easy to call

    def movement(self,scrWidth,scrHeight,colliders = []):
        keys = pygame.key.get_pressed()
        x, y = self.x, self.y

        if keys[pygame.K_a] and self.x > self.vel:
            x -= self.vel
            self.left = True
            self.right = False
            self.up = False
        elif keys[pygame.K_d] and self.x < scrWidth - self.width - self.vel:
            x += self.vel
            self.right = True
            self.left = False
            self.up = False
        elif keys[pygame.K_w] and self.y > self.vel:
            y -= self.vel
            self.left = False
            self.right = False
            self.up = True
        elif keys[pygame.K_s] and self.y < scrHeight - self.height - self.vel:
            y+= self.vel
            self.left = False
            self.right = False
            self.up = False
        else:
            self.right = False
            self.left = False
            self.up = False
            self.walkCount = 0

        #self.hitbox(x,y,15, 0, 31, 17, self.draw_PlayerBox) #PLAYER HITBOX #updates player hitbox
        self.hitbox(x,y,15, 0, 31, 17, self.draw_PlayerBox) #PLAYER HITBOX #updates player hitbox

        collisions = 0
        noCollisions = 0
        for collider in colliders:
            if collider.onTrigger > 0:
                if collider.playerCollide(self.rect):
                    self.funcOnTrigger = collider.onTrigger
            if not collider.playerCollide(self.rect) or collider.onTrigger > 0:
                collisions += 1

            if not collider.playerCollide(self.rect):
                noCollisions += 1

        if collisions == len(colliders):

            self.x, self.y = x, y

        if noCollisions == len(colliders):
            self.funcOnTrigger = 0


    #Draws hitbox (i made the function because sometimes it would be helpful to call it separate).
    def drawhitbox(self,win):
        pygame.draw.rect(win,(255,0,0),(self.hitboxX, self.hitboxY + 15, self.hitboxWidth+5, self.hitboxHeight), 1)

    def draw(self, win):
        if self.walkCount + 1 >= len(self.walkLeft)*3:
            self.walkCount = 0 

        #Animation:
        if self.left and self.walkLeft != []:
            win.blit(self.walkLeft[self.walkCount//3], (self.x+ 5,self.y))
            self.walkCount += 1
        elif self.right and self.walkRight != []:
            win.blit(self.walkRight[self.walkCount//3], (self.x+ 5,self.y))
            self.walkCount +=1
        else:
            win.blit(self.char, (self.x,self.y))
        
        #Draws the hitbox, just if the user wants.
        if self.draw_PlayerBox:
           self.drawhitbox(win)

#Sprite class:
class sprite(object):
    def __init__(self,x,y,charImage):
        self.x = x # sprite x position
        self.y = y # sprite y position
        self.char = charImage # sprite image
    
    def draw(self, win):
        win.blit(self.char, (self.x, self.y))

#Wall class:
class wall(object):
    def __init__(self, x, y, width, height, drawHitbox, onTrigger = 0):
        self.x = x # walls x position
        self.y = y # walls y position
        self.width = width # walls width
        self.height = height  # walls height
        self.rect = pygame.Rect(x, y-3, width- 19, height-16) # walls rect
        self.drawHitbox = drawHitbox # If its true, it draws the wall hitbox
        self.onTrigger = onTrigger # If its true, it calls the on trigger function
    
    # draws the wall
    def draw(self,win):
        if self.drawHitbox:
            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height), 2)

    # checks if collides with the player
    def playerCollide(self, test_rect):
        return self.rect.colliderect(test_rect) # returns collision with player and wall

def redrawGameWindow(win,bg,player,sprites = [], colliders = []):
    win.blit(bg, (-50,-200))
    player.draw(win)
    for collider in colliders:
        collider.draw(win)
    for sprite in sprites:
        sprite.draw(win)
    for text in sprites:
        text.draw(win)
    pygame.display.update()

def setScreen(scrWidth,scrHeight):
    return pygame.display.set_mode((scrWidth, scrHeight))

def setTitle(title):
    return pygame.display.set_caption(title)

def loadImage(img):
    return pygame.image.load(img)

def getEvents():
    return pygame.event.get()

def quit():
    return pygame.QUIT

def clock():
    return pygame.time.Clock()

def setIcon(img):
    programIcon = pygame.image.load(img)
    pygame.display.set_icon(programIcon)

def playSound(sound):
    pygame.mixer.init()
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
