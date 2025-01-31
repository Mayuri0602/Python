str=["arjun",34,"jaipur",2000]
print(str[3])
str[0]="karan"       #lists are mutable in python
print(str)

str.append("priya")   #adds one element at the end in the list
print(str)

list=[56,90,23,11,45]
list.sort()          #sort arranges list in an ascending order
print(list)

list.sort(reverse=True)    #arranges list in a descending order
print(list)

list.reverse()
print(list)

list.insert(5,67)
print(list)

list.pop(3)
print(list)