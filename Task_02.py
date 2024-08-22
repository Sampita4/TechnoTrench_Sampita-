
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."


def calculator():
    print("Simple Calculator")
    
    try:
        # for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # choose an operation
        print("Choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        # Perform the operation
        if choice == "1":
            result = add(num1, num2)
            print(f"The result of adding {num1} and {num2} is {result}.")
        elif choice == "2":
            result = subtract(num1, num2)
            print(f"The result of subtracting {num2} from {num1} is {result}.")
        elif choice == "3":
            result = multiply(num1, num2)
            print(f"The result of multiplying {num1} and {num2} is {result}.")
        elif choice == "4":
            result = divide(num1, num2)
            print(f"The result of dividing {num1} by {num2} is {result}.")
        else:
            print("Invalid choice! Please select a valid operation.")
    
    except ValueError:
        print("Error! Please enter valid numeric values.")

if __name__ == "__main__":
    calculator()
