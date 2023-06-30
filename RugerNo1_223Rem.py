# Ruger No 1 Rifle .223 Remington

from Gun_BreakOpen import Gun_BreakOpen
from Ammunition import remington223

#brandname and bullet and type, amount, sound, grain, velocity (fps), overall length (in mm), projectile count, malfunction chance
ammo = remington223

RugerNo1 = Gun_BreakOpen([["", False, 0, 0]], [0], 0, 0, ammo, 0, 0, False, False, 0, 3)


def main():
    if RugerNo1.isBarrelBlocked(0):
        RugerNo1.clearBarrels()
    act = ""
    while act != "@":
        print("-" * 50)
        print("The Ruger No 1 is a single shot rifle chambered in large rifle calibers. It is\n"
              "one of Ruger's most successful products, having been made since the 1960s.\n"
              "It is a falling block rifle, and to load it you must push down the lever to open\n"
              "up the chamber, where you can then load a cartridge into the breech. Close up the lever\n"
              "and you are ready to fire. A tang safety blocks the trigger if activated.")
        print("-" * 50)
        print("Ruger No 1 Rifle | .223 Remington")
        print("| = hold trigger/release trigger")
        print("/ = yank trigger")
        print("t/T = open lever, partial/fully")
        print("b = close lever")
        print("y/Y = insert round, remove round")
        print("v = toggle safety")
        print("{,} = next/previous ammo type")
        print("@ = exit program")
        RugerNo1.currentAmmo()
        print("-" * 50)
        print("hold trigger: " + str(RugerNo1.showTToggle()))
        if RugerNo1.getBarrelLock() >= 2:
            RugerNo1.showBarrel()
        act = input("CMD: ")
        for a in range(len(act)):
            if act[a] == "v":
                if RugerNo1.getFiremode() == 0:
                    RugerNo1.changeFiremode(1)
                    print("You push the sliding button on the tang so that the word SAFE is revealed.")
                else:
                    RugerNo1.changeFiremode(0)
                    print("You push the sliding button on the tang so that the word SAFE is covered up.")
            elif act[a] == "|":
                RugerNo1.toggleTrigger()
                if RugerNo1.showTToggle() and RugerNo1.getFiremode() == 0:
                    RugerNo1.fireBarrel(0)
            elif act[a] == "t":
                if RugerNo1.getBarrelLock() == 0:
                    RugerNo1.changeBarrelLock(2)
                    print("You depress the inside button on the lever, and partially push it down, opening the action.")
                    print("The gun is partially open.")
            elif act[a] == "T":
                if RugerNo1.getBarrelLock() < 3:
                    print("You depress the inside button on the lever, and push it down fully, opening the action.")
                    print("The gun is fully open.")
                    RugerNo1.changeBarrelLock(3)
                else:
                    print("The gun is already fully open.")
            elif act[a] == "b":
                if RugerNo1.getBarrelLock() != 0:
                    RugerNo1.changeBarrelLock(0)
                    print("You close up the lever, and thus close the action of the gun.")
                    if RugerNo1.showTToggle():
                        RugerNo1.changeHammer(0, 0)
                else:
                    print("The action is already closed.")
            elif act[a] == "/":
                if RugerNo1.getFiremode() == 0 and not RugerNo1.showTToggle():
                    RugerNo1.fireBarrel(0)
            elif act[a] == "y":
                RugerNo1.addRound(0)
            elif act[a] == "Y":
                RugerNo1.removeRound(0, 1)
            elif act[a] == "{":
                RugerNo1.prevRound()
            elif act[a] == "}":
                RugerNo1.nextRound()
            elif act[a] == "@":
                print("Exiting Program...")
            elif act[a] == " ":
                print("You wait...")
            else:
                print("NOT A VALID COMMAND")
            RugerNo1.incrementSec(1)
