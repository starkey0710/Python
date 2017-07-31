#1
fruit = ["apple", "banana", "carrot"]
for counter in range(3):
    print(fruit[counter])
#2
fruit = ["apple", "banana", "carrot"]
for counter in range(3):
    print(fruit[counter] + "!")"
#3
fruit = ["apple ", "banana ", "carrot "]
for counter in range(3):
    a = ""
    for number in range(3):
        a = a + fruit[counter]
    print(a)
