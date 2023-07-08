from Gun_BreakOpen import Gun_BreakOpen
from Ammunition import magnum357, special38

ammo = magnum357 + special38

#Barrels 1=top right, 2=bottom right, 3=bottom left, 4=top right

COP357 = Gun_BreakOpen([["", False, 0, 0], ["", False, 0, 0], ["", False, 0, 0], ["", False, 0, 0]], [0, 0, 0, 0], 0, 0,
                       ammo, 2, 1, False, False, 0, 0)

# COP shoots barrels in clockwise order

def moveLeft():
    if COP357.getCurrentBarrel() == 0:
        COP357.changeCurrentBarrel(3)
    else:
        COP357.changeCurrentBarrel(COP357.getCurrentBarrel()-1)


def moveRight():
    if COP357.getCurrentBarrel() == 3:
        COP357.changeCurrentBarrel(0)
    else:
        COP357.changeCurrentBarrel(COP357.getCurrentBarrel()+1)


def main():
    presentBarrel = 3
    if COP357.isBarrelBlocked(0) or COP357.isBarrelBlocked(1) or COP357.isBarrelBlocked(2) or COP357.isBarrelBlocked(3):
        COP357.clearBarrels()
    act = ""
    while act != "@":
        print("-" * 50)
        print("The COP .357 Pistol is a 4 barrel derringer chambered in .357 Magnum, and can also accept\n"
              ".38 Special. The name is an acronym that stands for Compact Off-Duty Police, because this pistol\n"
              "was meant to be sold to off duty police officers as a backup sidearm. It was not popular among that\n"
              "market due to its weight and its very heavy double action trigger pull. The pistol is double action\n"
              "only, and will fire the barrels in clockwise order. It is possible to pull the trigger while the\n"
              "action is open, and opening the action will not eject any spent or live cartridges in the barrels.")
        print("-" * 50)
        print("Compact Off-duty Police 357 Derringer | .38 Special/.357 Magnum")
        print("| = hold trigger/release trigger")
        print("/ = yank trigger")
        print("t/T = open barrels, partial/fully")
        print("b = close barrels")
        print("y/Y = insert round, remove round")
        print("{,} = next/previous ammo type")
        print("[,] = change barrel to load/unload")
        print("@ = exit program")
        COP357.currentAmmo()
        print("-" * 50)
        print("hold trigger: " + str(COP357.showTToggle()))
        if COP357.getBarrelLock() >= 2:
            COP357.showBarrel()
            if COP357.getCurrentBarrel() == 0:
                print("Remove/insert round in top right barrel")
            elif COP357.getCurrentBarrel() == 1:
                print("Remove/insert round in bottom right barrel")
            elif COP357.getCurrentBarrel() == 2:
                print("Remove/insert round in bottom left barrel")
            elif COP357.getCurrentBarrel() == 3:
                print("Remove/insert round in top left barrel")
        act = input("CMD: ")
        for a in range(len(act)):
            if act[a] == "[":
                if COP357.getBarrelLock() == 3:
                    moveLeft()
            if act[a] == "]":
                if COP357.getBarrelLock() == 3:
                    moveRight()
            elif act[a] == "|":
                COP357.toggleTrigger()
                if COP357.showTToggle():
                    moveRight()
                    presentBarrel = COP357.getCurrentBarrel()
                    COP357.changeHammer(presentBarrel, 2)
                    COP357.fireBarrel(presentBarrel)
            elif act[a] == "t":
                if COP357.getBarrelLock() == 0:
                    COP357.changeBarrelLock(2)
                    print("You pull back the top button/rear sight, and break open the barrels slightly.")
                    print("The gun is partially open.")
            elif act[a] == "T":
                if COP357.getBarrelLock() < 3:
                    print("You pull back the top button/rear sight, and break open the barrels fully.")
                    print("The gun is fully open.")
                    COP357.changeBarrelLock(3)
                else:
                    print("The gun is already fully open.")
            elif act[a] == "b":
                if COP357.getBarrelLock() != 0:
                    COP357.changeBarrelLock(0)
                    print("You close up the barrels, and thus close the action of the gun.")
                else:
                    print("The action is already closed.")
            elif act[a] == "/":
                if not COP357.showTToggle():
                    moveRight()
                    presentBarrel = COP357.getCurrentBarrel()
                    COP357.changeHammer(presentBarrel, 2)
                    COP357.fireBarrel(presentBarrel)
            elif act[a] == "y":
                COP357.addRound(COP357.getCurrentBarrel())
            elif act[a] == "Y":
                COP357.removeRound(COP357.getCurrentBarrel(), 1)
            elif act[a] == "{":
                COP357.prevRound()
            elif act[a] == "}":
                COP357.nextRound()
            elif act[a] == "@":
                print("Exiting Program...")
            elif act[a] == " ":
                print("You wait...")
            else:
                print("NOT A VALID COMMAND")
            COP357.incrementSec(1)
