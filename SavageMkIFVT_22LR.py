# Savage Mark 1 FVT Rifle .22 Long Rifle

from Gun_BreakOpen import Gun_BreakOpen

#brandname and bullet and type, amount, sound, grain, velocity (fps), overall length (in mm), projectile count
ammo = [["CCI Mini Mag|.22 LR|Round Nose", 100, "KRAAAAAAAK", 40, 1235, 25.4, 1]]

SavageMK1 = Gun_BreakOpen([""], [0], 0, 0, ammo, 0, 1, False, False, 0)

def main():
    act = ""
    while act != "@":
        print("-" * 50)
        print("The Savage Mark 1 rifle is a bolt action rifle chambered in .22 Long Rifle\n"
              "It is single shot only, and contains peep sights, which makes it usefull\n"
              "for target shooting, plinking, hunting, and other activities where precision\n"
              "is usefull. It is very popular in Boy Scout shooting ranges for this reason.")
        print("-" * 50)
        print("Savage Mark 1 FVT Rifle | .22 Long Rifle")
        print("| = hold trigger/release trigger")
        print("/ = yank trigger")
        print("g = rotate open bolt/close bolt")
        print("t/T = open bolt, partial/fully")
        print("b = push back bolt")
        print("y = insert round")
        print("h = remove round")
        print("v = toggle safety")
        print("{,} = next/previous ammo type")
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
                    SavageMK1.changeHammer(0, 2)
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
            elif act[a] == "t":
                if SavageMK1.getBarrelLock() == 1:
                    SavageMK1.changeBarrelLock(2)
                    print("You pull back the bolt partially.")
            elif act[a] == "T":
                if SavageMK1.getBarrelLock() >= 1:
                    SavageMK1.changeBarrelLock(3)
                    print("You pull back the bolt fully.")
            elif act[a] == "y":
                SavageMK1.addRound(0)
            elif act[a] == "h":
                SavageMK1.removeRound(0, 1)
            elif act[a] == "/":
                if SavageMK1.getFiremode() == 0:
                    SavageMK1.fireBarrel(0)
            elif act[a] == "|":
                SavageMK1.toggleTrigger()
                if SavageMK1.showTToggle() and SavageMK1.getFiremode() == 0:
                    SavageMK1.fireBarrel(0)
            elif act[a] == "@":
                print("Exiting Program...")
            else:
                print("NOT A VALID COMMAND")