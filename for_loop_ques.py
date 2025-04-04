# ques.1

total_price = 0
for i in range(5):
    price = float(input(f"Enter price of item {i + 1}: "))
    total_price += price
if total_price > 100:
    total_price *= 0.9   
print(f"Total bill after discount (if applicable): ${total_price: .2f}")   


# ques.2

