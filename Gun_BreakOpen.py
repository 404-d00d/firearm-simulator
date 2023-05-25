# simulates single barrel or multiple barrel firearms

class Gun_BreakOpen:
    #barrel, hammer, compatible ammo are arrays, firemode and barrellock are integers
    #exject variable: 0=eject always, 1=eject empties extract live, 2=extract always
    #independent hammer: 0=cock hammer when open/close, 1=hammer independent from barrel locking
    def __init__(self, barrel, hammer, firemode, barrellock, ammo, exject, indepham):
        self.barrel = barrel
        self.hammer = hammer
        self.firemode = firemode
        self.barrellock = barrellock
        self.ammo = ammo
        self.exject = exject
        self.indepham = indepham

    def changeHammer(self, Int, cock): #cock: 0 = down, 1 = half cock, 2 = cock
        self.hammer[Int] = cock

    def changeFiremode(self, mode): #dependent on gun.
        self.firemode = mode

    def getHammer(self, x): #return hammer state
        return self.hammer[x]

    def changeBarrelLock(self, x): #barrel: 0=closed, 1 & 2=partially open, 3=open
        self.barrellock = x
        if self.indepham == 1 and self.barrellock >= 2:
            for c in range(len(self.hammer)):
                self.changeHammer(c, 2)
        if self.barrellock == 3:
            if self.exject == 0:
                for a in range(len(self.barrel)):
                    for b in range(len(self.ammo)):
                        if self.barrel[a] == self.ammo[b][0]:
                            #print("remove round from chamber")
                            self.ammo[b][1] += 1
                    self.changeBarrel(a, "")
            elif self.exject == 1:
                for a in range(len(self.barrel)):
                    for b in range(len(self.ammo)):
                        if self.barrel[a] == "Spent "+self.ammo[b][0]:
                            self.changeBarrel(a, "")
                            #print("eject spent only")

    def changeBarrel(self, x, aemo):
        self.barrel[x] = aemo
        #print(self.barrel[x])

    def addRound(self, x, round):
        if self.barrellock == 3:
            if self.barrel[x] == "":
                for b in range(len(self.ammo)):
                    if self.ammo[b][0] == round:
                        self.changeBarrel(x, self.ammo[b][0])
                        self.ammo[b][1] -= 1

    def removeRound(self, x):
        if self.barrellock == 3:
            for b in range(len(self.ammo)):
                if self.barrel[x] == self.ammo[b][0]:
                    #print("remove round from chamber")
                    self.ammo[b][1] += 1
            self.changeBarrel(x, "")

    def fireBarrel(self, x):
        if self.barrellock == 0:
            #print("gun locked, ready to fire")
            if self.hammer[x] == 2:
                #print("hammer cocked, can fire")
                count = 0
                for a in range(len(self.ammo)):
                    if self.barrel[x] == self.ammo[a][0]:
                        #print("bullet fired")
                        print(self.ammo[a][2])
                        count += 1
                        self.changeBarrel(x, "Spent "+self.ammo[a][0])
                    self.changeHammer(x, 0)
                if count == 0:
                    print("KLIK")
            else:
                print("PLAP")
                #pulling trigger, just slapping metal
        else:
            print("PLAP")
            # pulling trigger, just slapping metal

