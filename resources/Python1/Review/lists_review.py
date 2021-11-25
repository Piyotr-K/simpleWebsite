# Q1
# data = [1, 2, 3, 4]
# data_2 = [1, 2, 4, 3]

# print(data == data_2)

# Q2
# data = [1, "hello", 2, "world"]
# print(data[0]) # arrays start from 0, so prints 1
# print(data[3]) # world

# Q3
# data = [1, "hello", 2, "world"]
# data.append(3)
# print(data)

# Q4
# data = [1, "hello", 2, "world", 3]
# data.insert(3, "teach")
# print(data)

# Q5
# data = ["teach", 1, "hello", 2, "world", 3]
# data.remove("teach")
# print(data)

# Q6
# data = [1, "hello", 2, "world"]
# nice = len(data)
# print(nice)

# Q7
# data = [1, "hello", 2, "world", 3]
# # takes the last element out of the list
# # and returns it
# nice = data.pop()
# print(data)
# print(nice)


# data = [1, 2, 3, 4, 5]
# data1 = []
# Put the reverse of data into data1
# using only pop and append
# no using "magic" numbers, only use 0 and 1
# for x in range(len(data)):
#     data1.append(data.pop())
# print(data1)

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# put the word "even" infront of all the even numbers
# can use magic numbers
# challenge: don't use magic numbers, but can use 2
# (0, 1, 2)
# i = 0
# while i < len(data):
#     # Remainder
#     if data[i] % 2 == 0:
#         data.insert(i, "even")
#         i += 1
#     i += 1

# print(data)