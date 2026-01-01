age = 10
print("memory of age=>", id(age))
x = age
print("memory of x=>", id(x))
x = 20
print("new memory of x=>", id(x), id(age))

list1 = [10,20,30,40,3,2,70]
# for e in list1:
#     print(e)  
 # execute loop directly => iterable


for index in range(0,7):
    print(index, list1[index])



    