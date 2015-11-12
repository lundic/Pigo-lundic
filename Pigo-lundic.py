#GOPUGO AUTONOMOUS, INSTANTIATED CLASS
#GoPiGo API: http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/


from gopigo import *
import time
STOP_DIST = 50

class Pigo:

    #######
    #######  BASIC STATUS AND METHODS
    #######

    status = {'ismoving': False, 'servo': 90, 'leftspeed': 175,
              'rigthspeed': 175, 'dist': 100, }

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
    #Check if conditions are safe to continue operating
    def keepGoing(self):
        if self.status['dist'] < STOP_DIST
            print "Obstable detected. Stopping"
            return False
        elif volt() > 14 or volt() < 6:
            print "Unsafe voltage detected: " + str(volt())
            return False
        else:
            return True

    def checkDist(self):
        self.status['dist'] = us_dist(15)
        print "I see something " + str(self.status['dist']) + "mm away"
        if not self.keepGoing():
            print "EMERGENCY STOP FROM THE CHECK DISTANCE METHOD!"
            self.stop()

    def circleLeft(self):
        for x in range(1):
            left()
        time.sleep(0.6)
        self.stop()

    def circleRight(self):
        for x in range(1):
            right()
        time.sleep(0.6)
        self.stop()

    def shuffle(self):
        for x in range(2):
            left_rot()
            right_rot()
        time.sleep(0.5)
        self.stop()

    def servoShake(self):
        for x in range(40,60):
            servo(x)
            time.sleep(.1)]
        #time.sleep(0.1)
        self.stop


    def blink(self):
        for x in range(4):
            led_on(1)
            time.sleep(0.3)
            led_off(1)
        self.stop()

    #######
    #######  ADVANCED METHODS
    #######
    
    def safeDrive(self):
        self.fwd()
        while self.keepGoing():
            self.checkDist()
        self.stop()

    def dance(self):
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

