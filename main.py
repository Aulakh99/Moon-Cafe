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
    print("----menu----")
    print("1 = Espresso = ₹80")
    print("2 = Cafe Latte = ₹200")
    print("3 = Mocha = ₹140")
    print("4 = Hot Chocolate = ₹220")
    print("5 = Cold Brew = ₹150")
    print("6 = Frappes = ₹260")

    user_input = int(input("Enter list number: "))

    if user_input == 1: #espresso
        time.sleep(1.5)
        clear_screen()
        print("Espresso = ₹80 (Selected)") #price 
        items = int(input("How many: "))
        total = items * 80 #calcu price
        time.sleep(0.5) #time
        table_input = int(input("Table Number: "))
        time.sleep(0.5) #time
        print(f"Table no = {table_input} Wating Time 10min ")
        print("Order Confirmed")
        time.sleep(0.5) #time
        print(f"order bill = {total}")
        time.sleep(1)

        user_exit = int(input("enter 0 to Main Menue: "))
        if user_exit == 0:
            print("thank you for visiting Moon Cafe ")
            continue
        else:
            print("Invalid Statement")

            

    elif user_input == 2: #Cafe Latte
        time.sleep(1.5)
        print("Cafe Latte = ₹200 (selected)")
        items = int(input("How many: "))
        total = items * 200 #calcu price
        time.sleep(0.5)
        print(f"order bill = {total}")
        table_input = int(input("Table Number: "))
        time.sleep(0.5) #time
        print(f"Table no = {table_input} Wating Time 10min ")
        time.sleep(0.5)
        print("Order Confirmed")
        time.sleep(1)
        user_input = int(input("enter 0 to Main Menue: "))
        if user_input == 0:
            print("thank you for visiting Moon Cafe ")
            continue
           
        else:
            print("Invalid Statement")
            


    elif user_input == 3:  #Mocha
        time.sleep(1.5)
        clear_screen()
        print("Mocha = ₹140 (Selected)")
        items = int(input("How many: "))
        total = items * 140 #calcu price
        time.sleep(0.5)
        print(f"order bill = {total}")
        time.sleep(0.5)
        table_input = int(input("Table Number: "))
        time.sleep(0.5) #time
        print(f"Table no = {table_input} Wating Time 10min ")
        time.sleep(0.5)
        print("Order Confirmed")
        time.sleep(0.5)
        print(f"order bill = {total}")
        time.sleep(0.5)
        user_input = int(input("enter 0 to Main Menue: "))
        if user_input == 0:
            print("thank you for visiting Moon Cafe ")
            continue
        else:
            print("Invalid Statement")
            

    elif user_input == 4:  #Hot Chocolate
        time.sleep(1.5)
        print("Hot Chocolate = ₹220 (selected)")
        items = int(input("How many: "))
        total = items * 220 #calcu price
        time.sleep(0.5)
        print(f"order bill = {total}")
        time.sleep(0.5)
        table_input = int(input("Table Number: "))
        time.sleep(0.5) #time
        print(f"Table no = {table_input} Wating Time 10min ")
        print("Order Confirmed")
        time.sleep(0.5)
        user_input = int(input("enter 0 to Main Menue: "))
        if user_input == 0:
           print("thank you for visiting Moon Cafe ")
           continue
        else:
           print("Invalid Statement")
           


    elif user_input == 5:  #Cold Brew
        time.sleep(1.5)
        clear_screen()
        print("Cold Brew = ₹150 (Selected)")
        items = int(input("How many: "))
        total = items * 150 #calcu price
        time.sleep(0.5)
        print(f"order bill = {total}")
        time.sleep(0.5)
        table_input = int(input("Table Number: "))
        time.sleep(0.5) #time
        print(f"Table no = {table_input} Wating Time 10min ")
        print("Order Confirmed")
        time.sleep(1)
        user_input = int(input("enter 0 to Main Menue: "))
        if user_input == 0:
            print("thank you for visiting Moon Cafe ")
            continue
        else:
            print("Invalid Statement")
            

    elif user_input == 6:  #Frappes
        time.sleep(1.5)
        print("Frappes = ₹260 (selected)")
        items = int(input("How many: "))
        total = items * 260 #calcu price
        time.sleep(0.5)
        print(f"order bill = {total}")
        time.sleep(0.5)
        table_input = int(input("Table Number: "))
        time.sleep(0.5) #time
        print(f"Table no = {table_input} Wating Time 10min ")
        print("Order Confirmed")
        time.sleep(0.5)
        user_input = int(input("enter 0 to Main Menue: "))
        if user_input == 0:
            print("thank you for visiting Moon Cafe ")
            continue
           
        else:   #items end                           
           print("Invalid Statement")
           
    
    else: #main loop
        print("Invalid Input")
        break
