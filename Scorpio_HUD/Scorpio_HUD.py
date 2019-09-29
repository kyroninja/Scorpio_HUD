import pygame
import ecu #obd stuff
import time, sys

#required before using pygame
pygame.init()

#init obd comms
time.sleep(1)
#ecu.ecuThread()
ecu.Test()

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

units = {1: "V", 2: "kPa", 3: "%", 4: "g/s", 
         5: "°C", 6: "rev/min", 7: "km/h",
         8: "kPa", 9: "°C", 10: "kPa", 11: "Bar"
         }

values = {}

#font usage
fontText = pygame.font.SysFont("comicsansms", 32) #font name, size
fontValue = pygame.font.SysFont("comicsansms", 64)

def drawGrid(surface):
    x = 0

    for i in [1, 2, 3, 4]:
        myRect1 = pygame.Rect(x, 0, 256, 175)
        paramText.update( {i : (x + 256/2, 175/10) } )
        valueText.update( {i : (x + 256/2, 175/2) } )
        unitText.update( {i : (x + 256/2, 175 - 175/7) } )
        x += 256
        pygame.draw.rect(surface, white, myRect1, 1)
        
    x = 0

    for i in [5, 6, 7]:
        myRect1 = pygame.Rect(x, 175, 341, 250)
        paramText.update( {i: (x + 341/2, 175 + 250/10)})
        valueText.update( {i : (x + 341/2, 175 + 250/2) } )
        unitText.update( {i : (x + 341/2, 375 + 250/10) } )
        x += 341
        pygame.draw.rect(surface, white, myRect1, 1)
        
    x = 0

    for i in [8, 9, 10, 11]:
        myRect1 = pygame.Rect(x, 425, 256, 175)
        paramText.update( {i: (x + 256/2, 425 + 175/10)})
        valueText.update( {i : (x + 256/2, 425 + 175/2) } )
        unitText.update( {i : (x + 256/2, 600 - 175/8) } )
        x += 256
        pygame.draw.rect(surface, white, myRect1, 1)
        
    x = 0

    #center positions
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        position = valueText[i]
        newPos = ( int(position[0]), int(position[1] ))
        #pygame.draw.circle(surface, white, newPos, 2)

def drawText():
    
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
        textParam = fontText.render(params[i], True, white)
        textUnit = fontText.render(units[i], True, white)
        textValue = fontValue.render(values[i], True, white)
        topPos = paramText[i]
        botPos = unitText[i]
        cenPos = valueText[i]

        #get_rect() returns a Rect object with width and height, but
        #by specifying center = (x,y) we can center at a coordinate

        top_text = (topPos[0], topPos[1])
        bot_text = (botPos[0], botPos[1])
        cen_text = (cenPos[0], cenPos[1])

        text_rect_top = textParam.get_rect(center = top_text)
        text_rect_bot = textUnit.get_rect(center = bot_text)
        text_rect_cen = textValue.get_rect(center = cen_text)

        screen.blit(textParam, text_rect_top)
        screen.blit(textUnit, text_rect_bot)
        screen.blit(textValue, text_rect_cen)

def drawBackground(surface):
    surface.fill((0,0,0))
    surface.blit(background, (0, 0))
        
def getValues():
    global values
    values = {
        1: str(ecu.voltage), 2: str(ecu.fuelPress), 3: str(ecu.engineLoad), 4: str(ecu.maf),
        5: str(ecu.coolantTemp), 6: str(ecu.rpm), 7: str(ecu.speed),
        8: str(ecu.barometricPressure), 9: str(ecu.intakeTemp), 10: str(ecu.manpress), 11:str(round(ecu.manpress - ecu.barometricPressure, 2))
        }

clock = pygame.time.Clock()
while not done:

    #get event and remove from queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    #pygame.draw.rect(screen, blue, myRect, 0) # surface, colour, rectangle object
    
    #update values
    getValues()

    #update display
    drawBackground(screen)
    drawGrid(screen)
    drawText()

    pygame.display.flip()
    clock.tick(60)