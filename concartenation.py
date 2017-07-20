number = input("Enter a number:")
number = int(number)#number is the number of rows
for counter in range(number):
    a = "*" + "*" * counter #counter equals to the number of * each row
    #since the counter of the first row is 0, add one star
    print(a)

    b = " " * (number-counter-1) + "*" + "*" * counter
    #the difference between Level One and Level Two is the space
    #the space equals to (the total number of rows - the number of * each row -1)
    #the amount of * each row is the same as Level One
    print(b)

    a = "*"
    c = " " * (number-counter-1) + "*" + "*" * counter + "*" * counter
    #Level Three is exactly like Level Two except that it has an extra amount of * each row
    print(c)

    a = "*"
    c = " " * (number-counter-1) + "*" + "*" * counter + "*" * counter
    print(c)
    #the first half of Level Four is the same as Level Three

    a = "*"
    d = " " * (counter+1) + "*" + "*" * (number-counter-2) + "*" * (number-counter-2)
    print(d)
