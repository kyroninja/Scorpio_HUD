import pygame
import pygame.gfxdraw
import math
import time
from dialGauge import createDialGauge
import ecu
import subprocess

RED = pygame.Color(255, 0, 0, 255)
BLUE = pygame.Color(0, 0, 255, 128)

done = False

process = subprocess.Popen(['socat', 'pty,link=/home/pi/wifiserial,waitslave', 'tcp:192.168.0.10:35000'])
ecu.ecuThread()

pygame.init()
screen1 = pygame.display.set_mode((1024,600))

rpm = createDialGauge(screen1, 256, 256, 0, 7000, 135, 405, BLUE, RED, 10, 0, 0, "tachometer_back.png")
boost = createDialGauge(screen1, 256, 256, 0,  105, 180, 405, BLUE, RED, 10, 256, 0, "tachometer_back.png")
maf = createDialGauge(screen1, 256, 256, 0,  300, 135, 405, BLUE, RED, 10, 512, 0, "tachometer_back.png")
fuel = createDialGauge(screen1, 256, 256, 0,  250, 135, 405, BLUE, RED, 10, 768, 0, "tachometer_back.png")
intake = createDialGauge(screen1, 256, 256, 0,  105, 135, 405, BLUE, RED, 10, 0, 256, "tachometer_back.png")
coolant = createDialGauge(screen1, 256, 256, 0,  150, 135, 405, BLUE, RED, 10, 256, 256, "tachometer_back.png")
load = createDialGauge(screen1, 256, 256, 0,  100, 135, 405, BLUE, RED, 10, 512, 256, "tachometer_back.png")

clock = pygame.time.Clock()

while not done:

    #get event and remove from queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    image = pygame.image.load("bkg.jpg").convert()
    screen1.blit(image, (0,0))

    rpm.update(ecu.rpm)
    boost.update(ecu.boostPressure)
    maf.update(ecu.maf)
    fuel.update(ecu.fuelPress)
    intake.update(ecu.intakeTemp)
    coolant.update(ecu.coolantTemp)
    load.update(ecu.engineLoad)

    pygame.display.update()
    clock.tick(60)
