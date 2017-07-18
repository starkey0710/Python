def multiple(number1, number2):
    return number1 % number2 == 0
def FizzBuzz(value):
    if multiple(value, 3) and multiple(value, 5):
        return("FizzBuzz")
    elif multiple(value, 5):
        return("Buzz")
    elif multiple(value, 3):
        return("Fizz")
    else:
        return("Oops")
user = "hi"
while user != "a":
    try:
        user = input("Enter a number:")
        if user == "a":
            print("Bye!")
            break
        number = int(user)
        answer = FizzBuzz(number)
        print(answer)
    except ValueError:
        print("hey that's not a number!")
