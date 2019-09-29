import pygame
import pygame.gfxdraw
import math

class createDialGauge:
    
    def __init__(self, screen, rectX, rectY, minValue, maxValue, angleMin, angleMax, dialColour, needleColour, needleSize, locX, locY, bkg=None):
        #initial variables
        self.minValue = minValue
        self.maxValue = maxValue
        self.dialColour = dialColour
        self.needleColour = needleColour
        self.angleMin = angleMin
        self.angleMax = angleMax
        self.rectX = rectX
        self.rectY = rectY
        self.locX = locX
        self.locY = locY
        self.screen = screen
        self.bkg = bkg

        dialCenterX = int(rectX / 2)
        dialCenterY = int(rectY / 2)
        self.dialCenter = (dialCenterX, dialCenterY)
        self.dialRadius = int(self.rectY / 2)

        needleCenterX = int(rectX / 2)
        needleCenterY = int(rectY / 2)
        self.needleCenter = (needleCenterX, needleCenterY)
        self.needleRadius = needleSize

        self.pySurface = pygame.Surface((self.rectX, self.rectY), pygame.SRCALPHA, 32)
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def update(self, value):
        #mapping function
        mapValue = math.radians((value - self.minValue) * (self.angleMax - self.angleMin) / (self.maxValue - self.minValue) + self.angleMin)

        x1 = (self.dialRadius - int(self.rectX / 10)) * math.cos(mapValue) + self.dialCenter[0]
        y1 = (self.dialRadius - int(self.rectY / 10)) * math.sin(mapValue) + self.dialCenter[1]

        x2 = -1 * self.needleRadius * math.sin(mapValue) + self.needleCenter[0]
        y2 = self.needleRadius * math.cos(mapValue) + self.needleCenter[1]

        x3 = self.needleRadius * math.sin(mapValue) + self.needleCenter[0]
        y3 = -1 * self.needleRadius * math.cos(mapValue) + self.needleCenter[1]

        self.points = [ (x1, y1), (x2, y2), (x3, y3) ]
        self.pySurface.fill( (0, 0, 0, 0) )

        semiRect = pygame.Rect(0, 0, self.rectX, self.rectY)

        tValue = self.font.render(str(value), True, (255, 255, 255, 255))

        if self.bkg is not None:
            self.background = pygame.image.load(self.bkg) #faster loading
            self.background = pygame.transform.scale(self.background, (self.rectX, self.rectY))
            self.pySurface.blit(self.background, (0, 0))
            self.pySurface.blit(tValue, (self.needleCenter[0], self.needleCenter[1] + self.rectY / 4))

        pygame.gfxdraw.aacircle(self.pySurface, self.needleCenter[0], self.needleCenter[1], self.needleRadius, self.needleColour)
        pygame.gfxdraw.aacircle(self.pySurface, self.dialCenter[0], self.dialCenter[1], self.dialRadius, self.dialColour)
        pygame.gfxdraw.aapolygon(self.pySurface, self.points, self.needleColour)
        #pygame.draw.arc(self.pySurface, self.dialColour , semiRect, math.radians(self.angleMin - 180), math.radians(self.angleMax - 180), 5)
        
        self.screen.blit(self.pySurface, (self.locX, self.locY))
