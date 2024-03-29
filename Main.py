import SavageMkIFVT_22LR
import HenrySigleShotShotgun_12Gauge
import HenrySingleShotRifle_223Rem
import RugerNo1_223Rem
import RossiSSPolyTuffyGreen_410Bore
import CharlesDalyTripleThreat_12Gauge
import StoegerDoubleDefenseSXS_12Gauge
import BrowningCynergyCXComposite_12Gauge
import COP357Derringer_357Magnum

guns = ["Henry Single Shot Shotgun Brass Frame = 12 Gauge 3 1/2 Inch", "Henry Single Shot Rifle = .223 Rem/5.56 NATO",
        "Ruger No 1 Rifle = .223 Rem/5.56 NATO", "Savage Mark 1 FVT Rifle = .22 LR",
        "Rossi SS Poly Tuffy Green Shotgun = .410 Bore 3 Inch", "Charles Daly Triple Threat Shotgun = 12 Gauge 3 Inch",
        "Stoeger Double Defense SxS Shotgun = 12 Gauge 3 Inch",
        "Browning Cynergy CX Composite Shotgun = 12 Gauge 3 Inch", "COP 357 Derringer = .357 Magnum/.38 Special"]

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
    #print("To get information on ammunition jams and how to deal with them - type in 'ammojam'")
    act = input("INPUT: ")
    if act == "1":
        HenrySigleShotShotgun_12Gauge.main()
    elif act == "2":
        HenrySingleShotRifle_223Rem.main()
    elif act == "3":
        RugerNo1_223Rem.main()
    elif act == "4":
        SavageMkIFVT_22LR.main()
    elif act == "5":
        RossiSSPolyTuffyGreen_410Bore.main()
    elif act == "6":
        CharlesDalyTripleThreat_12Gauge.main()
    elif act == "7":
        StoegerDoubleDefenseSXS_12Gauge.main()
    elif act == "8":
        BrowningCynergyCXComposite_12Gauge.main()
    elif act == "9":
        COP357Derringer_357Magnum.main()
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
