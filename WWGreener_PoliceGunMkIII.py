from CylinderGun import *

CG1 = CylinderGun(0, True, [""], [100], ["14 Gauge Greener"], ["*THOOOOOOOOOOOOOOOOOOOOM*"], "chamber", False, 0)

act = ""

while act != "stop":
    print("W. W. Greener Police Gun MkIII Shotgun")
    print("Caliber: 14 Gauge Greener")
    print("Amount of .577/450 rounds available: "+str(CG1.showCount(0)))
    print("LIST OF ACTIONS:")
    print("t - open lever")
    print("T - close lever")
    print("r - insert round")
    print("R - remove round")
    print("| - pull trigger")
    print("v - engage safety")
    print("V - disengage safety")
    print(CG1.showTerm()+" closed: "+str(CG1.showLatch()))
    if CG1.showHammer() == 1:
        print("hammer cocked: full cock")
    else:
        print("hammer cocked: not cocked")
    if CG1.showFiremode() == 1:
        print("safety engaged: true")
    else:
        print("safety engaged: false")
    if not CG1.showLatch():
        print(CG1.showTerm()+": "+str(CG1.showCylinder()))
    act = input(": ")
    for x in range(len(act)):
        if act[x] == "t":
            if CG1.showLatch():
                print("You push down the lever below the trigger guard")
                print("The "+CG1.showTerm()+" is now open")
                print("The internal hammer is now cocked")
                print("The safety is now engaged")
                if CG1.showRound(0) == CG1.showBullet(x):
                    print("A live round flies out of the "+CG1.showTerm())
                elif CG1.showRound(0) == "Spent "+CG1.showBullet(x):
                    print("A spent round flies out of the "+CG1.showTerm())
                CG1.ejectAllRounds()
                CG1.cockHammer(1)
                CG1.openCylinder()
                CG1.alternateMode(1)
            else:
                print("The "+CG1.showTerm()+" is already open")
        elif act[x] == "T":
            if not CG1.showLatch():
                print("You push up the lever below the trigger guard, until it touches the stock")
                print("The "+CG1.showTerm()+" is now closed")
                CG1.closeCylinder()
            else:
                print("The "+CG1.showTerm()+" is already closed")
        elif act[x] == "r":
            CG1.addRound(0, 0)
        elif act[x] == "R":
            if not CG1.showLatch():
                if CG1.showRound(0) == CG1.showBullet(0):
                    print("You pull out a live round from the " + CG1.showTerm())
                else:
                    print("There is nothing to remove")
                CG1.ejectAllRounds()
            else:
                print("You cannot remove a round in this state")
        elif act[x] == "|":
            if CG1.showLatch() and CG1.showFiremode() == 0:
                if CG1.showHammer() == 1:
                    CG1.pullTrigger(0, 0)
                    CG1.cockHammer(0)
                    print("The internal hammer is now uncocked")
                else:
                    print("You pull the trigger")
                    print("It is stiff and doesn't budge")
            else:
                print("You pull the trigger")
                print("It is stiff and doesn't budge")
        elif act[x] == "v":
            if CG1.showFiremode() == 0:
                print("You push up the safety lever")
                print("The safety is now engaged")
                CG1.alternateMode(1)
            else:
                print("The safety is already engaged")
        elif act[x] == "V":
            if CG1.showFiremode() == 1:
                print("You push down the safety lever")
                print("The safety is now disengaged")
                CG1.alternateMode(0)
            else:
                print("The safety is already disengaged")
        else:
            print("Not a valid action.")
    print("==>")