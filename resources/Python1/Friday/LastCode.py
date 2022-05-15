#!/bin/python3

def displayShopItems():
  print("""
1. Cool Sword (100g)
2. Cool Spear (150g)
3. Cool Shield (210g)
4. Cool School (1000g)
5. Cool Armour (200g)
6. Cool Glock 19 (500g)
7. Cool Roger (1g)
""")

def buyItem(number):
    global totalMoney
    number = int(number)
    if number == 1 and totalMoney >= 100:
        # we have to subtract money spent
        totalMoney -= 100
        print("Sword bought!")
        print("Money left: " + str(totalMoney))

bag = []

# starting gold
totalMoney = 1000

print("""
Welcome to the cool shop

:)

What would you like to do in my cool shop?
1. View All Items in the shop
2. View All Items you have
3. Buy item
4. Sell item
5. Exit shop
""")

while True:
    userChoice = int(input("Enter a number: "))
    if userChoice == 1:
        displayShopItems()
    elif userChoice == 2:
        print(bag)
    elif userChoice == 3:
        itemToBuy = input("Enter an item to buy: ")
        if len(bag) == 5:
            print("Bag is full!")
        else:
            buyItem(itemToBuy)
    elif userChoice == 4:
        itemToDelete = input("Enter the item to sell: ")
        for x in range(len(bag)):
            if itemToDelete == bag[x]:
                print(bag[x] + " removed.")
                bag.remove(bag[x])
                break
        else:
            print("Item not found!")
    elif userChoice == 5:
        break
    else:
        print("Invalid")