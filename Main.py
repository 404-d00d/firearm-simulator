import SavageMkIFVT_22LR
import HenrySigleShotShotgun_12Gauge
import HenrySingleShotRifle_243Win
import RugerNo1_65CM

guns = ["Henry Single Shot Shotgun Brass 12 Gauge", "Henry Single Shot Rifle .243 Win", "Ruger No 1 Rifle 6.5 CM",
        "Savage Mark 1 FVT Rifle .22 LR"]

act = ""
while act != "exit":
    print("-"*50)
    print("Choose a gun to use...")
    for x in range(len(guns)):
        print(str(x+1)+" - "+guns[x])
    act = input("INPUT: ")
    if act == "1":
        HenrySigleShotShotgun_12Gauge.main()
    elif act == "2":
        HenrySingleShotRifle_243Win.main()
    elif act == "3":
        RugerNo1_65CM.main()
    elif act == "4":
        SavageMkIFVT_22LR.main()
    elif act == "exit":
        print("Thank you for using the program. Have a nice day.")
    else:
        print("ERROR: Not a valid command")
