#GOPUGO AUTONOMOUS, INSTANTIATED CLASS
#GoPiGo API: http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/


from gopigo import *
import time
STOP_DIST = 50

sweep = [None] * 160


class Pigo:

    #######
    #######  BASIC STATUS AND METHODS
    #######

    status = {'ismoving': False, 'servo': 90, 'leftspeed': 175,
              'rigthspeed': 175, 'dist': 100, }
    MIN_DIST = 90

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
        if check1 > self.MIN_DIST and check2 > self.MIN_DIST and check3 > self.MIN_DIST:
            print "Quick check looks good."
            disable_servo()
            return True
        else:
            print "Quick check failed. [70|",check1,"cm.][90|",check2,"cm.][110|",check3,"cm.]"
            disable_servo()
            return False

    def scan(self):
        while stop() == 0:
            print "Having trouble stopping"
            time.sleep(.1)
        if self.quickcheck():
            print "Starting a full scan."
            for ang in range(10, 160, 5):
                servo(ang)
                time.sleep(.07)
                sweep[ang] = us_dist(15)
                print "[Angle:", ang, "--", sweep[ang], "cm]"

    def findaPath(self):
        count = 0
        for ang in range(10, 160, 2):
            if sweep[ang] > self.MIN_DIST:
                count += 1   #count how many angles have a clear path ahead
            else:
                count = 0   #resets the counter to 0 if a obstacle is detected, we only want counts in a row
            if count >= 10:   #10 counts means 20 degrees (since I count by 2s in the loop)
                return True
        return False

#######
####### MAIN APP STARTS HERE
#######

carl = Pigo()
carl.stop()

carl.scan()
print carl.findaPath()

