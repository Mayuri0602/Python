i = 1234
odd = 0
even = 0
while(i>0):
    r=i%10
    if(i%2==0):
        even=even+r
    else:
        odd=odd+r
    i=i//10
print(even)
print(odd) 



#user defined program

i=int(input("Enter first number: "))
n=int(input("Enter last number: "))
while(i<=n):
    print(i)
    i=i+1


#sum of square of a given number

i=123
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)
    i=i//10
print(sum) 


# reversible of a number

i=345
rev = 0
while(i>0):
    rev = (rev*10) + (i%10)
    i = i//10
print(rev)  



# sum of cube of a number

i = 124
sum = 0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
print(sum)    
   
