#GOPUGO AUTONOMOUS, INSTANTIATED CLASS
#GoPiGo API: http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/


from gopigo import *
import time
STOP_DIST = 50

sweep = [None] * 160
cornerdistance = 10
fardistance = 90

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

    #######
    #######  ADVANCED METHODS
    #######
    
    def safeDrive(self):
        self.fwd()
        while self.keepGoing():
            self.checkDist()
        self.stop()

    def servoSweep(self):
        print "Sweeping now!"
        for ang in range(20, 160, 5):
            servo(ang)
            time.sleep(.1)

    def quickcheck(self):
        enable_servo()
        servo(70)
        time.sleep(.20)
        check1 = us_dist(15)
        servo(90)
        time.sleep(.1)
        check2 = us_dist(15)
        servo(110)
        time.sleep(.1)
        check3 = us_dist(15)
        if check1 > fardistance and check2 > fardistance and check3 > fardistance:
            print "Quick check looks good."
            disable_servo()
            return True
        else:
            print "Quick check failed. [70|",check1,"cm.][80|",check2,"cm.][90|",check3,"cm.]"
            disable_servo()
            return False

    def scan():
        while stop() == 0:
            print "Having trouble stopping"
            time.sleep(.1)
        allclear = True
        if not quickcheck():
            print "Starting a full scan."
            for ang in range(10, 160, 5):
                servo(ang)
                time.sleep(.07)
                sweep[ang] = us_dist(15)
                print "[Angle:", ang, "--", sweep[ang], "cm]"
                if sweep[ang] < fardistance and ang > 65 and ang < 95:
                    allclear = False
        
#######
#######  MAIN APP STARTS HERE
#######
carl = Pigo()
carl.quickcheck()
carl.stop()

