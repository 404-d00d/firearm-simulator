# simulates single barrel or multiple barrel firearms
# classes that inherit it will implement conditions based on how firearm actually operates
# programs inheriting class just add flavor text to the operation of the firearm

import random


class Gun_BreakOpen:
    #barrel, hammer, compatible ammo are arrays, firemode and barrellock are integers
    #barrel is 2d array, first item is barrel contents, second item is whether barrel is blocked or not, 3rd item
    # is how long until ammo will fire if cartridge is a hang fire malfunction, 4th item is time hang fire started
    #exject variable: 0=eject always, 1=eject empties/extract live, 2=extract always
    #independent hammer: 0=cock hammer when open/close, 1=hammer independent from barrel locking
    #holdhammer and holdtrigger used for manually lowering hammer, fan fire, slam fire, fullauto functions
    #opentrigger: determines whether user can pull trigger if action is open or not, 0 = yes, 1 = no
    #cockon: determines at what stage on opening the action the gun will be cocked: 0 = cocking independed, 1-3 = stages of action
    def __init__(self, barrel, hammer, firemode, barrellock, ammo, exject, indepham, holdhammer, holdtrigger, opentrigger, cockon):
        self.barrel = barrel
        self.hammer = hammer
        self.firemode = firemode
        self.barrellock = barrellock
        self.ammo = ammo
        self.round = 0
        self.exject = exject
        self.indepham = indepham
        self.opentrigger = opentrigger
        self.holdhammer = holdhammer
        self.holdtrigger = holdtrigger
        self.cockon = cockon
        self.currentbarrel = 0
        self.secondsPassed = 0

    def clearBarrels(self):
        for x in range(len(self.barrel)):
            self.barrel[x][1] = False
            print("After handing the gun to a gunsmith to remove the squib load, the gun is now ready to fire.")

    def isBarrelBlocked(self, x):
        return self.barrel[x][1]

    def incrementSec(self, y):
        self.secondsPassed += y
        self.hangFire()

    def hangFire(self):
        for b in range(len(self.barrel)):
            # if the time between pulling the trigger and now is greater than the saved hang fire time - fire
            if self.secondsPassed - self.barrel[b][3] >= self.barrel[b][2] and self.barrel[b][2] != 0:
                for a in range(len(self.ammo)):
                    if self.barrel[b][0] == self.ammo[a][0]:
                        print(self.ammo[a][2])
                        self.changeBarrel(b, "Spent " + self.ammo[a][0])

    def getTotalSeconds(self):
        return self.secondsPassed

    def currentAmmo(self):
        print("Current ammo type: " + self.ammo[self.round][0] + " | " + str(self.ammo[self.round][1]) + " rounds")

    def changeHammer(self, Int, cock): #cock: 0 = down, 1 = half cock, 2 = cock
        self.hammer[Int] = cock

    def changeFiremode(self, mode): #dependent on gun. 0 is always ready to fire,
        self.firemode = mode

    def getFiremode(self):
        return self.firemode

    def getHammer(self, x): #return hammer state
        return self.hammer[x]

    def toggleHammer(self):
        if self.holdhammer:
            self.holdhammer = False
        else:
            self.holdhammer = True

    def toggleTrigger(self):
        if self.holdtrigger:
            self.holdtrigger = False
            print("You let go of the trigger.")
        else:
            self.holdtrigger = True
            print("You squeeze the trigger.")

    def showHToggle(self):
        return self.holdhammer

    def showTToggle(self):
        return self.holdtrigger

    def getBarrelLock(self):
        return self.barrellock

    def changeBarrelLock(self, x): #barrel: 0=closed, 1 & 2=partially open, 3=open
        self.barrellock = x
        if self.indepham == 0 and self.barrellock >= self.cockon:
            for c in range(len(self.hammer)):
                self.changeHammer(c, 2)
        if self.barrellock == 3: #if ejection is true for all or spent cartridges, play remove round
            if self.exject <= 1:
                self.removeRound(0, 0)

    def blockBarrel(self, x, trueOrNot):
        self.barrel[x][1] = trueOrNot

    def changeBarrel(self, x, aemo):
        self.barrel[x][0] = aemo
        self.barrel[x][2] = 0
        self.barrel[x][3] = 0

    def getCurrentRound(self):
        return self.round

    def prevRound(self):
        self.round -= 1
        if self.round == -1:
            self.round = len(self.ammo)-1

    def nextRound(self):
        self.round += 1
        if self.round == len(self.ammo):
            self.round = 0

    def addRound(self, x):
        if self.barrellock == 3:
            if self.barrel[x][0] == "":
                if self.ammo[self.round][1] > 0:
                    self.ammo[self.round][1] -= 1
                    self.changeBarrel(x, self.ammo[self.round][0])
                    print("You insert a live cartridge into the chamber.")
                else:
                    print("There's no more cartridges left to put into the chamber.")
            else:
                print("There's already a cartridge in the chamber.")
        else:
            print("You can't put a round into a closed chamber.")

    # y=0 autoremove, y=1 manually remove
    def removeRound(self, x, y):
        if self.barrellock == 3:
            for b in range(len(self.ammo)):
                if self.barrel[x][0] == self.ammo[b][0]:
                    self.ammo[b][1] += 1
                    if y == 1:
                        print("You remove a live cartridge from the chamber.")
                    elif self.exject == 0:
                        print("A live cartridge flies out of the chamber.")
                #selective ejection systems only kick out spent shells AFAIK - will amend once more info found
                elif self.barrel[x][0] == "Spent "+self.ammo[b][0]:
                    if y == 1:
                        print("You remove a spent cartridge from the chamber.")
                    elif self.exject <= 1:
                        print("A spent cartridge flies out of the chamber.")
                elif self.barrel[x][0] == "Dud "+self.ammo[b][0]:
                    if y == 1:
                        print("You remove a dud cartridge from the chamber.")
                    elif self.exject == 0:
                        print("A dud cartridge flies out of the chamber.")
                elif self.barrel[x][0] == "Struck "+self.ammo[b][0]:
                    if y == 1:
                        print("You remove a struck cartridge from the chamber.")
                        print("Because it's still a live round you put it somewhere where it won't explode and injure you.")
                    elif self.exject == 0:
                        print("A struck cartridge flies out of the chamber.")
                        print("Because it's still a live round you find it and put it somewhere where it won't explode and injure you.")
                elif y != 0:
                    print("There is nothing to remove.")
            self.changeBarrel(x, "")
        else:
            print("You can't remove a cartridge from a closed chamber.")

    def showBarrel(self):
        for s in range(len(self.barrel)):
            print("["+self.barrel[s][0]+"]", end=" ")
        print()

    def getAllHammer(self):
        return self.hammer

    def fireBarrel(self, x):
        if self.barrel[x][1] == True:
            print("Bad idea, that barrel seems to be blocked. \n"
                  "Don't fire unless you want to damage the gun or yourself.\n"
                  "I suggest you go back to the main menu, so that the jam will be cleared.")
        else:
            if not self.showTToggle():
                print("You pull the trigger.")
            #hammer must be cocked in order to fire properly
            if self.hammer[x] == 2:
                if self.opentrigger == 0 and self.getBarrelLock() == 0:
                    #check if ammo in barrel does not match up with ammolist, if not produce clicking noise,
                    # hammer goes down,
                    count = 0
                    for a in range(len(self.ammo)):
                        if self.barrel[x][0] == self.ammo[a][0]:
                            malfunction = random.random()
                            if malfunction < self.ammo[a][7]:
                                malftype = random.randint(0, 2)
                                # Dud rounds, powder in cartridge doesn't fire at all
                                if malftype == 0:
                                    self.changeBarrel(x, "Dud " + self.ammo[a][0])
                                # Hang fire, powder ignition is delayed, bullet will fire later
                                elif malftype == 1:
                                    self.changeBarrel(x, "Struck "+self.ammo[a][0])
                                    self.barrel[x][2] = random.uniform(0.1, 30)
                                    self.barrel[x][3] = self.secondsPassed
                                # Squib load, charge is not enough to propel bullet, bullet is stuck in barrel
                                else:
                                    print("POOOOFFFFFFFF")
                                    self.changeBarrel(x, "Spent " + self.ammo[a][0])
                                    self.blockBarrel(x, True)
                                    count += 1
                            else:
                                print(self.ammo[a][2])
                                count += 1
                                self.changeBarrel(x, "Spent "+self.ammo[a][0])
                    if count == 0:
                        print("KLIK")
                    self.changeHammer(x, 0)
                elif self.opentrigger == 1:
                    print("KLIK")
                    self.changeHammer(x, 0)
                else:
                    if not self.showTToggle():
                        print("PLAP")
            else:
                print("PLAP")
                #pulling trigger, just slapping metal
            if not self.showTToggle():
                print("After you pulled the trigger, you let go of it.")
