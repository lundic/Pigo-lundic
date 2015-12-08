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
              'rigthspeed': 175, 'dist': 100, "wentleft": True}
    MIN_DIST = 90
    vision = [None] * 180
    STEPPER = 5

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
            print "Quick check failed. [70|"+ str(check1) + "cm.][90|" + str(check2) + "cm.][110|" + str(check3) +"cm.]"
            disable_servo()
            return False

    def scan(self):
        if not self.quickcheck():
            print "Starting a full scan."
            for ang in range(10, 160, self.STEPPER):
                servo(ang)
                time.sleep(.07)
                sweep[ang] = us_dist(15)
                print "[Angle:", ang, "--", sweep[ang], "cm]"

    def findaPath(self):
        count = 0
        for ang in range(10, 160, self.STEPPER):
            if sweep[ang] > self.MIN_DIST:
                count += 1   #count how many angles have a clear path ahead
            else:
                count = 0   #resets the counter to 0 if a obstacle is detected, we only want counts in a row
            if count >= (20/self.STEPPER):   #10 counts means 20 degrees (since I count by 2s in the loop)
                print "The findaPath method has got an angle at " + str(ang - 10)
                return True
        return False

    def findAngle(self):
        counter = 0
        option = [] * 10  #we're going to fill this array with the angles of open paths
        optindex = 0  #this starts at 0 and will increase every time we find an option
        for ang in range(20, 160, self.STEPPER):
            if sweep[ang] > self.MIN_DIST:
                counter += 1
            else:
                counter = 0
            if counter >= (20/self.STEPPER):
                print "We've found an option at angle " + str(ang - 10)
                counter = 0
                return ang - 10
                option[0] = (ang - 10)
                optindex += 1
        if self.status['wentleft']:
            print "I went left last time. Seeing if I have a right turn option"
            for choice in option:
                print choice
                if choice < 90:
                    self.status['wentleft'] = False #switch this for next time
                    return choice
        else:
            print "Went right last time. Seeing if there's a left turn option"
            for choice in option:
                if choice > 90:
                    self.status['wentleft'] = True
                    return choice
        if option[0]:
            print "I couldn't turn the direction I wanted. Going to use angle " + str(option[0])
            return option[0]
        print "If I print this line I couldn't find an angle. How'd I get this far? I give up."
        return 90

    def turnTo(self, angle):
        if angle < 90:
            print "Turning right"
            self.rightrot()
            time.sleep(turntime)
            self.stop()
        else:
            print "Turning left"
            self.leftrot()
            time.sleep(turntime)
            self.stop()

#######
####### MAIN APP STARTS HERE
#######

carl = Pigo()
carl.stop()

carl.scan()
print carl.findaPath()
print carl.findAngle()

