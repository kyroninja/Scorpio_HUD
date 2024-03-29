import pygame, sys

#required before using pygame
pygame.init()

#pygame.Rect(x_coord of top left corner, y_coord of top left corner, width, height)
myRect = pygame.Rect(60, 60, 25, 25)

#colours, just a tuple
white = (255, 255, 255)
blue = (128, 128, 0)

#define the surface for using
screen = pygame.display.set_mode((1024, 600))
done = False

#centres using a dictionary
#dict.update( {key:value} )
valueText = {}
paramText = {}
unitText = {}

#image for fun
background = pygame.image.load("bkg.jpg").convert() #faster loading

#paramaters dict
params = {1: "Voltage", 2: "Fuel Presure", 3: "Load", 4: "M.A.F",
          5: "Engine Temp", 6: "RPM", 7: "Speed",
          8: "Barometric", 9: "Air Intake", 10: "Intake Manifold", 11: "Boost"
          }

units = {1: "V", 2: "kPa", 3: "%", 4: "g/s", 5: "C", 6: "rev/min", 7: "km/h",
         8: "kPa", 9: "C", 10: "kPa", 11: "Bar"
         }

#font usage
font = pygame.font.SysFont("comicsansms", 32)

#draw background
screen.blit(background, (0, 0))

def drawGrid(surf):
    x = 0

    for i in [1, 2, 3, 4]:
        myRect1 = pygame.Rect(x, 0, 256, 175)
        paramText.update( {i : (x + 256/2, 175/10) } )
        valueText.update( {i : (x + 256/2, 175/2) } )
        unitText.update( {i : (x + 256/2, 175 - 175/7) } )
        x += 256
        pygame.draw.rect(surf, white, myRect1, 1)
        
    x = 0

    for i in [5, 6, 7]:
        myRect1 = pygame.Rect(x, 175, 341, 250)
        paramText.update( {i: (x + 341/2, 175 + 250/10)})
        valueText.update( {i : (x + 341/2, 175 + 250/2) } )
        unitText.update( {i : (x + 341/2, 375 + 250/10) } )
        x += 341
        pygame.draw.rect(surf, white, myRect1, 1)
        
    x = 0

    for i in [8, 9, 10, 11]:
        myRect1 = pygame.Rect(x, 425, 256, 175)
        paramText.update( {i: (x + 256/2, 425 + 175/10)})
        valueText.update( {i : (x + 256/2, 425 + 175/2) } )
        unitText.update( {i : (x + 256/2, 600 - 175/8) } )
        x += 256
        pygame.draw.rect(surf, white, myRect1, 1)
        
    x = 0

    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        position = valueText[i]
        newPos = ( int(position[0]), int(position[1] ))
        pygame.draw.circle(screen, white, newPos, 2)

def drawText():
    
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        textParam = font.render(params[i], True, white)
        textUnit = font.render(units[i], True, white)
        topPos = paramText[i]
        botPos = unitText[i]

        #get_rect() returns a Rect object with width and height, but
        #by specifying center = (x,y) we can center at a coordinate

        top_text = (topPos[0], topPos[1])
        bot_text = (botPos[0], botPos[1])

        text_rect_top = textParam.get_rect(center = top_text)
        text_rect_bot = textUnit.get_rect(center = bot_text)
        screen.blit(textParam, text_rect_top)
        screen.blit(textUnit, text_rect_bot)
        

drawGrid(screen)
drawText()


clock = pygame.time.Clock()
while not done:
    #get event and remove from queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
                pygame.quit()
                sys.exit()
    
    #pygame.draw.rect(screen, blue, myRect, 0) # surface, colour, rectangle object
    #update display
    pygame.display.flip()
    clock.tick(60)
