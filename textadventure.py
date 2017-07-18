while True:
    print("You are on an island in Hawaii. Waking up on the hammock, you find the your most valuable treasure--King Pineapple missing! So, you decided to go on a journey of looking for King Pineapple. Where should you go first?")
    print("a.Go underwater b.Go to forest")
    Q1 = input("Your Choice:")
    if Q1 == "a":
        print("You jump into the water and bump into a giant shark. What do you do?")
        print("a. fight him b.tell him jokes")
        Q2 = input("Your Choice:")
        if Q2 == "a":
            print("You win the fight. Now you keep swimming. You see a shipwreck. What do you do?")
            print("a. Go check it out b. Keep going")
            Q5 = input("Your Choice:")
            if Q5 == "a":
                print("YOU FOUND THE PINEAPPLE!!")
                print("CONGRATULATIONS")
            elif Q5 == "b":
                print("Another shark appears and swallows you.")
                print("GAME OVER")
            else:
                print("invalid option")
        elif Q2 == "b":
            print("The shark thinks your jokes are boring and swallows you.")
            print("GAME OVER")
        else:
            print("invalid option")
    elif Q1 == "b":
        print("A monkey comes to you and says that he is able to guide you. What do you do?")
        print("a. Follow him b. No, thanks")
        Q3 = input("Your Choice:")
        if Q3 == "a":
            print("The monkey leads you to a cave. It's really dark. Would you go inside?")
            print("a. Yes b. Nope")
            Q4 = input("Your Choice:")
            if Q4 == "a":
                print("YOU FOUND THE PINEAPPLE!!")
                print("CONGRATULATIONS")
            elif Q4 == "b":
                print("You decide to go somewhere else but accidentally fall off a cliff.")
                print("GAME OVER")
            else:
                print("invalid option")
        elif Q3 == "b":
            print("While you are exploring your own way, you bump into a tree. You die.")
            print("GAME OVER")
        else:
            print("invalid option")
    option = input("Do you want to play again?")
    if option == "No":
        break
