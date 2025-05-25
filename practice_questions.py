# Q1 Write a program that takes an integer input from the user and checks whether the number is odd or even.


i=int(input("Enter an integer: "))
if(i%2==0):
    print("Even number")
elif(i%2!=0):
    print("Odd number")
else:
    print("Error")


# Q2 Write a program that takes three numbers as input and prints the largest of the three.
            

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))           
c=int(input("Enter third number: "))

if(a>b and a>c):
    print("The largest of the three numbers is a")
elif(b>a and b>c):
    print("The largest of the three numbers is b")
else:
    print("The largest of the three numbers is c") 


# Q3 Write a program to check if a given year is a leap year. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.


y=int(input("Enter a year: "))
if(y%4==0 and y%100!=0) or (y%400==0):
    print("Entered year is a leap year")
else:
    print("Entered year is not a leap year")

# Q4 Write a program that takes a percentage (integer) as input and prints the corresponding grade based on the following criteria:
# >= 90: Grade A
# >= 80: Grade B
# >= 70: Grade C
# >= 60: Grade D
# < 60: Grade F 
   

p=int(input("Enter your percentage: "))
if(p>=90):
    print("Grade A")
elif(p>=80 and p<90):
    print("Grade B")
elif(p>=70 and p<80):
    print("Grade C")
elif(p>=60 and p<70):
    print("Grade D")
elif(p<60):
    print("Grade F")
else:
    print("Input valid percentage")


# Q5 Write a program that checks if a given letter is a vowel (a, e, i, o, u) or a consonant.


l=input("Enter a letter: ")
if(l=='a' or l=='e' or l=='i' or l=='o' or l=='u' or l=='A' or l=='E' or l=="I" or l=='O' or l=='U'):
    print("Entered letter is a vowel")
else:
    print("Entered letter is a consonant")

# Q6 Write a basic calculator program that takes two numbers and an operator (+,-, *, /) as input and performs the specified operation. Print the result based on the operation.

x = float(input("Enter first number: "))
o = input("Enter an operator(+,-,*,/): ")
y = float(input("Enter second number: "))

if(o=='+'):
    result=x+y
elif(o=='-'):
    result=x-y
elif(o=='*'):
    result=x*y
elif(o=='/'):
    if (y%2 !=0):
        result=x/y
    else:
        result= "Error, division by zero"
else:
    result= "Invalid operator"

print("Result: ",result)


# Q7 Write a program that takes a number as input and checks whether it is positive, negative, or zero.


n=int(input("Enter any number: "))
if(n>0):
    print("Number is positive")
elif(n<0):
    print("Number is negative")
elif(n==0):
    print("Number is zero")
else:
    print("Error")   


# Q8 Write a program that checks if a username and password entered by the user match the pre-set values username = "admin" and password = "1234". If both match, print "Login Successful", otherwise print "Login Failed"


username = "admin"
password = "1234"

u = input("Enter username: ")
p = input("Enter password: ")

if u == username and p == password:
    print("Login Successful")
else:
    print("Login Failed")


# Q9 Write a program that takes three sides of a triangle as input and checks if those sides form a valid triangle. A triangle is valid if the sum of any two sides is greater than the third side. Check conditions like a + b > c, b + c > a, and a + c > b.

a = float(input("Enter first side of a triangle: "))
b = float(input("Enter second side of a triangle: "))
c = float(input("Enter third side of a triangle: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle is valid")
else:
    print("Not a valid triangle") 
   

# Q10 Write a program that calculates the Body Mass Index (BMI) based on user input for weight (in kilograms) and height (in meters). Then categorize the BMI into:
#  Underweight (BMI < 18.5)
#  Normal weight (18.5 <= BMI < 24.9)
#  Overweight (25 <= BMI < 29.9)
#  Obesity (BMI >= 30)
#  Use the formula: BMI = weight / (height ** 2)


w = float(input("Enter the weight: "))
h = float(input("Enter the height: "))

BMI =  w/h**2
print("BMI = ",BMI)

if(BMI < 18.5):
    result="Underweight"
elif(18.5 <= BMI < 24.9):
    result="Normal weight"
elif(25 <= BMI <29.9):
    result="Overweight"
elif(BMI >= 30):
    result="Obesity"
else:
    result="Error"

print(result)


# Q11 Write a program that calculates the discount for a product based on its price:
#  If price is greater than 1000, discount is 10%
#  If price is between 500 and 1000, discount is 5%
#  Otherwise, no discount
#  Print the final price after applying the discount


price = float(input("Enter the price of the product: "))

if (price > 1000):
    discount = 0.10  # 10%
elif (500 <= price <= 1000):
    discount = 0.05  # 5%
else:
    discount = 0.0   # No discount

discount_amount = price * discount
final_price = price - discount_amount

print("Discount: ₹{:.2f}".format(discount_amount))
print("Final price after discount: ₹{:.2f}".format(final_price))


# Q12 Write a program that takes the name of a month as input and prints the number of days in that month. Consider leap years for February.

month = input("Enter the name of the month: ")
year = int(input("Enter the year: "))

if month == "January":
    print("January has 31 days.")
elif month == "February":
    # Check if it's a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("February has 29 days.")
    else:
        print("February has 28 days.")
elif month == "March":
    print("March has 31 days.")
elif month == "April":
    print("April has 30 days.")
elif month == "May":
    print("May has 31 days.")
elif month == "June":
    print("June has 30 days.")
elif month == "July":
    print("July has 31 days.")
elif month == "August":
    print("August has 31 days.")
elif month == "September":
    print("September has 30 days.")
elif month == "October":
    print("October has 31 days.")
elif month == "November":
    print("November has 30 days.")
elif month == "December":
    print("December has 31 days.")
else:
    print("Invalid month name.")


# Q13 Write a program that simulates a simple ATM. The user should be able to:
#  Check balance
#  Deposit money
#  Withdraw money (ensure the balance doesn't go negative) Use an if-else structure to handle the user's choices.

balance = 5000.0

print("Welcome to the ATM!")
print("Select an option:")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    print(f"Your current balance is: ${balance:.2f}")

elif choice == "2":
    deposit = float(input("Enter amount to deposit: "))
    if deposit > 0:
        balance += deposit
        print(f"Deposit successful! New balance: ${balance:.2f}")
    else:
        print("Invalid deposit amount.")

elif choice == "3":
    withdraw = float(input("Enter amount to withdraw: "))
    if withdraw > 0:
        if withdraw <= balance:
            balance -= withdraw
            print(f"Withdrawal successful! New balance: ${balance:.2f}")
        else:
            print("Insufficient balance!")
    else:
        print("Invalid withdrawal amount.")

else:
    print("Invalid choice. Please select 1, 2, or 3.")


# Q14 Write a program that categorizes a given age into different groups:
#  Infant (0-1 year)
#  Toddler (2-4 years)
#  Child (5-12 years)
#  Teenager (13-19 years)
#  Adult (20-59 years)
#  Senior (60 years and above)


age = int(input("Enter the age: "))

if age >= 0 and age <= 1:
    print("Category: Infant")
elif age >= 2 and age <= 4:
    print("Category: Toddler")
elif age >= 5 and age <= 12:
    print("Category: Child")
elif age >= 13 and age <= 19:
    print("Category: Teenager")
elif age >= 20 and age <= 59:
    print("Category: Adult")
elif age >= 60:
    print("Category: Senior")
else:
    print("Invalid age entered.")


#Q15 Write a program that takes an integer (1-7) as input and prints the corresponding day of the week (1
#  for Monday, 2 for Tuesday, etc.)

day_number = int(input("Enter an integer (1-7): "))

if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid input! Please enter a number between 1 and 7.")
