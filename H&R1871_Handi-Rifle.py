from CylinderGun import *

CG3 = CylinderGun(0, True, [""], [100], [".25-06 Rem"], ["*KTHRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAK*"], "chamber", False, 0)

act = ""

while act != "stop":
    print("H&R 1871 Handi-Rifle Rifle")
    print("Caliber: .25-06 Remington")
    print("Amount of .25-06 Remington rounds available: "+str(CG3.showCount(0)))
    print("LIST OF ACTIONS:")
    print("t - open barrel")
    print("T - close barrel")
    print("r - insert round")
    print("R - remove round")
    print("| - pull trigger")
    print("g - cock hammer")
    print("G - decock hammer")
    print(CG3.showTerm()+" closed: "+str(CG3.showLatch()))
    if CG3.showHammer() == 1:
        print("hammer cocked: full cock")
    else:
        print("hammer cocked: not cocked")
    if not CG3.showLatch():
        print(CG3.showTerm()+": "+str(CG3.showCylinder()))
    act = input(": ")
    for x in range(len(act)):
        if act[x] == "t":
            if CG3.showLatch():
                print("You push down the lever to the right of the hammer, and break open the barrel")
                print("The "+CG3.showTerm()+" is now open")
                if CG3.showRound(0) == CG3.showBullet(x):
                    print("A live round flies out of the "+CG3.showTerm())
                elif CG3.showRound(0) == "Spent "+CG3.showBullet(x):
                    print("A spent round flies out of the "+CG3.showTerm())
                CG3.ejectAllRounds()
                CG3.openCylinder()
            else:
                print("The "+CG3.showTerm()+" is already open")
        elif act[x] == "T":
            if not CG3.showLatch():
                print("You close up the barrel")
                print("The "+CG3.showTerm()+" is now closed")
                CG3.closeCylinder()
            else:
                print("The "+CG3.showTerm()+" is already closed")
        elif act[x] == "r":
            CG3.addRound(0, 0)
        elif act[x] == "R":
            if not CG3.showLatch():
                if CG3.showRound(0) == CG3.showBullet(0):
                    print("You pull out a live round from the " + CG3.showTerm())
                else:
                    print("There is nothing to remove")
                CG3.ejectAllRounds()
            else:
                print("You cannot remove a round in this state")
        elif act[x] == "|":
            if CG3.showLatch():
                if CG3.showHammer() == 1:
                    CG3.pullTrigger(0, 0)
                    CG3.cockHammer(0)
                    print("The external hammer is now uncocked")
                else:
                    print("You pull the trigger")
                    print("It is stiff and doesn't budge")
            else:
                print("You pull the trigger")
                print("It is stiff and doesn't budge")
        elif act[x] == "g":
            if CG3.showHammer() == 0:
                print("You pull back the external hammer")
                print("The external hammer is now cocked")
                CG3.cockHammer(1)
            else:
                print("The external hammer is already cocked")
        elif act[x] == "G":
            if CG3.showHammer() == 1:
                print("You pull back the external hammer, while pulling the trigger, as you move the hammer to rest")
                print("The external hammer is now cocked")
                CG3.cockHammer(0)
            else:
                print("The external hammer is already uncocked")
        else:
            print("Not a valid action.")
    print("==>")