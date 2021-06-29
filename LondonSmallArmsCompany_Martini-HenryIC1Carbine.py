from CylinderGun import *

CG0 = CylinderGun(0, True, [""], [100], [".577/450"], ["*KTHOOOOOOOOOOOOOOOM*"], "chamber", False, 0)

act = ""

while act != "stop":
    print("London Small Arms Company Martini-Henry I.C.1 Carbine Rifle")
    print("Caliber: .577/450 Martini-Henry")
    print("Amount of .577/450 rounds available: "+str(CG0.showCount(0)))
    print("LIST OF ACTIONS:")
    print("t - open lever")
    print("T - close lever")
    print("r - insert round")
    print("R - remove round")
    print("| - pull trigger")
    print(CG0.showTerm()+" closed: "+str(CG0.showLatch()))
    if CG0.showHammer() == 1:
        print("hammer cocked: full cock")
    else:
        print("hammer cocked: not cocked")
    if not CG0.showLatch():
        print(CG0.showTerm()+": "+str(CG0.showCylinder()))
    act = input(": ")
    for x in range(len(act)):
        if act[x] == "t":
            if CG0.showLatch():
                print("You push down the lever below the trigger guard")
                print("The "+CG0.showTerm()+" is now open")
                print("The internal hammer is now cocked")
                if CG0.showRound(0) == CG0.showBullet(x):
                    print("A live round flies out of the "+CG0.showTerm())
                elif CG0.showRound(0) == "Spent "+CG0.showBullet(x):
                    print("A spent round flies out of the "+CG0.showTerm())
                CG0.ejectAllRounds()
                CG0.cockHammer(1)
                CG0.openCylinder()
            else:
                print("The "+CG0.showTerm()+" is already open")
        elif act[x] == "T":
            if not CG0.showLatch():
                print("You push up the lever below the trigger guard, until it touches the stock")
                print("The "+CG0.showTerm()+" is now closed")
                CG0.closeCylinder()
            else:
                print("The "+CG0.showTerm()+" is already closed")
        elif act[x] == "r":
            CG0.addRound(0, 0)
        elif act[x] == "R":
            if not CG0.showLatch():
                if CG0.showRound(0) == CG0.showBullet(0):
                    print("You pull out a live round from the " + CG0.showTerm())
                else:
                    print("There is nothing to remove")
                CG0.ejectAllRounds()
            else:
                print("You cannot remove a round in this state")
        elif act[x] == "|":
            if CG0.showLatch():
                if CG0.showHammer() == 1:
                    CG0.pullTrigger(0, 0)
                    CG0.cockHammer(0)
                    print("The  internal hammer is now uncocked")
                else:
                    print("You pull the trigger")
                    print("It is stiff and doesn't budge")
            else:
                print("You pull the trigger")
                print("It is stiff and doesn't budge")
        else:
            print("Not a valid action.")
    print("==>")