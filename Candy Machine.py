x = int(input("How many candy do you want?"))
av = 5
i = 1
while i <= x:
    if i > av:
        print("Candy is out of Stock")
        break

    print("Candy")
    i = i+1