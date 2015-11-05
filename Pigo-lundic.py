from gopigo import *
import time

class Pigo:

    #######
    #######  BASIC STATUS AND METHODS
    #######

    status = {'ismoving': False, 'servo': 90, 'leftspeed': 175,
              'rigthspeed': 175}

    def __init__(self):
        print "I'm a little robot car. beep beep."

    def stop(self):
        self.isMoving = False
        for x in range(3):
            stop()

    def fwd(self):
        self.isMoving = True
        for x in range(3):
            fwd()
        

    #######
    #######  ADVANCED METHODS
    #######

#######
#######  MAIN APP STARTS HERE
#######

tina = Pigo()
tina.fwd()
distance = us_dist(15)
while distance > 40:
    print distance
    time.sleep(.1)
    distance = us_dist(15)
tina.stop()
