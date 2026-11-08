valid = false
while not valid: 
    try:
        n = int(input("enter a number"))
        if n%2==0:
            print("bye")
            valid = true
    except ValuveError:
        print("invalid!")