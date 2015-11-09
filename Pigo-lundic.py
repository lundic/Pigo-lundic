from gopigo import *
import time
STOP_DIST = 50

class Pigo:

    #######
    #######  BASIC STATUS AND METHODS
    #######

    status = {'ismoving': False, 'servo': 90, 'leftspeed': 175,
              'rigthspeed': 175, 'dist': 100}

    def __init__(self):
        print "I'm a little robot car. beep beep."
        self.checkDist()
        
    def stop(self):
        self.status['ismoving'] = False
        print "Stoping."
        for x in range(3):
            stop()

    def fwd(self):
        self.status['ismoving'] = True
        print "Let's go!"
        for x in range(3):
            fwd()

    def bwd(self):
        self.status['ismoving'] = True
        print "Backing up, beep beep beep."
        for x in range(3):
            bwd()        
            
    def keepGoing(self):
        self.checkDist():
        if self.status['dist'] < STOP_DIST
            return False
        else:
            return Ture
    
    def checkDist(self):
        self.status['dist'] = us_dist(15)
        print "I see something " + str(self.status['dist']) + "mm away"
        
    #######
    #######  ADVANCED METHODS
    #######

    def dance(self)
        print "I just want to DANCE!"
        if self.keepGoing():
            self.circleRight()
            self.circleLeft()
            self.shuffle()
            self.servoShake()
            self.blink()
        
#######
#######  MAIN APP STARTS HERE
#######
carl = Pigo()
while carl.keepGoing():
    carl.fwd()
    distance = us_dist(15)
    while distance > 40:
        print distance
        time.sleep(.1)
        distance = us_dist(15)
    carl.stop()

carl.stop()

