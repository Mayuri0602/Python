y=int(input("Enter a year:"))
if(y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("Entered year is a leap year")
else:
    print("It's not a leap year")    