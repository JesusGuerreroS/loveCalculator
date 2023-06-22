#####################################################
#Funny script of calculate your match with someone
#####################################################

print("Welcome to the Love Calculator!")
#get names of both persons
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#count how many times the letters in name matches with true love
t = name1.lower().count("t") + name2.lower().count("t")
r = name1.lower().count("r") + name2.lower().count("r")
u = name1.lower().count("u") + name2.lower().count("u")
e = name1.lower().count("e") + name2.lower().count("e")

l = name1.lower().count("l") + name2.lower().count("l")
o = name1.lower().count("o") + name2.lower().count("o")
v = name1.lower().count("v") + name2.lower().count("v")
e = name1.lower().count("e") + name2.lower().count("e")

#adding everything
total = str(t + r + u + e) + str(l + o + v + e)

#check the true love with your possible partner
if ( int(total) <= 10 or int(total) >= 90 ):
    print(f"Your score is {total}, you go together like coke and mentos.")

elif ( int(total) >= 40 and int(total) <= 50 ):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
