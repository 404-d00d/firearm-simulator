class Gun_BreakOpen:
    def __init__(self, barrel, hammer, firemode, barrellock, bullet, sfx):
        self.barrel = barrel
        self.hammer = hammer
        self.firemode = firemode
        self.barrellock = barrellock
        self.bullet = bullet
        self.sfx = sfx

    def changeHammer(self, Int, cock):
        self.hammer[Int] = cock

    def changeFiremode(self, mode):
        self.firemode = mode

    def altLockBarrel(self):
        if self.barrellock:
            self.barrellock = False
        else:
            self.barrellock = True
