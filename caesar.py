import sys

userNum = input("What number do you want to use? ")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def newAlpha():
    for count in alphabet:
        newAlphabet = ""
        ascii = ord(alphabet[count]) #turns all the alphabet values to ascii values
        ascii = ascii + userNum
        newLetter = chr(ascii)
        newAlphabet = newAlphabet + newLetter

def read():
    readmessage = open ("in.txt", "r")
    linemessage = readmessage.readline()
    linemessage = linemessage.rstrip("\n")

def encrypt():
    read()
    for i in range (len(linemessage)):
        newMessage = ""
        letter = str(linemessage[i])
        letter = ord(letter)
        letter = letter + userNum
        newLetter = chr(letter)
        newMessage = newMessage + newLetter
