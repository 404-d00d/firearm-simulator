from CylinderGun import *

CG6 = CylinderGun(0, True, [""], [100], [".35 Whelen"], ["*KHTHROOOOOOOOOOOOOOOOOOOOOOOOOOOOOM*"], "chamber", False, 0)

act = ""

while act != "stop":
    print("Conneticut Valley Arms Scout Rifle")
    print("Caliber: .35 Whelen")
    print("Amount of .35 Whelen rounds available: "+str(CG6.showCount(0)))
    print("LIST OF ACTIONS:")
    print("t - open barrel")
    print("T - close barrel")
    print("r - insert round")
    print("R - remove round")
    print("| - pull trigger")
    print("g - cock hammer")
    print("G - decock hammer")
    print(CG6.showTerm()+" closed: "+str(CG6.showLatch()))
    if CG6.showHammer() == 1:
        print("hammer cocked: full cock")
    else:
        print("hammer cocked: not cocked")
    if CG6.showFiremode() == 1:
        print("safety engaged: true")
    else:
        print("safety engaged: false")
    if not CG6.showLatch():
        print(CG6.showTerm()+": "+str(CG6.showCylinder()))
    act = input(": ")
    for x in range(len(act)):
        if act[x] == "t":
            if CG6.showLatch():
                print("You push in the tang on the trigger guard, and break the barrel open")
                print("The "+CG6.showTerm()+" is now open")
                CG6.openCylinder()
            else:
                print("The "+CG6.showTerm()+" is already open")
        elif act[x] == "T":
            if not CG6.showLatch():
                print("You push up the barrel back into place")
                print("The "+CG6.showTerm()+" is now closed")
                CG6.closeCylinder()
            else:
                print("The "+CG6.showTerm()+" is already closed")
        elif act[x] == "r":
            CG6.addRound(0, 0)
        elif act[x] == "R":
            if not CG6.showLatch():
                if CG6.showRound(0) == CG6.showBullet(x):
                    print("A live round is pulled out of the " + CG6.showTerm())
                elif CG6.showRound(0) == "Spent " + CG6.showBullet(x):
                    print("A spent round is pulled out out of the " + CG6.showTerm())
                else:
                    print("There is nothing to remove")
                CG6.ejectAllRounds()
            else:
                print("You cannot remove a round in this state")
        elif act[x] == "|":
            if CG6.showLatch() and CG6.showFiremode() == 0:
                if CG6.showHammer() == 1:
                    CG6.pullTrigger(0, 0)
                    CG6.cockHammer(0)
                    print("The external hammer is now uncocked")
                else:
                    print("You pull the trigger")
                    print("It is stiff and doesn't budge")
            else:
                print("You pull the trigger")
                print("It is stiff and doesn't budge")
        elif act[x] == "g":
            if CG6.showHammer() == 0:
                print("You pull back the external hammer")
                print("The external hammer is now cocked")
                CG6.cockHammer(1)
            else:
                print("The external hammer is already cocked")
        elif act[x] == "G":
            if CG6.showHammer() == 1:
                print("You pull back the external hammer, while pulling the trigger, as you move the hammer to rest")
                print("The external hammer is now decocked")
                CG6.cockHammer(0)
            else:
                print("The external hammer is already uncocked")
        else:
            print("Not a valid action.")
    print("==>")