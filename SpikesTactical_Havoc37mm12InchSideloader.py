from CylinderGun import *

CG5 = CylinderGun(0, True, [""], [100], ["37mm"], ["*KTHOOOOOOOOK*"], "chamber", False, 0)

act = ""

while act != "stop":
    print("Spikes Tactical Havoc 37mm 12'' Sideloader Launcher")
    print("Caliber: 37mm rounds")
    print("Amount of 37mm rounds available: "+str(CG5.showCount(0)))
    print("LIST OF ACTIONS:")
    print("t - open barrel")
    print("T - close barrel")
    print("r - insert round")
    print("R - remove round")
    print("| - pull trigger")
    print("v - engage safety")
    print("V - disengage safety")
    print("g - pull back bolt")
    print("G - decock gun")
    print(CG5.showTerm()+" closed: "+str(CG5.showLatch()))
    if CG5.showHammer() == 1:
        print("hammer cocked: full cock")
    else:
        print("hammer cocked: not cocked")
    if CG5.showFiremode() == 1:
        print("safety engaged: true")
    else:
        print("safety engaged: false")
    if not CG5.showLatch():
        print(CG5.showTerm()+": "+str(CG5.showCylinder()))
    act = input(": ")
    for x in range(len(act)):
        if act[x] == "t":
            if CG5.showLatch():
                print("You push a button, then slide open the barrel, and move it into the leftmost notch")
                print("The "+CG5.showTerm()+" is now open")
                CG5.openCylinder()
            else:
                print("The "+CG5.showTerm()+" is already open")
        elif act[x] == "T":
            if not CG5.showLatch():
                print("You push the barrel out of the leftmost notch, and slide it back")
                print("The "+CG5.showTerm()+" is now closed")
                CG5.closeCylinder()
            else:
                print("The "+CG5.showTerm()+" is already closed")
        elif act[x] == "r":
            CG5.addRound(0, 0)
        elif act[x] == "R":
            if not CG5.showLatch():
                if CG5.showRound(0) == CG5.showBullet(x):
                    print("A live round is pulled out of the " + CG5.showTerm())
                elif CG5.showRound(0) == "Spent " + CG5.showBullet(x):
                    print("A spent round is pulled out out of the " + CG5.showTerm())
                else:
                    print("There is nothing to remove")
                CG5.ejectAllRounds()
            else:
                print("You cannot remove a round in this state")
        elif act[x] == "|":
            if CG5.showLatch() and CG5.showFiremode() == 0:
                if CG5.showHammer() == 1:
                    CG5.pullTrigger(0, 0)
                    CG5.cockHammer(0)
                    print("The bolt is now uncocked")
                else:
                    print("You pull the trigger")
                    print("It is stiff and doesn't budge")
            else:
                print("You pull the trigger")
                print("It is stiff and doesn't budge")
        elif act[x] == "v":
            if CG5.showFiremode() == 0:
                print("You push in the crossbolt safety")
                print("The safety is now engaged")
                CG5.alternateMode(1)
            else:
                print("The safety is already engaged")
        elif act[x] == "V":
            if CG5.showFiremode() == 1:
                print("You push out the crossbolt safety")
                print("The safety is now disengaged")
                CG5.alternateMode(0)
            else:
                print("The safety is already disengaged")
        elif act[x] == "g":
            if CG5.showHammer() == 0:
                print("You pull back the bolt")
                print("The bolt is now cocked")
                CG5.cockHammer(1)
            else:
                print("The bolt is already cocked")
        elif act[x] == "G":
            if CG5.showHammer() == 1:
                print("You pull back the bolt, while pulling the trigger, as you move the bolt to rest")
                print("The internal hammer is now decocked")
                CG5.cockHammer(0)
            else:
                print("The external hammer is already uncocked")
        else:
            print("Not a valid action.")
    print("==>")