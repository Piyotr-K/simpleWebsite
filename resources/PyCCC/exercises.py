def exercise1(n):
    # odds and evens
    # output odds and evens
    # 1 ... n
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(str(i) + " is even")
        else:
            print(str(i) + " is odd")

def exercise2():
    userinput = input("Enter a number: ")
    userinput = int(userinput)
    if 1 <= userinput <= 100:
        print("Within 1 to 100 inclusive")
    else:
        print("Outside of 1 to 100")

def exercise3():
    x = input("Enter an X value: ")
    y = input("Enter a Y value: ")

    temp = x
    x = y
    y = temp

    print("X after swapping: " + x)
    print("Y after swapping: " + y)

def exercise4():
    # Leap year
    # take user input
    # print out if it is a leap year or not
    # Leap years:
    # 2000, 2400
    # Not Leap years:
    # 1800, 1900, 2100, 2200
    year = int(input("Enter a year to test: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

exercise4()