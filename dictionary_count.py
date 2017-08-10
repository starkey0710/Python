word = input("Type a word to see how many times each letter appears")
dictionary = {
}
for letter in word:
    if letter in dictionary:
        dictionary[letter] = dictionary[letter] + 1
    else:
        dictionary[letter] = 1
for key, val in dictionary.items():
    print("Letter: " + key + "\tAppeared: " + str(val) + " " + "times")
