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
        while stop() == -1:
            time.sleep(.1)
            print "Ummm, yeah I can't stop!"

    def fwd(self):
        self.isMoving = True
        while fwd() == -1:
            time.sleep(.1)
            print "Hey, I can't seem to get moving"

    #######
    #######  ADVANCED METHODS
    #######

#######
#######  MAIN APP STARTS HERE
#######

tina = Pigo()
tina.fwd()
while us_dist(15) > 40:
    print "Weeeeeeeeeeee"
    time.sleep(.1)
tina.stop()
