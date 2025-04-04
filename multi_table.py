def multipli_table(N):
    
    table = [N * i for i in range(1, 11)]
    return table

N = int(input("Enter the number: ")) 
table = multipli_table(N)
print(table)  
