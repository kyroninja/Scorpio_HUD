#import modules
import obd
from threading import Thread
import random
import time

#globals
rpm = 0
speed = 0
coolantTemp = 0
intakeTemp = 0
maf = 0
engineLoad = 0
voltage = 0
fuelPress = 0
barometricPressure = 0
boostPressure = 0
manpress = 0

#obd globals
connection = None

class ecuThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        global connection
        port = "/dev/vcom0"
        baudrate = 115200
        
        connection = obd.Async(port, baudrate, fast = False)

        #rpm
        connection.watch(obd.commands.RPM, callback=self.newRpm)
        #maf
        connection.watch(obd.commands.MAF, callback=self.newMaf)
        #voltage
        connection.watch(obd.commands.ELM_VOLTAGE, callback=self.newVolt)
        #intake air temp
        connection.watch(obd.commands.INTAKE_TEMP, callback=self.newIntake)
        #baro pressure
        connection.watch(obd.commands.BAROMETRIC_PRESSURE, callback=self.newBaro)
        #engine temp
        connection.watch(obd.commands.COOLANT_TEMP, callback=self.newEngineTemp)
        #speed
        connection.watch(obd.commands.SPEED, callback=self.newSpeed)
        #manifold pressure
        connection.watch(obd.commands.INTAKE_PRESSURE, callback=self.newManPr)
        #fuel pressure
        connection.watch(obd.commands.FUEL_PRESSURE, callback=self.newFuelPress)
        #engine load
        connection.watch(obd.commands.ENGINE_LOAD, callback=self.newLoad)

        #start connection
        connection.start()

    def newRpm(self, r):
        global rpm
        rpm = int(r.value.magnitude)

    def newMaf(self, r):
        global maf
        maf = r.value.magnitude

    def newVolt(self, r):
        global voltage
        voltage = r.value.magnitude

    def newIntake(self, r):
        global intakeTemp
        intakeTemp = r.value.magnitude

    def newBaro(self, r):
        global barometricPressure
        barometricPressure = r.value.magnitude

    def newEngineTemp(self, r):
        global coolantTemp
        coolantTemp = r.value.magnitude

    def newSpeed(self, r):
        global speed
        speed = int(round(r.value.magnitude))

    def newManPr(self, r):
        global manpress
        manpress = r.value.magnitude

    def newFuelPress(self, r):
        global fuelPress
        fuelPress = r.value.magnitude

    def newLoad(self, r):
        global engineLoad
        engineLoad = int(round(r.value.magnitude))

class Test(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
    def run(self):
        global rpm
        global speed
        global coolantTemp
        global intakeTemp
        global maf
        global engineLoad
        global voltage
        global fuelPress
        global barometricPressure
        global boostPressure
        global manpress

        while True:
            rpm = random.randrange(1, 50)
            speed = random.randrange(1, 50)
            coolantTemp = random.randrange(1, 50)
            intakeTemp = random.randrange(1, 50)
            maf = random.randrange(1, 50)
            engineLoad = random.randrange(1, 50)
            voltage = random.randrange(1, 50)
            fuelPress = random.randrange(1, 50)
            barometricPressure = random.randrange(1, 50)
            boostPressure = random.randrange(1, 50)
            manpress = random.randrange(1, 50)
            time.sleep(0.2)