import pygame

pygame.init()

screen = pygame.display.set_mode([500,500])

color1 = (255,100,70)
color2 = (120,180,60)
color3 = (60,190,100)
color4 = (170,100,255)
color5 = (123,50,100)
color6 = (0,0,0)
white = (255,255,255)

screen.fill(white)

class circle:
    def __init__(self,colour,position,radius,wid = 0):
        self.colour = colour
        self.position = position
        self.radius = radius
        self.wid = wid
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.colour,self.position,self.radius,self.wid)

    def draw(self,x):
        self.radius += x
        pygame.draw.circle(self.colour,self.position,self.radius,self.wid)  

position = (300,300)
radius = 50
wid = 2
pygame.draw.circle(screen, color3, position, radius, wid ) 
pygame.display.update()

blueCircle = circle(color4, position, radius+60)
redCircle = circle(color2, position, radius+40)
yellowCircle = circle(color1, position, radius, 5)
greenCircle = circle(color5, position, 20)

while(1):
    for event in pygame.event.get():
        if (event.type == pygame .MOUSEBUTTONDOWN) :
            blueCircle.draw()
            redCircle.draw()
            yellowCircle.draw()
            greenCircle.draw()
            pygame.display.update()
        elif (event.type == pygame .MOUSEBUTTONUP) :
            blueCircle.grow(2) 
            redCircle.grow(2)
            yellowCircle.grow(2) 
            greenCircle.grow (2) 
            pygame.display.update()
        elif (event.type == pygame.MOUSEMOTION) :
            pos = pygame.mouse.get_pos()
            blackCircle = circle(color6, pos, 5)
            blackCircle.draw()
            pygame.display.update()

        elif event.type == pygame.QUIT:
            pygame.quit()





