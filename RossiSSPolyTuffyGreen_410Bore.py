# Rossi SS Poly Tuffy Green Shotgun .410 Bore

from Gun_BreakOpen import Gun_BreakOpen

#brandname and bullet and type, amount, sound, grain, velocity (fps), overall length (in mm), projectile count, malfunction chance
ammo = [["Fiocchi Target|.410 Bore|#8 Birdshot", 25, "KATHRAAAAK", 1.07, 1250, 63.5, 204, 0.001]]

RossiSSPTGreen = Gun_BreakOpen([["", False, 0, 0]], [0], 0, 0, ammo, 0, 1, False, False, 0, 0)

def main():
    if RossiSSPTGreen.isBarrelBlocked(0):
        RossiSSPTGreen.clearBarrels()
    act = ""
    while act != "@":
        print("-" * 50)
        print("The Rossi SS Poly Tuffy Shotgun is a .410 bore single shot break action shotgun made by Rossi, \n"
              "who are best known for making lever action repeating rifles and some revolvers. This is a shotgun \n"
              "with plastic green furniture and is chambered in 3 inch shells. Operation is very simple: \n"
              "Push the the button on the top right of the frame to open up the gun, then shove a shell into the \n"
              "barrel. Cock the hammer and when you're ready to fire, pull the trigger. There is a safety that \n"
              "prevents the hammer from striking the firing pi, although opening the action, pulling the trigger \n"
              "and cocking the hammer is unimpeded. Half cocking the hammer is possible with this gun.")
        print("-" * 50)
        print("Rossi SS Poly Tuffy Green Shotgun | .410 Bore 3 inch")
        print("| = hold trigger/release trigger")
        print("/ = yank trigger")
        print("g/G = pull hammer/release hammer, yank back hammer")
        print("t/T = open barrel, partial/fully")
        print("b/B = close barrel, half cock hammer")
        print("y = insert round")
        print("h = remove round")
        print("v = toggle safety")
        print("{,} = next/previous ammo type")
        print("@ = exit program")
        RossiSSPTGreen.currentAmmo()
        print("-"*50)
        print("hold hammer: "+str(RossiSSPTGreen.showHToggle()))
        print("hold trigger: "+str(RossiSSPTGreen.showTToggle()))
        if RossiSSPTGreen.getBarrelLock() >= 1:
            RossiSSPTGreen.showBarrel()
        act = input("CMD: ")
        for a in range(len(act)):
            if act[a] == "t":
                if RossiSSPTGreen.getBarrelLock() < 1 and RossiSSPTGreen.getHammer(0) == 0:
                    RossiSSPTGreen.changeBarrelLock(1)
                    print("You push down the button on the top right side, and open up the barrel.")
                    print("The gun is partially open.")
            elif act[a] == "B":
                if RossiSSPTGreen.getHammer(0) == 0:
                    RossiSSPTGreen.changeHammer(0, 1)
                    print("You pull back the hammer slightly, before letting go once it's halfway.")
                    print("The hammer is half cocked.")
                    if RossiSSPTGreen.showTToggle():
                        print("The hammer slams back into position.")
                        RossiSSPTGreen.changeHammer(0, 0)
                        print("KLIK")
                elif RossiSSPTGreen.getHammer(0) == 1:
                    print("The gun is already half cocked.")
                else:
                    print("You can't half cock the gun in this state.")
            elif act[a] == "v":
                if RossiSSPTGreen.getFiremode() == 0:
                    RossiSSPTGreen.changeFiremode(1)
                    print("You push the lever on the left side of the gun back so the red dot is covered.")
                else:
                    RossiSSPTGreen.changeFiremode(0)
                    print("You push the lever on the left side of the gun forward so the red dot is revealed.")
            elif act[a] == "|":
                RossiSSPTGreen.toggleTrigger()
                if RossiSSPTGreen.showTToggle():
                    if RossiSSPTGreen.getFiremode() == 0:
                        RossiSSPTGreen.fireBarrel(0)
                    else:
                        print("You pull the trigger.")
                        if RossiSSPTGreen.getHammer(0) == 2:
                            print("KLIK")
                            RossiSSPTGreen.changeHammer(0, 0)
                        else:
                            print("PLAP")
                        print("You release the trigger after pulling it.")
            elif act[a] == "T":
                if RossiSSPTGreen.getBarrelLock() < 3 and RossiSSPTGreen.getHammer(0) == 0:
                    print("You push down the button on the top right side, and open up the barrel.")
                    print("The gun is fully open.")
                    RossiSSPTGreen.changeBarrelLock(3)
                else:
                    print("The gun is already fully open.")
            elif act[a] == "G":
                if RossiSSPTGreen.getHammer(0) <= 1:
                    RossiSSPTGreen.changeHammer(0, 2)
                    print("You pull back the hammer, letting go once it is fully cocked.")
                    if RossiSSPTGreen.showTToggle():
                        print("The hammer immediately slams into the chamber.")
                        RossiSSPTGreen.fireBarrel(0)
            elif act[a] == "g":
                RossiSSPTGreen.toggleHammer()
                if RossiSSPTGreen.showHToggle():
                    if RossiSSPTGreen.getHammer(0) <= 1:
                        RossiSSPTGreen.changeHammer(0, 2)
                        print("You pull back the hammer, and you keep your thumb on it.")
                    else:
                        print("You put your thumb on the hammer.")
                else:
                    print("You remove your thumb from the hammer.")
                if RossiSSPTGreen.showTToggle() and not RossiSSPTGreen.showHToggle():
                    RossiSSPTGreen.changeHammer(0, 0)
                    print("You ease the hammer into its resting position.")
                    print("The gun is now not cocked.")
            elif act[a] == "b":
                if RossiSSPTGreen.getHammer(0) == 0:
                    RossiSSPTGreen.changeBarrelLock(0)
                    print("You close up the barrel of the gun.")
                else:
                    print("The action is already closed.")
            elif act[a] == "y":
                RossiSSPTGreen.addRound(0)
            elif act[a] == "h":
                RossiSSPTGreen.removeRound(0, 1)
            elif act[a] == "/":
                if not RossiSSPTGreen.showHToggle() and not RossiSSPTGreen.showTToggle():
                    if RossiSSPTGreen.getFiremode() == 0:
                        RossiSSPTGreen.fireBarrel(0)
                    else:
                        print("You pull the trigger.")
                        if RossiSSPTGreen.getHammer(0) == 2:
                            print("KLIK")
                            RossiSSPTGreen.changeHammer(0, 0)
                        else:
                            print("PLAP")
                        print("You release the trigger after pulling it.")
            elif act[a] == "{":
                RossiSSPTGreen.prevRound()
            elif act[a] == "}":
                RossiSSPTGreen.nextRound()
            elif act[a] == "@":
                print("Exiting Program...")
            elif act[a] == " ":
                print("You wait...")
            else:
                print("NOT A VALID COMMAND")
            RossiSSPTGreen.incrementSec(1)
