info= {                   
    "name" : "anuja",
    "age" : 22,
    "job" : "software engineer",
    "hobbies" : ("dancing","singing","reading books"),   #use tuples & lists to store more than one value in key
    "is_adult" : True,
}

print(info)
print(type(info))
print(info["job"])

#dict_methods

print(info.keys())
print(info.values())
print(info.items())

print(info.get("name"))
print(info.get("name2"))

info.update({"name":"vishu"})
print(info)


# From "apple", create a dictionary where keys are characters and values are how many times they occur.

s = "apple"
d = { }
for ch in s:
    if ch in d:
        d[ch] += 1
    else: 
        d[ch] = 1
print(d)            


# Merge two dictionaries, if key is common, add values.

d1 = {'a': 1, 'b' : 2}
d2 = {'b': 3, 'c' : 7}
result = { }
for k in d1:
    result[k] = d1[k]
for k in d2:
    if k in result:
        result[k] = result[k] + d2[k]
    else:
        result[k] = d2[k]
print(result)



# Get all keys that exist in both {'a' : 1, 'b' : 2, 'c' : 7} and {'d' : 5, 'c' : 6, 'b' : 9}

d1 = {'a' : 1, 'b' : 2, 'c' : 7}
d2 = {'d' : 5, 'c' : 6, 'b' : 9} 
common = [ ]
for k in d1:
    if k in d2:
        common.append(k)
print(common)        



# Inverse key - value pairs.

d = {'a':1,'b':2,'c':1}
inv = { }
for k in d:
    val = d[k]
    if val in inv:
        inv[val].append(k)
    else:
        inv[val] = [k]
print(inv)            
