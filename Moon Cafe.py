import os
import time
import platform


def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

print("----------")

while True:
    time.sleep(1)
    clear_screen()
    print("Moon Cafe")
    print("----menue----")
    print("1 = Espresso = ₹80")
    print("2 = Cafe Latte = ₹200")
    print("3 = Mocha = ₹140")
    print("4 = Hot Chocolate = ₹220")
    print("5 = Cold Brew = ₹150")
    print("6 = Frappes = ₹260")

    user_input = int(input("Enter list number: "))

    if user_input == 1: #espresso
        time.sleep(1)
        clear_screen()
        print("Espresso = ₹80 (Selected)")
        items = int(input("How many: "))
        total = items * 80
        print(" Order Confirmed")
        print(f"  order bill = {total}")
        time.sleep(1)
        user_input = int(input("   enter 0 to Main Menue"))
        if user_input == "q":
            continue

    elif user_input == 2: #Cafe Latte
        time.sleep(1)
        print("Cafe Latte = ₹200 (selected)")
        items = int(input("How many: "))
        total = items * 200
        print(f"order bill = {total}")
        print("Order Confirmed")
        time.sleep(1)
        user_input = int(input("enter 0 to Main Menue"))
        if user_input == "q":
           continue


    elif user_input == 3:  #Mocha
        time.sleep(1)
        clear_screen()
        print("Mocha = ₹140 (Selected)")
        items = int(input("How many: "))
        total = items * 140
        print(f"order bill = {total}")
        print("Order Confirmed")
        time.sleep(1)
        user_input = int(input("enter 0 to Main Menue"))
        if user_input == "q":
            continue

    elif user_input == 4:  #Hot Chocolate
        time.sleep(1)
        print("Hot Chocolate = ₹220 (selected)")
        items = int(input("How many: "))
        total = items * 220
        print(f"order bill = {total}")
        print("Order Confirmed")
        time.sleep(1)
        user_input = int(input("enter 0 to Main Menue"))
        if user_input == "q":
           continue


    elif user_input == 5:  #Cold Brew
        time.sleep(1)
        clear_screen()
        print("Cold Brew = ₹150 (Selected)")
        items = int(input("How many: "))
        total = items * 150
        print(f"order bill = {total}")
        print("Order Confirmed")
        time.sleep(1)
        user_input = int(input("enter 0 to Main Menue"))
        if user_input == "q":
            continue

    elif user_input == 6:  #Frappes
        time.sleep(1)
        print("Frappes = ₹260 (selected)")
        items = int(input("How many: "))
        total = items * 260
        print(f"order bill = {total}")
        print("Order Confirmed")
        time.sleep(1)
        user_input = int(input("enter 0 to Main Menue"))
        if user_input == "q":
           continue
    
    else:
        print("Invalid Input")
        break
