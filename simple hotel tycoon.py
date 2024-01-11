import random as rm
import time as tm
import os

guests_growth_rate = [1, 2, 1, 2, 1, 1]

golden_statue = 0
diamond_statue = 0
luxury_painting = 0
bonus_money = 0

guests = 0
floors = 1
comfort = 10

money = 100
limit = 10

shop_item = {"1": 100, "2": 300, "3" : 0}
special_item = {"1" : 10000, "2" : 200000, "3" : 500000, "4" : 0}


class shop:
    def item_shop():
        print("1. Upgrade Comfort $100")
        print("2. Upgrade Floor $300")
        print("3. Special Shop")
        print("4. Back")
        print("Your money: ", money)
        
    def special_shop():
        print("1. Golden Statue $10k")
        print("2. Diamond Statue $200k")
        print("3. Luxury Painting $500k")
        print("4. Back")
        print("Your money: ", money)
        
class menu:
    def main_menu():
        print("Simple Hotel Tycoon")
        print("1. Start Game")
        print("2. About")
        print("3. Exit Game")

    def about():
        print(
            "This simple game was created by Nuno337 under MIT License, this game is about you become the owner hotel and gain more money to upgrade your hotel"
        )


class game:
    def game_menu():
        print("1. Guests Stats")
        print("2. Hotel Stats")
        print("3. Shop")
        print("4. Tap Section")

    def game1():
        print("Guests Stats")
        print("Guests: ", guests, "/", limit)

    def game2():
        print("Hotel Stats")
        print("Floors: ", floors)
        print("Comfort Meter: ", comfort)
        print("Space: ", guests, "/", limit)
        print("Bonus Income: ", bonus_money)
        print("Golden Statue: ", golden_statue, "/", "1")
        print("Diamond Statue: ", diamond_statue, "/", "1")
        print("Luxury Paintings: ", luxury_painting, "/", "5")
    
    def game3():
        print("1. Tap to add guests")
        print("2. Tap to earn money")
        print("3. Back")

try:
    while True:
        menu.main_menu()
        choice = input("Input your choice: ")
        if choice == "3":
            print("Exit game...")
            tm.sleep(2)
            print("Success!")
            break
        elif choice == "2":
            menu.about()
            input("Press Enter to continue")
            os.system("cls" if os.name == "nt" else "clear")
        elif choice == "1":
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                game.game_menu()
                choice = input("Please input your choice: ")
                if choice == "1":
                    game.game1()
                    input("Press Enter to continue")
                elif choice == "2":
                    game.game2()
                    input("Press Enter to continue")
                elif choice == "3":
                    shop.item_shop()
                    choice = input("Choose an item to upgrade! ")
                    if choice in shop_item:
                        if choice == "1":
                            if money >= 100:
                                print("Successfully Upgraded!")
                                money -= 100             
                                input("Press Enter to continue")
                            else:
                                print("Oops, not enough money")
                                input("Press Enter to continue")
                        elif choice == "2":
                            if money >= 300:
                                print("Successfully Upgraded!")
                                money -= 300
                                floors += 1
                                limit += 5
                                input("Press Enter to continue")
                            else:
                                print("Oops, not enough money!")
                                input("Press Enter to continue")
                        elif choice == "3":
                            while True:
                                shop.special_shop()
                                choice = input("Please input your choice: ")
                                if choice in special_item:
                                    if choice == "1":
                                        if money >= 10000:
                                            if golden_statue == 0:
                                                print("Successfully bought")
                                                golden_statue += 1
                                                bonus_money += 100
                                                input("Press Enter to continue")
                                            else:
                                                print("You're already owned it!")
                                        else:
                                           print("Not enough money")
                                    elif choice == "2":
                                        if money >= 200000:
                                            if diamond_statue == 0:
                                                money -= special_item[choice]
                                                diamond_statue += 1
                                                bonus_money += 200
                                                print("Successfully bought")
                                                input("Press Enter to continue")
                                            else:
                                                print("You're already own it!")
                                        else:
                                            print("Not enough money!")  
                                    elif choice == "4":
                                                          print("Leaving...")
                                                          tm.sleep(2)
                                                          print("Success!")
                                                          break
                                    elif choice == "3":
                                        if money >= 500_000:
                                            if luxury_painting < 5:
                                                money -= 500_000
                                                luxury_painting += 1                                        
                                                print("Successfully bought")
                                                input("Press Enter to continue")
                                            else:
                                                print("The slot for this item is on limit!")
                                        else:
                                            print("You don't have enough money")
                                            input("Press Enter to Continue")    
                                            os.system('cls' if os.name == "nt" else 'clear')       
                                
                                                                                
                                                                                
                                else:
                                    print("Invalid choice!")
                                    input("Press Enter to continue")     
                    else:
                        print("Invalid choice!")
                        input("Press Enter to continue")
                elif choice == "4":
                    while True:
                        game.game3()
                        choice = input("Input your choice: ")
                        if choice == "1":
                            while True:
                                gueran = rm.choice(guests_growth_rate)
                                print("Guests: ", guests)
                                choice = input("Tap Enter to add guests (type 'leave' to leave this menu): ")
                                if choice.lower() != "leave":
                                    if guests < limit:
                                        guests += gueran
                                    else:
                                        guests = limit
                                        print("Not enough space!")                              
                                else:
                                    print("Leaving...")
                                    tm.sleep(1)
                                    print("Success!")
                                    tm.sleep(0.5)
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break
                        elif choice == "2":
                            while True:
                                choice = input("Press enter to continue (type 'leave' if you want to leave this menu): ").lower()
                                if choice.lower() != "leave":
                                    earnings = 1 * guests
                                    money += earnings + bonus_money
                                    print("Your money:", money)
                                else:
                                    print("Leaving...")
                                    tm.sleep(1)
                                    print("Success!")
                                    tm.sleep(0.5)
                                    os.system('cls' if os.name == "nt" else 'clear')
                                    break
                        elif choice == "3":
                            break                   
                else:
                    print("Invalid choices!")
                    input("Press Enter to continue")
        else:
            print("Enter a valid choice!")
except ValueError:
    print("Invalid!")