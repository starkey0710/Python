def xOr (a, b):
    if a == b:
        return 0
    else:
        return 1

def longXOr (string1, string2):
    a = ""
    for i in range (len(string1)):
        int1 = int(string1[i])
        int2 = int(string2[i])
        digit = xOr (int1, int2)
        a = a + str(digit)
    return a

'''print (longXOr ("100110", "010111"))'''

def btol (b):
    ascii = int(b, 2)
    return chr(ascii)

'''user = input("Choose binary to convert to a letter: ")
print (btol(user))'''

def ltob (l):
    a = ""
    ascii = ord(l)
    result = bin(ascii)
    result = result[2:]
    numof0 = 8-len(result)
    for number in range(numof0):
        a = a + "0"
    return a + result


'''user1 = input("Choose a letter to convert to binary: ")
print (ltob(user1))'''

def wtob (w):
    a = ""
    for i in range (len(w)):
        letter = str(w[i])
        completeword = ltob (letter)
        a = a + str(completeword)
    return a

'''user2 = input("Choose a word to convert to binary: ")
print (wtob (user2))'''

def btow (b):
    a = ""
    for index in range (0, len(b), 8):
        letter = b[index: index + 8]
        oneLetter = btol (letter)
        a = a + str(oneLetter)
    return a

'''user3 = input("Choose binary to convert to a word: ")
print (btow (user3))'''

def encrypt (message, key):
    mb = wtob (message)
    result = longXOr(mb, key)
    return result

def decrypt (ciphertext, key):
    result = longXOr(ciphertext, key)
    return btow (result)
    print(decrypt(ciphertext, k))

user = input("Do you want to encrypt or decrypt your message? ")
if user == "encrypt":
    user4 = input("Choose a message up to 10 characters to encrypt: ")
    if len(user4) > 10:
        print ("Error: message too long.")
    k = "10101010111111110011001100000000110011001010101011111111001100110000000011001100"
    ciphertext = encrypt(user4, k)
    print (ciphertext)
elif user == "decrypt":
    user2 = input("Choose binary up to 80 characters to decrypt: ")
    if len(user2) > 80:
        print ("Error: message too long.")
    ciphertext = user2
    k = "10101010111111110011001100000000110011001010101011111111001100110000000011001100"
    print (decrypt(ciphertext, k))
else:
    print ("Error.")
