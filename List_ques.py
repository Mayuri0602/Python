# Identifying passengers eligible for discount-(senior citizens,age>=60 are eligible for discounts)

ages = [25,30,76,56,60,22,68]
discount = [ ]

for age in ages:
    if age>=60:
        discount.append(True)
    else:
        discount.append(False)
print("Discount eligibility: ",discount)  


# Given monthly sales of 6 employees in a list. Determine which employees achieved sales about 5000 units.

sales = [4500,6000,3000,8000,5500,4200]
high_performers = [ ]

for i in range (len(sales)):
    if sales[i] > 5000:
        high_performers.append(f"Employee {i + 1}")
print(high_performers) 


# Find the most expensive product out of several products in a list.

Products = ["Laptop","Mobile","Headphone","Monitor"]
Prices = [80000,33000,5000,9000]

max_price = max(Prices)
index = Prices.index(max_price)
print(f"{Products[index]} :- ${max_price}")


# A warehouse stores product and their stock levels are listed. Identify products with a stock below 5 units. Identify products with a value less than 5.

products = ["Shirts","Jeans","Jackets","Shoes","Hats"]
stock = [3,10,4,15,21]

low_stock = []
for i in range (len(stock)):
    if stock[i] < 5:
        low_stock.append(products[i])
print(f"low stock products : {low_stock}")
