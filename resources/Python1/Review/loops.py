# difference between for-each and for index
list1 = [1, 2, 3, 4, 5, 6, 7, 8]

# for index loop
# If you need to do index specific stuff
for i in range(len(list1)):
    if list1[i] == list1[i+1]:
        pass

# for-each loop
# If you need to do value specific stuff
lastNum = 0
for i in list1:
    print(i * 2)