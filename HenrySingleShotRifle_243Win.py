# Henry HO15-243 Single Shot Rifle 243 Winchester

from Gun_BreakOpen import Gun_BreakOpen

#brandname and bullet and type, amount, sound, grain, velocity (fps), overall length (in mm), projectile count
ammo = [["Prvi Partizan|.243 Winchester|Soft Point", 20, "KATHRAAAOOOOOOOOOOM", 90, 3100, 68.83, 1]]

HenrySSRifle = Gun_BreakOpen([""], [0], 0, 0, ammo, 2, 1, False, False, 0, 0)

def main():
    act = ""
    while act != "@":
        print("-" * 50)
        print("The Henry HO15 single shot series of firearms have been a successful product line from Henry Repeating Arms, \n"
              "who are best known for making lever action repeating rifles. This is a rifle with a semi-pistol grip stock, \n"
              "and is chambered in .243 Winchester. Operation is very simple: \n"
              "Push the lever left or right to open up the gun, then shove a cartridge into the barrel. \n"
              "Cock the hammer and when you're ready to fire, pull the trigger.\n"
              "A specialized hammer system prevents the barrel from opening or closing if the hammer is cocked.")
        print("-" * 50)
        print("Henry HO15 Single Shot Rifle | .243 Winchester")
        print("| = hold trigger/release trigger")
        print("/ = yank trigger")
        print("g/G = pull hammer/release hammer, yank back hammer")
        print("t/T = open barrel, partial/fully")
        print("b = close barrel")
        print("y = insert round")
        print("h = remove round")
        print("{,} = next/previous ammo type")
        HenrySSRifle.currentAmmo()
        print("-"*50)
        print("hold hammer: "+str(HenrySSRifle.showHToggle()))
        print("hold trigger: "+str(HenrySSRifle.showTToggle()))
        if HenrySSRifle.getBarrelLock() >= 1:
            HenrySSRifle.showBarrel()
        act = input("CMD: ")
        for a in range(len(act)):
            if act[a] == "t":
                if HenrySSRifle.getBarrelLock() < 1 and HenrySSRifle.getHammer(0) == 0:
                    HenrySSRifle.changeBarrelLock(1)
                    print("You move the lever, and open the action.")
                    print("The gun is partially open.")
            elif act[a] == "|":
                HenrySSRifle.toggleTrigger()
                if HenrySSRifle.showTToggle():
                    HenrySSRifle.fireBarrel(0)
            elif act[a] == "T":
                if HenrySSRifle.getBarrelLock() < 3 and HenrySSRifle.getHammer(0) == 0:
                    print("You move the lever, and open the action.")
                    print("The gun is fully open.")
                    HenrySSRifle.changeBarrelLock(3)
                else:
                    print("The gun is already fully open.")
            elif act[a] == "G":
                if HenrySSRifle.getHammer(0) == 0:
                    HenrySSRifle.changeHammer(0, 2)
                    print("You pull back the hammer, letting go once it is fully cocked.")
                    if HenrySSRifle.showTToggle():
                        print("The hammer immediately slams into the chamber.")
                        HenrySSRifle.fireBarrel(0)
            elif act[a] == "g":
                HenrySSRifle.toggleHammer()
                if HenrySSRifle.showHToggle():
                    if HenrySSRifle.getHammer(0) == 0:
                        HenrySSRifle.changeHammer(0, 2)
                        print("You pull back the hammer, and you keep your thumb on it.")
                    else:
                        print("You put your thumb on the hammer.")
                else:
                    print("You remove your thumb from the hammer.")
                if HenrySSRifle.showTToggle() and not HenrySSRifle.showHToggle():
                    HenrySSRifle.changeHammer(0, 0)
                    print("You ease the hammer into its resting position.")
                    print("The gun is now not cocked.")
            elif act[a] == "b":
                if HenrySSRifle.getHammer(0) == 0:
                    HenrySSRifle.changeBarrelLock(0)
                    print("You close up the barrel of the gun.")
                else:
                    print("The action is already closed.")
            elif act[a] == "y":
                HenrySSRifle.addRound(0)
            elif act[a] == "h":
                HenrySSRifle.removeRound(0, 1)
            elif act[a] == "/":
                if not HenrySSRifle.showHToggle() and not HenrySSRifle.showTToggle():
                    HenrySSRifle.fireBarrel(0)
            elif act[a] == "{":
                HenrySSRifle.prevRound()
            elif act[a] == "}":
                HenrySSRifle.nextRound()
            elif act[a] == "@":
                print("Exiting Program...")
            else:
                print("NOT A VALID COMMAND")
