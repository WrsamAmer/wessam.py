def menu():
    return " 1- What Happens if I do not freeze my subscription \n 2- What Days The Gym Are Open? \n 3- How Can I recieve a locker \n 4- What are the requirments to enter the swimming pool \n 5- What is the customer service number \n 6- What is the phone code to know more about the latest gym offers \n 7- What happens if I renew my subscription before it finishes. \n ------------------------"

while True:
    print(menu())
    choice = float(input("Please Choose An Item from the menu : "))
    print("--------------------")
    if choice == 1:
        print("-    If you don’t freeze your subscription, you will lose your count of days.")
        print("--------------------")
    elif choice == 2:
        print("-    The gym does not open on Fridays")
        print("--------------------")
    elif choice == 3:
        print("-    In order to reserve a locker, call the customer support, and ask for a locker.")
        print("--------------------")
    elif choice == 4:
       print("-    You can enter the swimming pool only if you have your swimming cap on.")
       print("--------------------")
    elif choice == 5:
        print("-    If you call 1234 or call 099876666 you will receive customer support")
        print("--------------------")
    elif choice == 6:
        print("-    Dial extension number 5 to know more about the latest gym offers")
        print("--------------------")
    elif choice == 7:
        print("-    If you renew your subscription before its expired, you will get 10% discount")
        print("--------------------")
    elif choice == 8:
        print("-    Please Choose Valid Choice")
        print("-----------------------")

    else:
        print("Thanks For Visiting Us ")