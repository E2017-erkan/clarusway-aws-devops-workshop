3# Python program to find the largest number among the three input numbers

# creating empty list
lis = []

# user enters the number of elements to put in list
#count = int(input('How many numbers? '))

# iterating till count to append all input elements in list
for n in range(1,6):
    number = int(input('Enter number: '))
    lis.append(number)

# displaying largest element
print("Largest number of the list is :", max(lis))