# Savage Mark 1 FVT Rifle .22 Long Rifle

from Gun_BreakOpen import Gun_BreakOpen
from Ammunition import lr22

#brandname and bullet and type, amount, sound, grain, velocity (fps), overall length (in mm), projectile count, malfunction chance
ammo = lr22

SavageMK1 = Gun_BreakOpen([["", False, 0, 0]], [0], 0, 0, ammo, 0, 0, False, False, 1, 1)


def main():
    if SavageMK1.isBarrelBlocked(0):
        SavageMK1.clearBarrels()
    act = ""
    while act != "@":
        print("-" * 50)
        print("The Savage Mark 1 rifle is a bolt action rifle chambered in .22 Long Rifle. It is single shot only, \n"
              "and contains peep sights, which makes it useful for target shooting, plinking, hunting, and other \n"
              "activities where precision is usefull. It is very popular in Boy Scout shooting ranges for this \n"
              "reason. To operate it, rotate the bolt handle up and pull back to load a round into the chamber.\n"
              "To close the bolt perform the reverse motions and when you are ready to fire, pull the trigger.\n"
              "A safety will prevent you from pulling the trigger if activated, but you are still able to move the bolt.")
        print("-" * 50)
        print("Savage Mark 1 FVT Rifle | .22 Long Rifle")
        print("| = hold trigger/release trigger")
        print("/ = yank trigger")
        print("g = rotate open bolt/close bolt")
        print("t/T = open bolt, partial/fully")
        print("b = push back bolt")
        print("y/Y = insert round, remove round")
        print("v = toggle safety")
        print("{,} = next/previous ammo type")
        print("@ = exit program")
        SavageMK1.currentAmmo()
        print("-" * 50)
        print("hold trigger: " + str(SavageMK1.showTToggle()))
        if SavageMK1.getBarrelLock() >= 2:
            SavageMK1.showBarrel()
        act = input("CMD: ")
        for a in range(len(act)):
            if act[a] == "g":
                if SavageMK1.getBarrelLock() == 0:
                    SavageMK1.changeBarrelLock(1)
                    print("You lift up the bolt handle until it is upright.\n"
                          "The gun is now cocked.")
                elif SavageMK1.getBarrelLock() == 1:
                    SavageMK1.changeBarrelLock(0)
                    print("You close the bolt handle of the gun.")
                    if SavageMK1.showTToggle():
                        SavageMK1.changeHammer(0, 0)
            elif act[a] == "v":
                if SavageMK1.getFiremode() == 0:
                    SavageMK1.changeFiremode(1)
                    print("You push the right side lever until the red dot is covered.")
                else:
                    SavageMK1.changeFiremode(0)
                    print("You push the right side lever so that the red dot is revealed.")
            elif act[a] == "b":
                if SavageMK1.getBarrelLock() >= 2:
                    SavageMK1.changeBarrelLock(1)
                    print("You push the bolt until the chamber is closed")
                else:
                    print("The bolt is already closed.")
            elif act[a] == "t":
                if not SavageMK1.showTToggle():
                    if SavageMK1.getBarrelLock() == 1:
                        SavageMK1.changeBarrelLock(2)
                        print("You pull back the bolt partially.")
                else:
                    print("You pull back the bolt, only to realize that you'll just remove the bolt from the gun.")
                    print("Bad idea.")
            elif act[a] == "T":
                if not SavageMK1.showTToggle():
                    if SavageMK1.getBarrelLock() >= 1 and SavageMK1.getBarrelLock() != 3:
                        print("You pull back the bolt fully.")
                        SavageMK1.changeBarrelLock(3)
                    else:
                        print("The gun is already fully open.")
                else:
                    print("You pull back the bolt, only to realize that you'll just remove the bolt from the gun.")
                    print("Bad idea.")
            elif act[a] == "y":
                SavageMK1.addRound(0)
            elif act[a] == "Y":
                SavageMK1.removeRound(0, 1)
            elif act[a] == "/":
                if SavageMK1.getFiremode() == 0 and not SavageMK1.showTToggle():
                    SavageMK1.fireBarrel(0)
            elif act[a] == "|":
                SavageMK1.toggleTrigger()
                if SavageMK1.showTToggle() and SavageMK1.getFiremode() == 0:
                    SavageMK1.fireBarrel(0)
            elif act[a] == "@":
                print("Exiting Program...")
            elif act[a] == " ":
                print("You wait...")
            else:
                print("NOT A VALID COMMAND")
            SavageMK1.incrementSec(1)
