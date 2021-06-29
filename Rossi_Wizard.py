from CylinderGun import *

CG4 = CylinderGun(0, True, [""], [100], [".22-250 Rem"], ["*KTHRAAAAAAAAAAAAAAAAAAAAAAK*"], "chamber", False, 0)

act = ""

while act != "stop":
    print("Rossi Wizard Rifle")
    print("Caliber: .22-250 Remington")
    print("Amount of .22-250 Remington rounds available: "+str(CG4.showCount(0)))
    print("LIST OF ACTIONS:")
    print("t - open barrel")
    print("T - close barrel")
    print("r - insert round")
    print("R - remove round")
    print("| - pull trigger")
    print("g - cock hammer")
    print("G - decock hammer")
    print("v - engage safety")
    print("V - disengage safety")
    print(CG4.showTerm()+" closed: "+str(CG4.showLatch()))
    if CG4.showHammer() == 1:
        print("hammer cocked: full cock")
    else:
        print("hammer cocked: not cocked")
    if CG4.showFiremode() == 1:
        print("safety engaged: true")
    else:
        print("safety engaged: false")
    if not CG4.showLatch():
        print(CG4.showTerm()+": "+str(CG4.showCylinder()))
    act = input(": ")
    for x in range(len(act)):
        if act[x] == "t":
            if CG4.showLatch():
                print("You push down the lever to the right of the hammer, and break open the barrel")
                print("The "+CG4.showTerm()+" is now open")
                if CG4.showRound(0) == CG4.showBullet(x):
                    print("A live round flies out of the "+CG4.showTerm())
                elif CG4.showRound(0) == "Spent "+CG4.showBullet(x):
                    print("A spent round flies out of the "+CG4.showTerm())
                CG4.ejectAllRounds()
                CG4.openCylinder()
            else:
                print("The "+CG4.showTerm()+" is already open")
        elif act[x] == "T":
            if not CG4.showLatch():
                print("You close up the barrel")
                print("The "+CG4.showTerm()+" is now closed")
                CG4.closeCylinder()
            else:
                print("The "+CG4.showTerm()+" is already closed")
        elif act[x] == "r":
            CG4.addRound(0, 0)
        elif act[x] == "R":
            if not CG4.showLatch():
                if CG4.showRound(0) == CG4.showBullet(0):
                    print("You pull out a live round from the " + CG4.showTerm())
                else:
                    print("There is nothing to remove")
                CG4.ejectAllRounds()
            else:
                print("You cannot remove a round in this state")
        elif act[x] == "|":
            if CG4.showLatch():
                if CG4.showHammer() == 1:
                    CG4.pullTrigger(0, 0)
                    CG4.cockHammer(0)
                    print("The external hammer is now uncocked")
                else:
                    print("You pull the trigger")
                    print("It is stiff and doesn't budge")
            else:
                print("You pull the trigger")
                print("It is stiff and doesn't budge")
        elif act[x] == "g":
            if CG4.showHammer() == 0:
                print("You pull back the external hammer")
                print("The external hammer is now cocked")
                CG4.cockHammer(1)
            else:
                print("The external hammer is already cocked")
        elif act[x] == "G":
            if CG4.showHammer() == 1:
                print("You pull back the external hammer, while pulling the trigger, as you move the hammer to rest")
                print("The external hammer is now decocked")
                CG4.cockHammer(0)
            else:
                print("The external hammer is already uncocked")
        elif act[x] == "v":
            if CG4.showFiremode() == 0:
                print("You move the safety lever to cover up the red dot")
                print("The safety is now engaged")
                CG4.alternateMode(1)
            else:
                print("The safety is already engaged")
        elif act[x] == "V":
            if CG4.showFiremode() == 1:
                print("You move the safety lever so the red dot shows up")
                print("The safety is now disengaged")
                CG4.alternateMode(0)
            else:
                print("The safety is already disengaged")
        else:
            print("Not a valid action.")
    print("==>")