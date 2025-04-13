n=5
for i in range(1,n+1):
    print('*' * i) 

for i in range(1,n+1):      #outer loop for rows
    for j in range (i):     #inner loop for printing stars
        print('*', end='')    #print star without new line
    print()                    #move to the next line after inner loop


y=5
for i in range(1,y+1):
    if i==1 or i==y:
        print('*' * i)     #first or last row
    else:
        print('*' + ' ' * (i-2) + '*')   #middle rows with spaces

x=5
for i in range(1,x+1):     #outer loop for rows
    for j in range(i):      #inner loop for printing patterns
        if j==0 or j==i-1 or i==1 or i==x:
            print('*', end='')        #print '*' at first, last position, and first/last
        else:                             
            print(' ',end='')          #print space for middle part
    print()                           #move to the next line after inner loop



a=5
for i in range(1,a+1):
    print(' ' * (n-i) + '*' * (2*i-1))    

b=6
for i in range(1,b+1):          #outer loop for rows
    for j in range(b-i):        #inner loop for spaces
        print(' ',end='')       #print space

    for k in range(2*i-1):      #inner loop for stars
        print('*',end='')       #print star

    print()                         #move to the next line after inner loop

#inverted pyramid pattern

c=5
for i in range(c,0,-1):
    print(' ' * (c-i) + '*' * (2*i-1))    

    