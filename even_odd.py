def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
n = int(input("Enter an integer: "))
result = check_even_odd(n)
print(f"The number {n} is {result}.")
