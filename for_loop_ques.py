# ques.1

total_price = 0
for i in range(5):
    price = float(input(f"Enter price of item {i + 1}: "))
    total_price += price
if total_price > 100:
    total_price *= 0.9   
print(f"Total bill after discount (if applicable): ${total_price: .2f}")   


# ques.2

# count no. of vowels in a given string using for loop

text = "hello world"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
print("Number of vowels: ", count)


# multiplication table

num = 6
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")


# sum of first 10 natural numbers

total = 0
for i in range(1,11):
    total = total + i
print("Sum: ",total)    



# factorial of a number


num = 6
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(f"Factorial of {num} is {fact}")   


# check pallindromic word

words = ["madam", "sir", "racecar", "java", "level"]
pallindrome_check = [] 
for word in words:
    if word == word[ ::-1]:
        pallindrome_check.append(True)
    else:
        pallindrome_check.append(False)
print("Pallindrome Check: ",pallindrome_check) 


# filtering out odd numbers

numbers = [10,25,36,47,52,63,78,99]
even_numbers = []
odd_numbers = []
for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print("Even numbers: ", even_numbers)
print("Odd numbers: ", odd_numbers)


# categorize product based on prices

prices = [1200,800,450,300,950,2000]
categories = []
for price in prices:
    if price > 1000:
        categories.append("Expensive")
    elif (500 <= price <= 1000):
        categories.append("Moderate")
    else: 
        categories.append("Cheap")
print("Price Categories: ", categories)                

