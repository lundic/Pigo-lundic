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
        if self.status['dist'] < STOP_DIST:
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
        print "Circling left"
        for x in range(2):
            left()
        time.sleep(1)
        self.stop()

    def circleRight(self):
        print "Circling right"
        for x in range(2):
            right()
        time.sleep(1)
        self.stop()

    def shuffle(self):
        print "Time to shuffle"
        for x in range(2):
            left_rot()
            right_rot()
        time.sleep(1)
        self.stop()

    def servoShake(self):
        print "servo shaking"
        for x in range(2):
            servo(40)
            time.sleep(1)
            servo(120)
        self.stop()

    def blink(self):
        print "blinking"
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

    def servoSweep(self):
        for ang in range(20, 160, 5):
            servo(ang)
            time.sleep(.1)

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
carl.dance()

carl.stop()

