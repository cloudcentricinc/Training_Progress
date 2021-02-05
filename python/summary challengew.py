
choice = "-"
while choice!= "0":
    if choice in "12345":
        print("you choose{}".format(choice))

    else:
        print("please choose your option from the list below")
        print("1:\tlearn python")
        print("2:\tlearn java")
        print("3:\tlearn swimming")
        print("4:\tdinner")
        print("5:\tgo to bed")
        print("6:\texit")

    choice = input()
