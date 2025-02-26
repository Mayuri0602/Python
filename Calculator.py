def perform_operation(a, b, operator):
    if operator == 1:
        print(a + b, end="")  
    elif operator == 2:
        print(a - b, end="")  
    elif operator == 3:
        print(a * b, end="")
    elif operator == 4:
        print(a / b, end="")      
    else:
        print("Invalid Input", end="")  

a = int(input("Enter first number: "))  
b = int(input("Enter second number: "))  
operator = int(input("Enter the operator: "))  

perform_operation(a, b, operator)
