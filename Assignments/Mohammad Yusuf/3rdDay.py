
#name = input("Enter Latters: ")

#if name == "abc":
 #   print("First latter of Alphabets.")
#elif name == "xyz":
#    print("Last latter of Alphabets.")
#else:
#    print("Any other latter.")
#if name == "abc":
 #   print("other condation.")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter Operator: ")

if op == "+":
    print("Yusuf= "+str(num1 + num2))
elif op == "-":
    print("Najib= "+str(num1 - num2))
elif op == "*":
    print("Musbah= "+str(num1 * num2))
elif op == "/":
    print("obaid= "+str(num1 / num2))
else:
    print("Wrong operator!")

color = input("What's Your favorite color?")
if color == 'purple':
    print("excellent choice!")
elif color == 'teal':
    print("not bad!")
elif color == 'seafoam':
    print("mediocre")
elif color == 'pure darkness':
    print("I like how you think")
else:
    print("You Monster!")