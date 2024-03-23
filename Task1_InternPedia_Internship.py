def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

def calculator():
    print("Welcome to Simple Calculator!")
    while True:
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        try:
            ch =int(input("Enter your choice(in numbers): "))
            if ch ==5:
                print("Goodbye!")
                break
            n1=float(input("Enter first number: "))
            n2=float(input("Enter second number: "))
            if ch ==1:
                print("Result: ", int(add(n1, n2)))
            elif ch ==2:
                print("Result: ", int(subtract(n1, n2)))
            elif ch ==3:
                print("Result: ", int(multiply(n1, n2)))
            elif ch==4:
                if n2 == 0:
                    print("Cannot divide by zero.")
                else:
                    print("Result: ", divide(n1, n2))
            else:
                print("Invalid input. Please enter a valid number (1/2/3/4/5).")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
        except Exception as e:
            print("An error occurred:", e)
calculator()