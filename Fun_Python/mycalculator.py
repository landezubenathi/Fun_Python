def add(x, y):
    return x + y
def subtract(x, y):
     return x-y
def multiply(x, y):
     return x*y
def divide(x, y):
    if y == 0:
          return "Error! Division by zero."
    return x/y

#Command line arguments
while True:
    print("\nSimple Calculator Select your Expression")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter choice (1-5): ")

    if choice == "5":
        print("Exiting... Goodbye!")
        break

    if choice in ("1","2","3","4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(f"Result: {add(num1, num2)}")
            if choice == "2":
                print(f"Result: {subtract(num1, num2)}")
            if choice == "3":
                print(f"Result: {multiply(num1, num2)}")
            if choice == "4":
                print(f"Result: {divide(num1, num2)}")

        except ValueError:
            print("Invalid Input! Please enter numbers only.")

    else:
        print("Invalid Choice! Please choose between 1-5.")
        continue
