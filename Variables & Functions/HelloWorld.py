#Ask the user name (removing white space on the left and correcting the first letter to capital)
name = input("What's your name? ").strip().capitalize()

#Split First and Second name
first, last = name.split(" ")

#print the user first name
print("Hello,"  + first)

#Ask and print the age
age = input("\nHow old you? ")
print("You are", age ,"years old!")

print("Thanks, bye!")