from Gun_BreakOpen import Gun_BreakOpen
from Ammunition import gauge12_2and3quarters

#brandname and bullet and type, amount, sound, grain, velocity (fps), overall length (in mm), projectile count, malfunction chance
ammo = gauge12_2and3quarters

BrowningCynergyCX = Gun_BreakOpen([["", False, 0, 0], ["", False, 0, 0]], [0, 0], 0, 0, ammo, 1, 0, False, False, 1, 3)


def switchBarrel():
    if BrowningCynergyCX.getCurrentBarrel() == 1:
        BrowningCynergyCX.changeCurrentBarrel(0)
    else:
        BrowningCynergyCX.changeCurrentBarrel(1)

def main():
    if BrowningCynergyCX.isBarrelBlocked(0) or BrowningCynergyCX.isBarrelBlocked(1):
        BrowningCynergyCX.clearBarrels()
    act = ""
    while act != "@":
        print("-" * 50)
        print("The Browning Cynergy CX Composite is a shotgun chambered in 12 Gauge shells up to 3 inches long. It is\n"
              "a double barrel firearm with the barrels arranged in an Over-Under configuration and has composite\n"
              "furniture instead of wood. This type of configuration provides a unified sight plane for aiming, and\n"
              "is commonly used for trap shooting, as well as certain hunting configurarions. To load the gun, break \n"
              "open the barrel, and insert cartridges into the gun. Close the action up and you are ready to fire. An\n"
              "automatic ejector will kick out spent shells while leaving live shells in the gun. The safety is non\n"
              "automatic, and will only block the trigger when activated. The safety doubles as a barrel selector,\n"
              "and moving it to the left or right will choose whether the bottom or top barrel will be fire first\n"
              "respectively.")
        print("-" * 50)
        print("Browning Cynergy CX Composite Shotgun | 12 Gauge")
        print("| = hold trigger/release trigger")
        print("/ = yank trigger")
        print("t/T = open barrels, partial/fully")
        print("b = close barrels")
        print("y/Y = insert round, remove round")
        print("v/V = toggle safety, switch barrel selector")
        print("{,} = next/previous ammo type")
        print("[,] = change barrel to load/unload")
        print("@ = exit program")
        BrowningCynergyCX.currentAmmo()
        print("-" * 50)
        print("hold trigger: " + str(BrowningCynergyCX.showTToggle()))
        if BrowningCynergyCX.getBarrelLock() >= 2:
            BrowningCynergyCX.showBarrel()
            if BrowningCynergyCX.getCurrentBarrel() == 0:
                print("Remove/insert round in top barrel")
            elif BrowningCynergyCX.getCurrentBarrel() == 1:
                print("Remove/insert round in bottom barrel")
        act = input("CMD: ")
        for a in range(len(act)):
            if act[a] == "[":
                if BrowningCynergyCX.getBarrelLock() == 3:
                    switchBarrel()
            if act[a] == "]":
                if BrowningCynergyCX.getBarrelLock() == 3:
                    switchBarrel()
            # 0=Top first ready, 1=Bottom first ready, 2=Top first safe, 3=Bottom first safe
            if act[a] == "v":
                if BrowningCynergyCX.getFiremode() == 0:
                    BrowningCynergyCX.changeFiremode(BrowningCynergyCX.getFiremode()+2)
                    print("You push the sliding button on the tang so that the letter S is revealed.")
                else:
                    BrowningCynergyCX.changeFiremode(BrowningCynergyCX.getFiremode()-2)
                    print("You push the sliding button on the tang so that the letter S is covered.")
            if act[a] == "V":
                if BrowningCynergyCX.getCurrentBarrel() == 0:
                    print("You push the sliding button on the tang so that the letter U is revealed and the letter O is covered.")
                    BrowningCynergyCX.changeCurrentBarrel(1)
                    if BrowningCynergyCX.getFiremode() == 0:
                        BrowningCynergyCX.changeFiremode(1)
                    elif BrowningCynergyCX.getFiremode() == 2:
                        BrowningCynergyCX.changeFiremode(3)
                else:
                    print("You push the sliding button on the tang so that the letter O is revealed and the letter U is covered.")
                    BrowningCynergyCX.changeCurrentBarrel(0)
                    if BrowningCynergyCX.getFiremode() == 1:
                        BrowningCynergyCX.changeFiremode(0)
                    elif BrowningCynergyCX.getFiremode() == 3:
                        BrowningCynergyCX.changeFiremode(2)
            elif act[a] == "|":
                BrowningCynergyCX.toggleTrigger()
                if BrowningCynergyCX.showTToggle():
                    if BrowningCynergyCX.getFiremode() <= 1:
                        BrowningCynergyCX.fireBarrel(BrowningCynergyCX.getCurrentBarrel())
                        switchBarrel()
                    else:
                        print("PLAP")
            elif act[a] == "t":
                if BrowningCynergyCX.getBarrelLock() == 0:
                    BrowningCynergyCX.changeBarrelLock(2)
                    print("You push the top lever to the right, and break open the barrels slightly.")
                    print("The gun is partially open.")
            elif act[a] == "T":
                if BrowningCynergyCX.getBarrelLock() < 3:
                    print("You push the top lever to the right, and break open the barrels fully.")
                    print("The gun is fully open.")
                    BrowningCynergyCX.changeBarrelLock(3)
                else:
                    print("The gun is already fully open.")
            elif act[a] == "b":
                if BrowningCynergyCX.getBarrelLock() != 0:
                    BrowningCynergyCX.changeBarrelLock(0)
                    print("You close up the barrels, and thus close the action of the gun.")
                    if BrowningCynergyCX.getFiremode() == 0 or BrowningCynergyCX.getFiremode() == 2:
                        BrowningCynergyCX.changeCurrentBarrel(0)
                    elif BrowningCynergyCX.getFiremode() == 1 or BrowningCynergyCX.getFiremode() == 3:
                        BrowningCynergyCX.changeCurrentBarrel(1)
                else:
                    print("The action is already closed.")
            elif act[a] == "/":
                if not BrowningCynergyCX.showTToggle():
                    if BrowningCynergyCX.getFiremode() <= 1:
                        BrowningCynergyCX.fireBarrel(BrowningCynergyCX.getCurrentBarrel())
                        switchBarrel()
                    else:
                        print("You pull the trigger.")
                        print("PLAP")
                        print("After you pulled the trigger, you let go of it.")
            elif act[a] == "y":
                BrowningCynergyCX.addRound(BrowningCynergyCX.getCurrentBarrel())
            elif act[a] == "Y":
                BrowningCynergyCX.removeRound(BrowningCynergyCX.getCurrentBarrel(), 1)
            elif act[a] == "{":
                BrowningCynergyCX.prevRound()
            elif act[a] == "}":
                BrowningCynergyCX.nextRound()
            elif act[a] == "@":
                print("Exiting Program...")
            elif act[a] == " ":
                print("You wait...")
            else:
                print("NOT A VALID COMMAND")
            BrowningCynergyCX.incrementSec(1)
