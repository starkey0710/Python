shop = {
"strawberry": 3,
"banana": 2,
"peach": 5,
"mango": 6,
"kiwi": 4
}

pantry = {
"strawberry": 0,
"banana": 0,
"peach": 0,
"mango": 0,
"kiwi": 0,
"S1": 0,
"S2": 0,
"S3": 0,
"S4": 0
}

sb = {
"strawberry": 5,
"banana": 3
}

pm = {
"peach": 3,
"mango": 2
}

bk = {
"banana": 2,
"kiwi": 4
}

sk = {
"strawberry": 5,
"kiwi": 3
}

recipeBook = {
"S1": sb,
"S2": pm,
"S3": bk,
"S4": sk
}


money_total = {
"money": 100
}

while True:
    print(
    "~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(
    "Welcome to Yujing's Store!")
    print(
    "~~~~~~~~~~~~~~~~~~~~~~~~~~")
    actions = {
    "press v": "to view",
    "press b": "to buy",
    "press s": "to sell",
    "press q": "to quit",
    "press m": "to make a tasty smoothie"
    }
    for key, val in actions.items():
        print(key + ": " + str(val))


    action = input("What do you wanna do?")


    #BUY
    if action == "b":
        #start with $100
        money_origin = 100
        #print item and price
        for key, val in shop.items():
            s_str = "{:<20}{:<20}".format("Item:" + key, "Price:" + str(val))
            print(s_str)
        buy = input("What do you wanna buy?")
        quantity_b = input("How many do you want?")
        #update the current money
            #pantry[buy] = the amount of the item
            #shop[buy] = the price of the item
        pantry[buy] = pantry[buy] + int(quantity_b)
        totalSpent = shop[buy] * int(quantity_b)
        money_total["money"] = money_total["money"] - totalSpent
        for key, val in money_total.items():
            print(key + ": " + str(val))


    #VIEW
    if action == "v":
        view = {
        "money": money_total,
        "items": pantry,
        "menu": shop,
        "recipe": recipeBook
        }
        for key, val in view.items():
            print(key)
        vv = input("What do you wanna view?")
        for key, val in view[vv].items():
            v_str = "{:<20}{:<20}".format(key + " ",str(val),)
            print(v_str)


    #SELL
    if action == "s":
        for key, val in pantry.items():
            s_str = "{:<20}{:<20}".format("Item:" + key, "Amount:" + str(val))
            print(s_str)
        sell = input("What do you wanna sell?")
        quantity_s = input("How much do you wanna sell?")
        if pantry[sell] <= int(quantity_s):
            print("Oops. Insufficient ingredient.")
        else:
            #update the current money
                #pantry[sell] = the amount of the item
                #shop[sell] = the price of the item
            pantry[sell] = pantry[sell] - int(quantity_s)
            totalEarn = shop[sell] * int(quantity_s)
            money_total["money"] = money_total["money"] + totalEarn
            for key, val in money_total.items():
                print(key + ": " + str(val))


    #MAKE
    if action == "m":
        for key, val in recipeBook.items():
            m_str = "{:<8}{:<20}".format(key, str(val))
            print(m_str)
        make = input("What do you wanna make?")
        if make == "S1":
            if pantry["strawberry"]<= sb["strawberry"]:
                print("Oops. Insufficient ingredient.")
            else:
                #the amount of s in the pantry - the amount of s it takes to make S1
                pantry["strawberry"] = pantry["strawberry"] - sb["strawberry"]
                #the amount of b in the pantry - the amount of b it takes to make S1
                pantry["banana"] = pantry["banana"] - sb["banana"]
                #the amount of S1 increases by 1
                pantry["S1"] = pantry["S1"] + 1
                #print the pantry
                for key, val in pantry.items():
                    a_str = "{:<8}{:<20}".format(key, str(val))
                    print(a_str)
        elif make == "S2":
            if pantry["strawberry"]<= sb["strawberry"]:
                print("Oops. Insufficient ingredient.")
            else:
                pantry["peach"] = pantry["peach"] - pm["peach"]
                pantry["mango"] = pantry["mango"] - pm["mango"]
                pantry["S2"] = pantry["S2"] + 1
                for key, val in pantry.items():
                    b_str = "{:<8}{:<20}".format(key, str(val))
                    print(b_str)
        elif make == "S3":
            if pantry["strawberry"]<= sb["strawberry"]:
                print("Oops. Insufficient ingredient.")
            else:
                pantry["banana"] = pantry["banana"] - bk["banana"]
                pantry["kiwi"] = pantry["kiwi"] - bk["kiwi"]
                pantry["S3"] = pantry["S3"] + 1
                for key, val in pantry.items():
                    c_str = "{:<8}{:<20}".format(key, str(val))
                    print(c_str)
        elif make == "S4":
            if pantry["strawberry"]<= sb["strawberry"]:
                print("Oops. Insufficient ingredient.")
            else:
                pantry["strawberry"] = pantry["strawberry"] - sk["strawberry"]
                pantry["kiwi"] = pantry["kiwi"] - sk["kiwi"]
                pantry["S4"] = pantry["S4"] + 1
                for key, val in pantry.items():
                    d_str = "{:<8}{:<20}".format(key, str(val))
                    print(d_str)
        else:
            print("Error.")


    #QUIT
    if action == "q":
        print("See you next time!")
        break
