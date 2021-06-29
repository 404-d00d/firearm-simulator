from CylinderGun import *

CG7 = CylinderGun(0, True, [""], [100], [".375 Win"], ["*KTHROOOOOOOOOOOOOOOOOOOOOOOOOM*"], "chamber", False, 0)

act = ""

while act != "stop":
    print("Tanfoglio Thor Pistol")
    print("Caliber: .375 Winchester")
    print("Amount of .375 Winchester rounds available: "+str(CG7.showCount(0)))
    print("LIST OF ACTIONS:")
    print("t - open barrel")
    print("T - close barrel")
    print("r - insert round")
    print("R - remove round")
    print("| - pull trigger")
    print("g - cock hammer")
    print("h - half-cock hammer")
    print("G - decock hammer")
    print("v - engage safety")
    print("V - disengage safety")
    print(CG7.showTerm()+" closed: "+str(CG7.showLatch()))
    if CG7.showHammer() == 2:
        print("hammer cocked: full cock")
    elif CG7.showHammer() == 1:
        print("hammer cocked: half cock")
    else:
        print("hammer cocked: not cocked")
    if CG7.showFiremode() == 1:
        print("safety engaged: true")
    else:
        print("safety engaged: false")
    if not CG7.showLatch():
        print(CG7.showTerm()+": "+str(CG7.showCylinder()))
    act = input(": ")
    for x in range(len(act)):
        if act[x] == "t":
            if CG7.showLatch():
                print("You push down the button to the left of the hammer, and break open the barrel")
                print("The "+CG7.showTerm()+" is now open")
                if CG7.showRound(0) == CG7.showBullet(x):
                    print("A live round flies out of the "+CG7.showTerm())
                elif CG7.showRound(0) == "Spent "+CG7.showBullet(x):
                    print("A spent round flies out of the "+CG7.showTerm())
                CG7.ejectAllRounds()
                CG7.openCylinder()
            else:
                print("The "+CG7.showTerm()+" is already open")
        elif act[x] == "T":
            if not CG7.showLatch():
                if CG7.showHammer() == 0:
                    print("You cannot close the barrel in this state")
                else:
                    print("You close up the barrel")
                    print("The "+CG7.showTerm()+" is now closed")
                    CG7.closeCylinder()
            else:
                print("The "+CG7.showTerm()+" is already closed")
        elif act[x] == "r":
            CG7.addRound(0, 0)
        elif act[x] == "R":
            if not CG7.showLatch():
                if CG7.showRound(0) == CG7.showBullet(0):
                    print("You pull out a live round from the " + CG7.showTerm())
                else:
                    print("There is nothing to remove")
                CG7.ejectAllRounds()
            else:
                print("You cannot remove a round in this state")
        elif act[x] == "|":
            if CG7.showLatch():
                if CG7.showHammer() == 2:
                    CG7.pullTrigger(0, 0)
                    CG7.cockHammer(0)
                    print("The external hammer is now uncocked")
                else:
                    print("You pull the trigger")
                    print("It is stiff and doesn't budge")
            else:
                print("You pull the trigger")
                print("It is stiff and doesn't budge")
        elif act[x] == "g":
            if CG7.showHammer() == 0 or CG7.showHammer() == 1:
                print("You pull back the external hammer fully")
                print("The external hammer is now fully cocked")
                CG7.cockHammer(2)
            else:
                print("The external hammer is already fully cocked")
        elif act[x] == "G":
            if CG7.showHammer() == 2:
                print("You pull back the external hammer, while pulling the trigger, as you move the hammer to rest")
                print("The external hammer is now decocked")
                CG7.cockHammer(0)
            else:
                print("The external hammer is already uncocked")
        elif act[x] == "h":
            if CG7.showHammer() == 0:
                print("You pull back the external hammer partway")
                print("The external hammer is now half cocked")
                CG7.cockHammer(1)
            else:
                print("The external hammer is already half cocked")
        elif act[x] == "v":
            if CG7.showFiremode() == 0:
                print("You move the safety lever so it fits the notch")
                print("The safety is now engaged")
                CG7.alternateMode(1)
            else:
                print("The safety is already engaged")
        elif act[x] == "V":
            if CG7.showFiremode() == 1:
                print("You move the safety lever so its out of the notch")
                print("The safety is now disengaged")
                CG7.alternateMode(0)
            else:
                print("The safety is already disengaged")
        else:
            print("Not a valid action.")
    print("==>")