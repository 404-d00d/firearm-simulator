# simulates single barrel or multiple barrel firearms
# classes that inherit it will implement conditions based on how firearm actually operates
# programs inheriting class just add flavor text to the operation of the firearm


class Gun_BreakOpen:
    #barrel, hammer, compatible ammo are arrays, firemode and barrellock are integers
    #exject variable: 0=eject always, 1=eject empties/extract live, 2=extract always
    #independent hammer: 0=cock hammer when open/close, 1=hammer independent from barrel locking
    #holdhammer and holdtrigger used for manually lowering hammer, fan fire, slam fire, fullauto functions
    #opentrigger: determines whether user can pull trigger if action is open or not, 0 = yes, 1 = no
    def __init__(self, barrel, hammer, firemode, barrellock, ammo, exject, indepham, holdhammer, holdtrigger, opentrigger):
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

    def currentAmmo(self):
        print("Current ammo type: " + self.ammo[self.round][0] + " | " + str(self.ammo[self.round][1]) + " rounds")

    def changeHammer(self, Int, cock): #cock: 0 = down, 1 = half cock, 2 = cock
        self.hammer[Int] = cock

    def changeFiremode(self, mode): #dependent on gun.
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
            print("You let go of the trigger")
        else:
            self.holdtrigger = True
            print("You hold down the trigger")

    def showHToggle(self):
        return self.holdhammer

    def showTToggle(self):
        return self.holdtrigger

    def getBarrelLock(self):
        return self.barrellock

    def changeBarrelLock(self, x): #barrel: 0=closed, 1 & 2=partially open, 3=open
        self.barrellock = x
        if self.indepham == 0 and self.barrellock >= 2:
            for c in range(len(self.hammer)):
                self.changeHammer(c, 2)
        if self.barrellock == 3:
            if self.exject == 0:
                for a in range(len(self.barrel)):
                    self.removeRound(0, 0)
                    print("A live cartridge flies out of the chamber")
            elif self.exject == 1:
                for a in range(len(self.barrel)):
                    for b in range(len(self.ammo)):
                        if self.barrel[a] == "Spent "+self.ammo[b][0]:
                            self.removeRound(0, 0)
                            print("A spent cartridge flies out of the chamber")

    def changeBarrel(self, x, aemo):
        self.barrel[x] = aemo
        #print(self.barrel[x])

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
        if self.barrellock == 3 and self.barrel[x] == "" and self.ammo[self.round][1] > 0:
            self.ammo[self.round][1] -= 1
            self.changeBarrel(x, self.ammo[self.round][0])
            print("You insert a live cartridge into the chamber.")

    # y=0 autoremove, y=1 manually remove
    def removeRound(self, x, y):
        if self.barrellock == 3:
            for b in range(len(self.ammo)):
                if self.barrel[x] == self.ammo[b][0]:
                    #print("remove round from chamber")
                    self.ammo[b][1] += 1
                    if y == 1:
                        print("You remove a live cartridge from the chamber.")
                elif self.barrel[x] == "Spent "+self.ammo[b][0] and y == 1:
                    print("You remove a spent cartridge from the chamber.")
            self.changeBarrel(x, "")

    def showBarrel(self):
        for s in range(len(self.barrel)):
            print("["+self.barrel[s]+"]", end=" ")
        print()

    def getAllHammer(self):
        return self.hammer

    def fireBarrel(self, x):
        if self.hammer[x] == 2:
            if self.opentrigger == 0 and self.getBarrelLock() == 0:
                #print("hammer cocked, can fire")
                count = 0
                for a in range(len(self.ammo)):
                    if self.barrel[x] == self.ammo[a][0]:
                        #print("bullet fired")
                        print("You pull the trigger.")
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
                print("PLAP")
        else:
            print("PLAP")
            #pulling trigger, just slapping metal
