# Henry HO15B-12 Single Shot Shotgun 12 Gauge

from Gun_BreakOpen import Gun_BreakOpen

#brandname and bullet and type, amount, sound, grain, velocity (fps), overall length (in mm), projectile count
ammo = [["Winchester Super-X|12 Gauge|Buckshot", 10, "KATHOOOOOOOM", 53.8, 1325, 69.85, 9]]

HenrySSShotgun = Gun_BreakOpen([""], [0], 0, 0, ammo, 0, 1, False, False, 0)

def main():
    act = ""
    while act != "@":
        print("-" * 50)
        print("The Henry HO15 single shot series of firearms have been a successful product line from Henry Repeating Arms, \n"
              "who are best known for making lever action repeating rifles. This is a shotgun with a brass frame, \n"
              "and straight stock, and is chambered in 3 1/2 inch shells. Operation is very simple: \n"
              "Push the lever left or right to open up the gun, then shove a shell into the barrel. \n"
              "Cock the hammer and when you're ready to fire, pull the trigger.\n"
              "A specialized hammer system prevents the barrel from opening or closing if the hammer is cocked.")
        print("-" * 50)
        print("Henry HO15 Single Shot Shotgun | 12 Gauge 3 1/2 inch")
        print("| = hold trigger/release trigger")
        print("/ = yank trigger")
        print("g/G = pull hammer/release hammer, yank back hammer")
        print("t/T = open barrel, partial/fully")
        print("b = close barrel")
        print("y = insert round")
        print("h = remove round")
        print("{,} = next/previous ammo type")
        print("Current ammo type: "+ammo[HenrySSShotgun.getCurrentRound()][0]+"| "+str(ammo[HenrySSShotgun.getCurrentRound()][1])+" rounds")
        print("-"*50)
        print("hold hammer: "+str(HenrySSShotgun.showHToggle()))
        print("hold trigger: "+str(HenrySSShotgun.showTToggle()))
        if HenrySSShotgun.getBarrelLock() >= 1:
            HenrySSShotgun.showBarrel()
        act = input("CMD: ")
        for a in range(len(act)):
            if act[a] == "t":
                if HenrySSShotgun.getBarrelLock() < 1 and HenrySSShotgun.getHammer(0) == 0:
                    HenrySSShotgun.changeBarrelLock(1)
                    print("You move the lever, and open the action.")
                    print("The gun is partially open.")
            elif act[a] == "|":
                HenrySSShotgun.toggleTrigger()
                if HenrySSShotgun.showTToggle():
                    HenrySSShotgun.fireBarrel(0)
            elif act[a] == "T":
                if HenrySSShotgun.getBarrelLock() < 3 and HenrySSShotgun.getHammer(0) == 0:
                    HenrySSShotgun.changeBarrelLock(3)
                    print("You move the lever, and open the action.")
                    print("The gun is fully open.")
            elif act[a] == "G":
                if HenrySSShotgun.getHammer(0) == 0:
                    HenrySSShotgun.changeHammer(0, 2)
                    print("You pull back the hammer, letting go once it is fully cocked.")
                    if HenrySSShotgun.showTToggle():
                        print("The hammer immediately slams into the chamber.")
                        HenrySSShotgun.fireBarrel(0)
            elif act[a] == "g":
                HenrySSShotgun.toggleHammer()
                if HenrySSShotgun.showHToggle():
                    HenrySSShotgun.changeHammer(0, 2)
                    print("You pull back the hammer, and you keep your thumb on it.")
                else:
                    print("You remove your thumb from the hammer.")
                if HenrySSShotgun.showTToggle() and not HenrySSShotgun.showHToggle():
                    HenrySSShotgun.changeHammer(0, 0)
                    print("You ease the hammer into its resting position.")
                    print("The gun is now not cocked.")
            elif act[a] == "b":
                if HenrySSShotgun.getHammer(0) == 0:
                    HenrySSShotgun.changeBarrelLock(0)
                    print("You close up the barrel of the gun.")
            elif act[a] == "y":
                HenrySSShotgun.addRound(0)
            elif act[a] == "h":
                HenrySSShotgun.removeRound(0, 1)
            elif act[a] == "/":
                if not HenrySSShotgun.showHToggle():
                    HenrySSShotgun.fireBarrel(0)
            elif act[a] == "{":
                HenrySSShotgun.prevRound()
            elif act[a] == "}":
                HenrySSShotgun.nextRound()
            elif act[a] == "@":
                print("Exiting Program...")
            else:
                print("NOT A VALID COMMAND")
