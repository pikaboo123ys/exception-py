try:
    number = int(input("enter a number"))
    print("the number entered is", number)

except ValuveError as ex:
    print("exception:", ex)
print("hello")