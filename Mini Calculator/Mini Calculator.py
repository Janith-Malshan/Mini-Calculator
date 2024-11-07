#Mini Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("float division by zero")
        print(f"{a} / {b} = None")
        return None
    return a / b

def power(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("float division by zero")
        print(f"{a} % {b} = None")
        return None
    return a % b

# select_op function to handle operations
def select_op(choice):
    if choice == '#':  # Terminate the program
        return -1
    elif choice == '$':  # Reset (just return to main menu, no action needed here)
        return 0
    elif choice in ['+', '-', '*', '/', '^', '%']:  # Arithmetic operations
        try:
            # Input the first number
            num1 = input("Enter first number: ")
            print(num1)
            if num1.endswith('$'):  # Reset input handling
                return 0
                
            num1 = float(num1)

            # Input the second number
            num2 = input("Enter second number: ")
            print(num2)
            if num2.endswith('$'):  # Reset input handling
                return 0
                
            num2 = float(num2)

            # Perform the corresponding operation
            if choice == '+':
                result = add(num1, num2)
            elif choice == '-':
                result = subtract(num1, num2)
            elif choice == '*':
                result = multiply(num1, num2)
            elif choice == '/':
                result = divide(num1, num2)
            elif choice == '^':
                result = power(num1, num2)
            elif choice == '%':
                result = remainder(num1, num2)

            # Display the result
            if result is not None:
                print(f"{num1} {choice} {num2} = {result}")
        except ValueError:  # Handle invalid input
            print("Done. Terminating")
            exit()
        return 0
    else:
        print("Unrecognized operation")
        return 0


# Main loop to interact with the user
while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
 
  # Take input from the user
    choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
    print(choice)
    
    if select_op(choice) == -1:  # If the user chooses to terminate
        print("Done. Terminating")
        exit()  # Exit the program