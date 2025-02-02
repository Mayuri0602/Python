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