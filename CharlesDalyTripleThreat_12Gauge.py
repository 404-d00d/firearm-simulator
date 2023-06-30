from Gun_BreakOpen import Gun_BreakOpen
from Ammunition import gauge12_2and3quarters

#brandname and bullet and type, amount, sound, grain, velocity (fps), overall length (in mm), projectile count, malfunction chance
ammo = gauge12_2and3quarters

CharlesDalyTT = Gun_BreakOpen([["", False, 0, 0], ["", False, 0, 0], ["", False, 0, 0]], [0, 0, 0], 0, 0, ammo, 2, 0, False, False, 1, 3)


def switchBarrel():
    if CharlesDalyTT.getCurrentBarrel() == 2:
        CharlesDalyTT.changeCurrentBarrel(0)
    elif CharlesDalyTT.getCurrentBarrel() == 0:
        CharlesDalyTT.changeCurrentBarrel(1)


def main():
    CharlesDalyTT.changeCurrentBarrel(2)
    if CharlesDalyTT.isBarrelBlocked(0) or CharlesDalyTT.isBarrelBlocked(1) or CharlesDalyTT.isBarrelBlocked(2):
        CharlesDalyTT.clearBarrels()
    act = ""
    while act != "@":
        print("-" * 50)
        print("The Charles Daly Triple Threat Shotgun is a triple barreled shotgun made in Turkey as the \n"
              "Akkar Mammut 312 HD Black, and is imported into the US under the Charles Daly sub-brand of Chiappa.\n"
              "It has picatinny rails mounted to the top and end of the barrel for\n"
              "mounting sights and flashlights/lasers respectively. To operate the shotgun, push the lever to the\n"
              "left or right to open up the barrel, and insert live cartridges after removing any cartridges inside\n"
              "the barrel. The gun will not eject spent or live cartridges. Pulling the trigger fires the right\n"
              "barrel first then left, and finally the top barrel. The safety will prevent the hammer from striking\n"
              "the firing pin. Inserting and removing rounds will follow the barrel firing order. The gun is\n"
              "chambered for 12 Gauge 3 inch shells. 3.5 inch Magnum shells will NOT fit into the chambers.")
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
        CharlesDalyTT.currentAmmo()
        print("-" * 50)
        print("hold trigger: " + str(CharlesDalyTT.showTToggle()))
        if CharlesDalyTT.getBarrelLock() >= 2:
            CharlesDalyTT.showBarrel()
            if CharlesDalyTT.getCurrentBarrel() == 0:
                print("Remove/insert round in left barrel")
            elif CharlesDalyTT.getCurrentBarrel() == 1:
                print("Remove/insert round in top barrel")
            else:
                print("Remove/insert round in right barrel")
        act = input("CMD: ")
        for a in range(len(act)):
            if act[a] == "[":
                if CharlesDalyTT.getBarrelLock() == 3:
                    if CharlesDalyTT.getCurrentBarrel() == 0:
                        CharlesDalyTT.changeCurrentBarrel(2)
                    else:
                        CharlesDalyTT.changeCurrentBarrel(CharlesDalyTT.getCurrentBarrel()-1)
            if act[a] == "]":
                if CharlesDalyTT.getBarrelLock() == 3:
                    if CharlesDalyTT.getCurrentBarrel() == 2:
                        CharlesDalyTT.changeCurrentBarrel(0)
                    else:
                        CharlesDalyTT.changeCurrentBarrel(CharlesDalyTT.getCurrentBarrel()+1)
            if act[a] == "v":
                if CharlesDalyTT.getFiremode() == 0:
                    CharlesDalyTT.changeFiremode(1)
                    print("You push the sliding button on the tang so that the red dot is covered and the letter S is revealed.")
                else:
                    CharlesDalyTT.changeFiremode(0)
                    print("You push the sliding button on the tang so that the letter S is covered and a red dot is shown.")
            elif act[a] == "|":
                CharlesDalyTT.toggleTrigger()
                if CharlesDalyTT.showTToggle():
                    if CharlesDalyTT.getFiremode() == 0:
                        CharlesDalyTT.fireBarrel(CharlesDalyTT.getCurrentBarrel())
                        switchBarrel()
                    else:
                        print("PLAP")
            elif act[a] == "t":
                if CharlesDalyTT.getBarrelLock() == 0:
                    CharlesDalyTT.changeBarrelLock(2)
                    print("You push the top lever to the right, and break open the barrels slightly.")
                    print("The gun is partially open.")
            elif act[a] == "T":
                if CharlesDalyTT.getBarrelLock() < 3:
                    print("You push the top lever to the right, and break open the barrels fully.")
                    print("The gun is fully open.")
                    CharlesDalyTT.changeBarrelLock(3)
                    CharlesDalyTT.changeCurrentBarrel(2)
                else:
                    print("The gun is already fully open.")
            elif act[a] == "b":
                if CharlesDalyTT.getBarrelLock() != 0:
                    CharlesDalyTT.changeBarrelLock(0)
                    print("You close up the barrels, and thus close the action of the gun.")
                    CharlesDalyTT.changeCurrentBarrel(2)
                else:
                    print("The action is already closed.")
            elif act[a] == "/":
                if not CharlesDalyTT.showTToggle():
                    if CharlesDalyTT.getFiremode() == 0:
                        CharlesDalyTT.fireBarrel(CharlesDalyTT.getCurrentBarrel())
                        switchBarrel()
                    else:
                        print("You pull the trigger.")
                        print("PLAP")
                        print("After you pulled the trigger, you let go of it.")
            elif act[a] == "y":
                CharlesDalyTT.addRound(CharlesDalyTT.getCurrentBarrel())
            elif act[a] == "Y":
                CharlesDalyTT.removeRound(CharlesDalyTT.getCurrentBarrel(), 1)
            elif act[a] == "{":
                CharlesDalyTT.prevRound()
            elif act[a] == "}":
                CharlesDalyTT.nextRound()
            elif act[a] == "@":
                print("Exiting Program...")
            elif act[a] == " ":
                print("You wait...")
            else:
                print("NOT A VALID COMMAND")
            CharlesDalyTT.incrementSec(1)
