from Gun_BreakOpen import Gun_BreakOpen
from Ammunition import gauge12_2and3quarters

#brandname and bullet and type, amount, sound, grain, velocity (fps), overall length (in mm), projectile count, malfunction chance
ammo = gauge12_2and3quarters

StoegerDD = Gun_BreakOpen([["", False, 0, 0], ["", False, 0, 0]], [0, 0, 0], 0, 0, ammo, 2, 0, False, False, 1, 3)


def switchBarrel():
    if StoegerDD.getCurrentBarrel() == 1:
        StoegerDD.changeCurrentBarrel(0)

def main():
    StoegerDD.changeCurrentBarrel(2)
    if StoegerDD.isBarrelBlocked(0) or StoegerDD.isBarrelBlocked(1):
        StoegerDD.clearBarrels()
    act = ""
    while act != "@":
        print("-" * 50)
        print("The Stoeger Double Defense shotgun is a side by side double barrel made in Brazil under the comapny,\n"
              "E.R. Amantino (aka Boito), and is imported into the US under the Stoeger brand, which is an owned\n"
              "subsidary of Benelli. It has picatinny rails mounted to the top and end of the barrel for\n"
              "mounting sights and flashlights/lasers respectively. To operate the shotgun, push the lever to the\n"
              "left or right to open up the barrel, and insert live cartridges after removing any cartridges inside\n"
              "the barrel. The gun will not eject spent or live cartridges. Pulling the trigger fires the right\n"
              "barrel first then left. The safety will prevent the hammer from striking the firing pin. Inserting\n"
              "and removing rounds will follow the barrel firing order. The gun is chambered\n"
              "for 12 Gauge 3 inch shells. 3.5 inch Magnum shells will NOT fit into the chambers.\n"
              "An automatic safety will engage everytime the action is opened.")
        print("-" * 50)
        print("Charles Daly Triple Threat Shotgun | 12 Gauge")
        print("| = hold trigger/release trigger")
        print("/ = yank trigger")
        print("t/T = open barrels, partial/fully")
        print("b = close barrels")
        print("y/Y = insert round, remove round")
        print("v = toggle safety")
        print("{,} = next/previous ammo type")
        print("[,] = change barrel to load/unload")
        print("@ = exit program")
        StoegerDD.currentAmmo()
        print("-" * 50)
        print("hold trigger: " + str(StoegerDD.showTToggle()))
        if StoegerDD.getBarrelLock() >= 2:
            StoegerDD.showBarrel()
            if StoegerDD.getCurrentBarrel() == 0:
                print("Remove/insert round in left barrel")
            elif StoegerDD.getCurrentBarrel() == 1:
                print("Remove/insert round in right barrel")
        act = input("CMD: ")
        for a in range(len(act)):
            if act[a] == "[":
                if StoegerDD.getBarrelLock() == 3:
                    if StoegerDD.getCurrentBarrel() == 0:
                        StoegerDD.changeCurrentBarrel(1)
                    else:
                        StoegerDD.changeCurrentBarrel(StoegerDD.getCurrentBarrel()-1)
            if act[a] == "]":
                if StoegerDD.getBarrelLock() == 3:
                    if StoegerDD.getCurrentBarrel() == 1:
                        StoegerDD.changeCurrentBarrel(0)
                    else:
                        StoegerDD.changeCurrentBarrel(StoegerDD.getCurrentBarrel()+1)
            if act[a] == "v":
                if StoegerDD.getFiremode() == 0:
                    StoegerDD.changeFiremode(1)
                    print("You push the sliding button on the tang so that the letter S is revealed.")
                else:
                    StoegerDD.changeFiremode(0)
                    print("You push the sliding button on the tang so that the letter S is covered.")
            elif act[a] == "|":
                StoegerDD.toggleTrigger()
                if StoegerDD.showTToggle():
                    if StoegerDD.getFiremode() == 0:
                        StoegerDD.fireBarrel(StoegerDD.getCurrentBarrel())
                        switchBarrel()
                    else:
                        print("PLAP")
            elif act[a] == "t":
                if StoegerDD.getBarrelLock() == 0:
                    StoegerDD.changeBarrelLock(2)
                    print("You push the top lever to the right, and break open the barrels slightly.")
                    print("The gun is partially open.")
            elif act[a] == "T":
                if StoegerDD.getBarrelLock() < 3:
                    print("You push the top lever to the right, and break open the barrels fully.")
                    print("The gun is fully open.")
                    StoegerDD.changeBarrelLock(3)
                    StoegerDD.changeCurrentBarrel(1)
                    if StoegerDD.getFiremode() == 0:
                        print("The automatic safety is engaged, and the S underneath the safety is revealed.")
                    StoegerDD.changeFiremode(1)
                else:
                    print("The gun is already fully open.")
            elif act[a] == "b":
                if StoegerDD.getBarrelLock() != 0:
                    StoegerDD.changeBarrelLock(0)
                    print("You close up the barrels, and thus close the action of the gun.")
                    StoegerDD.changeCurrentBarrel(1)
                else:
                    print("The action is already closed.")
            elif act[a] == "/":
                if not StoegerDD.showTToggle():
                    if StoegerDD.getFiremode() == 0:
                        StoegerDD.fireBarrel(StoegerDD.getCurrentBarrel())
                        switchBarrel()
                    else:
                        print("You pull the trigger.")
                        print("PLAP")
                        print("After you pulled the trigger, you let go of it.")
            elif act[a] == "y":
                StoegerDD.addRound(StoegerDD.getCurrentBarrel())
            elif act[a] == "Y":
                StoegerDD.removeRound(StoegerDD.getCurrentBarrel(), 1)
            elif act[a] == "{":
                StoegerDD.prevRound()
            elif act[a] == "}":
                StoegerDD.nextRound()
            elif act[a] == "@":
                print("Exiting Program...")
            elif act[a] == " ":
                print("You wait...")
            else:
                print("NOT A VALID COMMAND")
            StoegerDD.incrementSec(1)
