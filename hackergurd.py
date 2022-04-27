#IN this projcet Axosolaman will make a robot called hackergurd
# SO lets get Started !!!!!!!

intoro = "Hi i am hackergurd the protector and selles man of Hackershop"
hackershop = "Hackershop its a shope where you will find service that needed for a hacker"
q1 = "Whats your name ? "
qred = "Thanks for Comeing"

menu = "1=Linux_Security\n2=Windows_Security\n3Linux_Security\n4=Network_Security\n5=Webapp_Security\n6=Facebook_Security"
q2 = "which service you Would like to have ?: "
confum = "Your order number is "
confum_ord = "Click any Button For Going into next step"
# CODE STARTS NOW

print("""
    _                   _                 
   / \   __  _____  ___| |__   ___  _ __  
  / _ \  \ \/ / _ \/ __| '_ \ / _ \| '_ \ 
 / ___ \  >  < (_) \__ \ | | | (_) | |_) |
/_/   \_\/_/\_\___/|___/_| |_|\___/| .__/ 
                                   |_|    
""")
print(hackershop)

print(input("Click any button for Starting\n="))

print(intoro)

name = input("Whats Your name ?\n=")

print(name + " Thanks for comeing ")

input("Would you like to see our Services?\ntype Y or N\n=")

print(menu)

print(q2 + name)
your_order = input("which Service would you like to have ?\n=")
print(confum + your_order )
input(confum_ord + "\n=")
