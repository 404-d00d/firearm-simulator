import SavageMkIFVT_22LR
import HenrySigleShotShotgun_12Gauge
import HenrySingleShotRifle_243Win
import RugerNo1_65CM
import RossiSSPolyTuffyGreen_410Bore

guns = ["Henry Single Shot Shotgun Brass Frame = 12 Gauge", "Henry Single Shot Rifle = .243 Win",
        "Ruger No 1 Rifle = 6.5 CM", "Savage Mark 1 FVT Rifle = .22 LR",
        "Rossi SS Poly Tuffy Green Shotgun = .410 Bore"]

print("_____________________")
print("|   GUN SIMULATOR   |")
print("|-------------------|")
act = ""
while act != "exit":
    print("-"*50)
    print("Choose a gun to use by putting in the number and hitting enter...")
    for x in range(len(guns)):
        print(str(x+1)+" - "+guns[x])
    print("To leave the program - type in 'exit'")
    print("To get the 4 main rules of gun safety - type in 'safe'")
    act = input("INPUT: ")
    if act == "1":
        HenrySigleShotShotgun_12Gauge.main()
    elif act == "2":
        HenrySingleShotRifle_243Win.main()
    elif act == "3":
        RugerNo1_65CM.main()
    elif act == "4":
        SavageMkIFVT_22LR.main()
    elif act == "5":
        RossiSSPolyTuffyGreen_410Bore.main()
    elif act == "safe":
        print("============ THE FOUR MAIN RULES OF GUN SAFETY ============")
        print("= Even if this is a simulation, ALWAYS FOLLOW THESE RULES =")
        print("===========================================================")
        print("1. TREAT EVERY GUN AS IF IT IS ALWAYS LOADED.")
        print("2. ALWAYS KEEP THE GUN POINTED IN A SAFE DIRECTION.")
        print("3. ALWAYS BE SURE OF YOUR TARGET AND WHATS BEHIND IT.")
        print("4. KEEP YOUR FINGER OFF OF THE TRIGGER UNTIL YOU ARE READY TO FIRE.")
    elif act == "exit":
        print("Thank you for using the program. Have a nice day.")
    else:
        print("ERROR: Not a valid command")
