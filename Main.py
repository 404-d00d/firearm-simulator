import SavageMkIFVT_22LR
import HenrySigleShotShotgun_12Gauge
import HenrySingleShotRifle_243Win

guns = ["Savage Mk 1 FVT 22LR", "Henry Single Shot Shotgun Brass 12 Gauge", "Henry Single Shot Rifle .243 Win"]

act = ""
while act != "exit":
    print("-"*50)
    print("Choose a gun to use...")
    for x in range(len(guns)):
        print(str(x+1)+" - "+guns[x])
    act = input("INPUT: ")
    if act == "1":
        SavageMkIFVT_22LR.main()
    elif act == "2":
        HenrySigleShotShotgun_12Gauge.main()
    elif act == "3":
        HenrySingleShotRifle_243Win.main()
    elif act == "exit":
        print("Thank you for using the program. Have a nice day.")
    else:
        print("ERROR: Not a valid command")
