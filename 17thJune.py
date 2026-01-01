# Question 1. Write a program to check whether any number is Armstrong number or not
# Note:Armstrong Number is a number that is the sum of its own digits each raised to the power of the number of digits
# Input : 153 Output : Narcissistic Number Explanation: 1^3+5^3+3^3=153
# Input : 1634 Output : Narcissistic Number Explanation: 1^4+6^4+3^4+4^4=1634
n = int(input("Enter  a number: "))
temp = n
sum = 0
while(n > 0):
    sum = sum + (n%10) * (n%10) * (n%10)
    n = n//10
if(temp == sum):
    print("Armstrong number")
else:
    print("Not an armstrong number") 

# Question 2. Write a Python program to print hash pattern
#
##
###
####
###
##
#
for i in range(1,5):
    print('#' * i)
    i += 1

for i in range(3,0,-1):
    print('#' * i) 
    i -= 1   

# Question 3. Write a Python program to print hollow right angle triangle
# 1
# 23
# 4 5
# 6 7
# 89101112
rows=5
num=1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            print(num, end='')
        else:
            print(' ', end='')
        num += 1
    print()

# Question 4. Write a Python program to print duplicates from a list of integers
# Input: [ 40, 50, -20, 60, 60, -20, -20]
# Output : [60,-20]
nums = [ 40, 50, -20, 60, 60, -20, -20]
duplicates = []
for num in nums:
    