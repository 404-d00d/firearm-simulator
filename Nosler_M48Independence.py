from CylinderGun import *

CG2 = CylinderGun(0, True, [""], [100], ["22 Nosler"], ["*KHTRAAAAAAAAAAAAAAAAAAAAk*"], "chamber", False, 0)

act = ""

while act != "stop":
    print("Nosler M48 Independence Pistol")
    print("Caliber: 22 Nosler")
    print("Amount of 22 Nosler rounds available: "+str(CG2.showCount(0)))
    print("LIST OF ACTIONS:")
    print("t - open bolt")
    print("T - close boltr")
    print("r - insert round")
    print("R - remove round")
    print("| - pull trigger")
    print("v - engage safety")
    print("V - disengage safety")
    print(CG2.showTerm()+" closed: "+str(CG2.showLatch()))
    if CG2.showHammer() == 1:
        print("hammer cocked: full cock")
    else:
        print("hammer cocked: not cocked")
    if CG2.showFiremode() == 1:
        print("safety engaged: true")
    else:
        print("safety engaged: false")
    if not CG2.showLatch():
        print(CG2.showTerm()+": "+str(CG2.showCylinder()))
    act = input(": ")
    for x in range(len(act)):
        if act[x] == "t":
            if CG2.showLatch():
                print("You rotate and pull back the bolt")
                print("The "+CG2.showTerm()+" is now open")
                print("The internal hammer is now cocked")
                if CG2.showRound(0) == CG2.showBullet(x):
                    print("A live round flies out of the "+CG2.showTerm())
                elif CG2.showRound(0) == "Spent "+CG2.showBullet(x):
                    print("A spent round flies out of the "+CG2.showTerm())
                CG2.ejectAllRounds()
                CG2.cockHammer(1)
                CG2.openCylinder()
            else:
                print("The "+CG2.showTerm()+" is already open")
        elif act[x] == "T":
            if not CG2.showLatch():
                print("You push and rotate the bolt back to its locked position")
                print("The "+CG2.showTerm()+" is now closed")
                CG2.closeCylinder()
            else:
                print("The "+CG2.showTerm()+" is already closed")
        elif act[x] == "r":
            CG2.addRound(0, 0)
        elif act[x] == "R":
            if not CG2.showLatch():
                if CG2.showRound(0) == CG2.showBullet(0):
                    print("You pull out a live round from the " + CG2.showTerm())
                else:
                    print("There is nothing to remove")
                CG2.ejectAllRounds()
            else:
                print("You cannot remove a round in this state")
        elif act[x] == "|":
            if CG2.showLatch() and CG2.showFiremode() == 0:
                if CG2.showHammer() == 1:
                    CG2.pullTrigger(0, 0)
                    CG2.cockHammer(0)
                    print("The internal hammer is now uncocked")
                else:
                    print("You pull the trigger")
                    print("It is stiff and doesn't budge")
            else:
                print("You pull the trigger")
                print("It is stiff and doesn't budge")
        elif act[x] == "v":
            if CG2.showFiremode() == 0:
                print("You push in the crossbolt safety")
                print("The safety is now engaged")
                CG2.alternateMode(1)
            else:
                print("The safety is already engaged")
        elif act[x] == "V":
            if CG2.showFiremode() == 1:
                print("You push out the crossbolt safety")
                print("The safety is now disengaged")
                CG2.alternateMode(0)
            else:
                print("The safety is already disengaged")
        else:
            print("Not a valid action.")
    print("==>")