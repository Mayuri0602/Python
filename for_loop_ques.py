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
print(f"Number of vowels: ",count)  

# ques.3

