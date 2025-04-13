#reversible of a number & pallindrome number


i=int(input("Enter a number: "))
orig=i
rev=0
while(i>0):
    rev=(rev*10)+(i%10)
    i=i//10
print("reversible no.=",rev)    
if(orig==rev):
    print("pallindrome no.")
else:
    print("not a pallindrome no.")        