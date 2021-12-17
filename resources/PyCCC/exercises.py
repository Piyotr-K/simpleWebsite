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

def exercise5():
    # take user input
    # convert their input (celsius) to fahrenheit
    # formula: celsius * 1.8 + 32 = fahrenheit
    # print out the answer
    # 1 C to 33.8 F
    # 6 C to 42.8 F
    # 6.5 to 43.7 F
    ui = float(input("Enter celsius time: "))
    ans = ui * 1.8 + 32
    print(f"Your input converted is {ans} degrees fahrenheit.")

def exercise6(start, end):
    # Find all the prime numbers between the start and end numbers (incl.)
    # 1 7
    # 2, 3, 5, 7
    # 5 9
    # 5 7
    # 20 50
    # 23 29 31 37 41 43 47
    # Assume correct parameters
    # Print all prime numbers
    for i in range(start, end + 1):
        if i > 1:
            for div in range(2, i):
                if i % div == 0:
                    break
            else:
                print(i, end=", ")

exercise6(0, 100)