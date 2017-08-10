import random
username = input("Please enter a username.")
dictionary = {
}

choices = ["heads", "tails"]
choice = random.randint(0,1)

guess = input("Guess if the coin is heads or tails:")
if guess == "choice":
    print("You got it RIGHT!")
    dictionary[score] = dictionary[score] + 1
else:
    print("Oops.")



for key, val in dictionary.items():
    print("username: " + key + "\t score: " + str(val))
