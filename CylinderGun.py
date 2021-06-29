##NOTE:
##YOU MUST COPY EVERYTHING BELOW THIS INTO A PYTHON FILE BEFORE PLACING THE GUN CODE FOR TESTING

class CylinderGun:
    def __init__(self, hammer, cylinder, capacity, rounds, bullet, SFX, term, triggerdown, firemode):
        self.hammer = hammer #status of the hammer, integer (0 = decocked, 0< = cocked)
        self.cylinder = cylinder #Checks if cylinder or barrel is closed, boolean
        self.capacity = capacity #How much the gun can hold. list
        self.rounds = rounds #number of rounds available for gun to use, list of integers
        self.bullet = bullet #name of cartridge gun is chamberred in, list of strings
        self.SFX = SFX #sound the gun makes when fired, list of strings
        self.term = term #refers to how to describe where to put the bullets in, string
        self.triggerdown = triggerdown #checks if trigger is held down, boolean
        self.firemode = firemode #determines firemode for the gun (including safety), integer

    def ejectAllRounds(self):
        for x in range(len(self.capacity)):
            for y in range(len(self.bullet)):
                if self.capacity[x] == self.bullet[y]:
                    self.rounds[y] += 1
                self.capacity[x] = ""

    def ejectOneRound(self, x):
        for y in range(len(self.bullet)):
            if self.capacity[x] == self.bullet[y]:
                self.rounds[y] += 1
            self.capacity[x] = ""

    def cylinderLeft(self):
        self.capacity.append(self.capacity[0])
        self.capacity.pop(0)

    def cylinderRight(self):
        self.capacity.insert(0, self.capacity[len(self.capacity)-1])
        self.capacity.pop(len(self.capacity)-1)

    def showCylinder(self):
        print(self.capacity)

    def openCylinder(self):
        self.cylinder = False

    def closeCylinder(self):
        self.cylinder = True

    def pullTrigger(self, y, z): #ALWAYS SET Z TO ZERO
        print("You pull the trigger")
        for x in range(len(self.bullet)):
            if self.capacity[y] == self.bullet[x]:
                self.capacity[y] = "Spent "+self.bullet[x]
                print(self.SFX[x])
                z += 1
        if z == 0:
            print("*KLICK*")

    def cockHammer(self, x):
        self.hammer = x

    def addRound(self, x, y):
        if not self.cylinder:
            if self.rounds[y] > 0:
                if self.capacity[x] == "":
                    print("You insert a round into the "+self.term)
                    self.capacity[x] = self.bullet[y]
                    self.rounds[y] -= 1
                else:
                    print("The "+self.term+" is full")
            else:
                print("There is no ammo left")
        else:
            print("You can't insert a round in this state")

    def showCylinder(self):
        return self.capacity

    def showLatch(self):
        return self.cylinder

    def showCount(self, x):
        return self.rounds[x]

    def showBullet(self, x):
        return self.bullet[x]

    def showHammer(self):
        return self.hammer

    def showTerm(self):
        return self.term

    def showSFX(self):
        return self.SFX

    def showRound(self, specCyl):
        return self.capacity[specCyl]

    def showFiremode(self):
        return self.firemode

    def changeMode(self, x):
        if x == 0:
            if self.firemode == 0:
                self.firemode = 1
            else:
                self.firemode = 0
        elif x > 1:
            if self.firemode < x:
                self.firemode += 1
            else:
                self.firemode = 0

    def alternateMode(self, x):
        self.firemode = x

    def holdTrigger(self):
        if self.triggerdown:
            self.triggerdown = False
        else:
            self.triggerdown = True

    def triggerDown(self):
        return self.triggerdown
