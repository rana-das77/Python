#count even and odd numbers in a list
numbers = [2, 4, 7, 8, 9, 13, 767, 434, 545]
even_count = 0
odd_count = 0
for num in numbers:
    if (num%2 == 0):
        even_count += 1
    else:
        odd_count += 1
print ("Even numbers count:", even_count)
print ("Odd numbers count:", odd_count)

        
