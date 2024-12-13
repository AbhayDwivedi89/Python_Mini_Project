
#Python program to find the largest number in an array −

# a = [2,3,4,5,20,76,45,80]
# n = len(a)

# largest = a[0]
# for i in range (1, n):
#     if a[i] > largest:
#         largest = a[i]
        
# print("The largest number in the list is:", largest)


#Python program to store all even numbers from an array in another array −

a = [23,45,67,89,90,56,12,20,70,50,34,450]

b = []

for i in range (1, len(a)):
    if a[i] % 2 == 0:
        b.append(a[i])
        
print(" even numbers = ", b)