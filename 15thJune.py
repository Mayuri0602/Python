# Question 1
# i = 1
# while (i <= 10):
#     print(i)
#     i += 1

# Question 2
# i = 1
# while (i <= 20):
#     if(i % 2 == 0):
#         print(i) 
#     i += 3    

# Question 3
# n = int(input("Enter a number: "))
# i = 1
# sum = 0
# while (i <= n):
#     sum = sum + i
#     i = i + 1
# print(sum)   

# Question 4
# n = int(input("Enter a number: "))
# i = 1
# while( i <= 10):
#     print(n, "x", i, "=", n*i)
#     i = i + 1

# Question 5
# n = 1234
# rev = 0
# while(n > 0):
#     rev = (rev * 10) + (n % 10)
#     n = n//10
# print("Reversible of a number = ", rev)
    
# Question 6        
# n = 12345 
# count = 0
# while(n > 0):
#     n = n//10
#     count = count + 1
# print("Total digits in a number = ", count)    

# Question 7
# i = 1
# n = 6
# fact = 1
# while(i <= 6):
#     fact = fact * i
#     i += 1
# print("Factorial of 6 = ", fact)
    
#  Question 8
# n = 1432
# sum = 0
# while(n > 0):
#     digit = n % 10
#     sum = sum + digit
#     n=n//10
# print("Sum of digits of a number= ",sum)    

# Question 9
# s = input("Enter a string: ")
# count_vowel = 0
# index = 0
# while(index < len(s)):
#     if s[index].lower() in 'aeiou':
#         count_vowel += 1
#     index += 1
# print(count_vowel)       


# text = input("Enter a string: ")
# vowels = 'aeiouAEIOU'
# count = 0

# for char in text:
#     if char in vowels:
#         count += 1
# print("Number of vowels:", count)

# Question 10
text = input("Enter a string: ")
mid = len(text) // 2

if text[:mid] == text[mid:]:
    print("String is symmetrical")
else:
    print("String is not symmetrical")