def print_last_digit(n):
    
    last_digit = abs(n) % 10
    print(last_digit)
# abs(n) ensures that even if the number is negative, we get a positive value for the last digit.

n = int(input("Enter a number : " ))  
print_last_digit(n)
