# Question 1: Print no.s. from 1 to 10
i = 1
while (i <= 10):
    print(i)
    i += 1

# Question 2: Print even no. from 1 to 20 with a step value of 3
i = 1
while (i <= 20):
    if(i % 2 == 0):
        print(i) 
    i += 3    

# Question 3: Sum of number
n = int(input("Enter a number: "))
i = 1
sum = 0
while (i <= n):
    sum = sum + i
    i = i + 1
print(sum)   

# Question 4: Multiplication table
n = int(input("Enter a number: "))
i = 1
while( i <= 10):
    print(n, "x", i, "=", n*i)
    i = i + 1

# Question 5: Reversible of a number
n = 1234
rev = 0
while(n > 0):
    rev = (rev * 10) + (n % 10)
    n = n//10
print("Reversible of a number = ", rev)
    
# Question 6: Count number of digits in a number.       
n = 12345 
count = 0
while(n > 0):
    n = n//10
    count = count + 1
print("Total digits in a number = ", count)    

# Question 7: Find out factorial of a number.
i = 1
n = 6
fact = 1
while(i <= 6):
    fact = fact * i
    i += 1
print("Factorial of 6 = ", fact)
    
#  Question 8: Input: number   Output: sum of digits of a number
n = 1432
sum = 0
while(n > 0):
    digit = n % 10
    sum = sum + digit
    n=n//10
print("Sum of digits of a number= ",sum)    

# Question 9: Write a program to count the total number of vowels from a string of numbers:
# input: abcdef , output => 2
# input: 43213 , output => 0
s = input("Enter a string: ")
count_vowel = 0
index = 0
while(index < len(s)):
    if s[index].lower() in 'aeiou':
        count_vowel += 1
    index += 1
print(count_vowel)       

            # or 

text = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = 0

for char in text:
    if char in vowels:
        count += 1
print("Number of vowels:", count)

# Question 10:  Write a python program to check whether the given string is symmetrical or not
# Example: A string is said to be symmetrical if both the halves of the string are the same
# Input: khokho , Output => String is symmetrical ( Example : kho (first half) is same as kho ( last half)
# Input: regex Output: String is not symmetrical
text = input("Enter a string: ")
mid = len(text) // 2
if text[:mid] == text[mid:]:
    print("String is symmetrical")
else:
    print("String is not symmetrical")