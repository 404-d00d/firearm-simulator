# simulates single barrel or multiple barrel firearms

class Gun_BreakOpen:
    #barrel, hammer, compatible ammo are arrays, firemode and barrellock are integers
    def __init__(self, barrel, hammer, firemode, barrellock, ammo):
        self.barrel = barrel
        self.hammer = hammer
        self.firemode = firemode
        self.barrellock = barrellock
        self.ammo = ammo

    def changeHammer(self, Int, cock): #cock: 0 = down, 1 = half cock, 2 = cock
        self.hammer[Int] = cock

    def changeFiremode(self, mode): #dependent on gun.
        self.firemode = mode

    def changeBarrelLock(self, x): #barrel: 0=closed, 1=partially open, 2<=open
        self.barrellock = x

    def changeBarrel(self, x, aemo):
        self.barrel[x] = aemo
        #print(self.barrel[x])

    def addRound(self, x, round):
        if self.barrellock == 2:
            if self.barrel[x] == "":
                for b in range(len(self.ammo)):
                    if self.ammo[b][0] == round:
                        self.changeBarrel(x, self.ammo[b][0])
                        self.ammo[b][1] -= 1

    def removeRound(self, x):
        if self.barrellock == 2:
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


