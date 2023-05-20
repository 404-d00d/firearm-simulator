# simulates single barrel or multiple barrel firearms

class Gun_BreakOpen:
    def __init__(self, barrel, hammer, firemode, barrellock):
        self.barrel = barrel
        self.hammer = hammer
        self.firemode = firemode
        self.barrellock = barrellock

    def changeHammer(self, Int, cock): #cock: 0 = down, 1 = half cock, 2 = cock
        self.hammer[Int] = cock

    def changeFiremode(self, mode): #dependent on gun.
        self.firemode = mode

    def changeBarrelLock(self, x): #barrel: 0=closed, 1=partially open, 2=open
        self.barrellock = x

