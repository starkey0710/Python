number = input("Enter a number:")
number = int(number)#number is the number of rows
a = ""#a is the number of * each row
for counter in range(number):
    a = a + "*" #counter equals to the number of * each row
    #since the counter of the first row is 0, add one star
    print(a)
for counter in range(number):
    a = "*"
    b = " "*(number-counter-1) + a + a*counter
    #the difference between Level One and Level Two is the space
    #the space equals to (the total number of rows - the number of * each row -1)
    #the amount of * each row is the same as Level One
    print(b)
for counter in range(number):
    a = "*"
    c = " "*(number-counter-1) + a + a*counter + a*counter
    #Level Three is exactly like Level Two except that it has an extra amount of * each row
    print(c)
for counter in range(number):
    a = "*"
    c = " "*(number-counter-1) + a + a*counter + a*counter
    print(c)
    #the first half of Level Four is the same as Level Three
for counter in range(number):
    a = "*"
    d = " "*(counter+1) + a + a*(number-counter-2) + a*(number-counter-2)
    print(d)
