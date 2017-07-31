numbers = [1, 2, 3, 4, 5, 6, 7, 15, 26, 27, 17, 99, 85, 76, 30, 43, 54, 45, 33]
print(numbers)
multiples = []

length = len(numbers)

for count in range(length):
    check_list = numbers[count]
    if check_list % 5 != 0 or check_list % 3 != 0 and check_list % 2 != 0 and check_list > 1:
        multiples.append(check_list)

lengthOfMultiple = len(multiples)

print(multiples)
