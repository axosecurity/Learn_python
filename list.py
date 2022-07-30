
# IN this lab i will use python list
# AWSOME!!!!!,is"t it ?

h1 = "how to hack linux video"

h2 = "how to hack windows"

h3 = "how to hack android"

o1 = "a = Vide\nb = e-book\nc = blog\n"

print("What you need ?\n0 = " + h1 + "\n1 = " + h2 + "\n2 = " + h3 + "\n3 = Exit" )


list = [ h1 , h2 , h3 ]


need = int(input("Inpute the number of order\n "))

if int(need) == 1 or int(need) == 2:

    print("you ordered " + str(list[need]))
    print("we have\n" + o1 )

    nk = input("inpute the number of option\n")

    if nk == "a" and int(need) == 1:

        print("ink of video " + h1 )

    elif nk == "b" and int(need) == 1:

        print("lik of e-book" + h1)

    elif nk == "c" and int(need) == 1:

        print("link of blog" + h1)

    if nk == "a" and int(need) == 2:

        print("your link of video " + h2 )

    elif nk == "b" and int(need) == 2:

        print("lik of e-book" + h2 )

    elif nk == "c" and int(need) == 2:

        print("link of blog" + h2 )

elif int(need) >= 3:
    print("Sorry i dont know what you are saying\npress enter for exit ")

    input()














