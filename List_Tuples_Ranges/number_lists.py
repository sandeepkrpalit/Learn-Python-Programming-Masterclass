empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

#Nested lists
numbers = [even, odd]
print(numbers)

#loop through the nested list
for number_list in numbers:
    print(number_list)

    for value in number_list:
        print(value)
