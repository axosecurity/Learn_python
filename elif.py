

#test lab for learing elif

print("we have = 1 2 3")

need = input("What you need sir\n:")

#print("you order number is " + need )

if int(need) == 1:
    print("you order number is " + need)
    price = 10
    print("your order price is " + str(price) )
    print("more we have a b c ")
    mor = input("enter what you need\n")
    if mor == "a":
        valu = 6
        tt = price + valu
        print("total price is " + str(tt)  )
    elif mor == "b":
        valu2 = 3
        tt2 = price + valu2
        print("total price is " + str(tt2))
    elif mor == "c":
        valu3 = 8
        tt3 = price + valu3
        print("total price is " + str(tt3))

    elif int(need) == 2:
         print("you order number is " + str(need))

         price1 = 20
         print("your order price is " + str(price1)  )
elif int(need) == 3:
    print("you order number is " + str(need))

    price3 = 30
    print("your order price is " + str(price3)  )
else:
    print("we dont have that item so \nFUCK OFF !!!!!")







