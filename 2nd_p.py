#Find the largest number in a listFind the largest number in a list

#Calculate the sum of all elements in a list

#count even and odd numbers in a list

#Remove duplicate elements from a list

#Sort a list without using sort()

'''def largest_num(a, b, c):
    if (a>b and a>c):
        return(a)
    elif (b>a and b>c):
        return(b)
    else:
        return(c)
print(largest_num(56, 64, 87))
'''

'''
numbers = [7, 8, 3498, 373]
print("The largest number:", max(numbers))

'''
'''
numbers = [656, 544, 545, 345, 3487,]
largest =numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print("Largest number:", largest)     

'''

numbers = [1, 2, 3, 4]
print("Sum of the numbers:",sum(numbers))

numbers = [1, 2, 3, 4]
total = 0
for num in numbers:
    
    total += num
    
print("Sum of the numbers:",total)