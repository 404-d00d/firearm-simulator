#
cont=True
while(cont):

    USD=float(input("Please enter an amount of US Currency:"))
    Q=USD//0.25
    D=USD//0.10
    N=USD//0.05
    P=USD/0.01

    print("Maximum amount of quarters:", Q)
    print("Maximum amount of dimes:", D)
    print("Maximum amount of nickels:", N)
    print("Maximum amount of pennies:", P)

#You can type in yes and it wont be case sensitive

    cont2=True
    while(cont2):

        ans2=input("Do you want to do another banking transaction yes/no")
        if (ans2.lower()== "yes"):
            cont=True
            cont2=False
            print("Allright, here we go.")
        elif ans2.lower()== ("no"):
            cont=False
            cont2=False
            print("Well fine then. GO BANK SOMEWHERE ELSE!")
            
        else:
            print("Type in something I can actually UNDERSTAND.")
            cont=False
            cont2=True
