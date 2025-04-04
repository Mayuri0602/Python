set={23,45,78,90,"khush","prateek"}     #collection of unordered items

print(set)
print(type(set))

set.add("swastik")
print(set)
set.remove(78)
print(set)
set.clear()
print(set)


set1={67,56,32,"maths","physics",2002}
set2={"maths",45,32,89}

print(set1.union(set2))
print(set1.intersection(set2))
  
      