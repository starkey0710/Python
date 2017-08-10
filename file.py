f = open ("open.txt", "w")
f.write("I'm\n")
f.write("Yujing")
f.close()

f = open("open.txt", "r")
for line in f:
    print(line.rstrip("\n"))
f.close
