#Ask the First Number
x = int(input("Input the First number: "))

#Ask the Second Number
y = int(input("Input the Second number: "))

#Print the result
print("\n\nThe result is: ",x+y)

#Print the result with .000
z = x + y
print('\nNumeber with .000:', f"{z:,}")


#Float

#Ask the First Number
a = float(input("\nInput the First Float number: "))

#Ask the Second Number
b = float(input("\nInpute the Second Float number: "))

#Print the result
c = (a+b)

#Print the result with 2 decimal places
print('\nThe result is: ', f"{c:.2f}")

#Print the round result
d = round(c)
print('\nThe round of the result is: ',round(d))