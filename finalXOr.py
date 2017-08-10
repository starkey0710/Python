import sys


#python xOr.py -e in.txt key.txt out.txt
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

def btol (b):
    ascii = int(b, 2)
    return chr(ascii)

def ltob (l):
    a = ""
    ascii = ord(l)
    result = bin(ascii)
    result = result[2:]
    numof0 = 8-len(result)
    for number in range(numof0):
        a = a + "0"
    return a + result

def wtob (w):
    a = ""
    for i in range (len(w)):
        letter = str(w[i])
        completeword = ltob (letter)
        a = a + str(completeword)
    return a

def btow (b):
    a = ""
    for index in range (0, len(b), 8):
        letter = b[index: index + 8]
        oneLetter = btol (letter)
        a = a + str(oneLetter)
    return a

def encrypt (message, key):
    mb = wtob (message)
    result = longXOr(mb, key)
    return result

def decrypt (ciphertext, key):
    result = longXOr(ciphertext, key)
    return btow (result)
    print(decrypt(ciphertext, k))

readmessage = open ("in.txt", "r")
linemessage = readmessage.readline()
linemessage = linemessage.rstrip("\n")
readkey = open ("key.txt", "r")
linekey = readkey.readline()
linekey = linekey.rstrip("\n")

if sys.argv[1] == "-e":
    ciphertext = encrypt(linemessage, linekey)
    f = open ("out.txt", "w")
    f.write(ciphertext)
    f.close()
elif sys.argv[1] == "-d":
    f = open ("out.txt", "w")
    f.write(decrypt(linemessage, linekey))
    f.close()
else:
    print ("Error.")
