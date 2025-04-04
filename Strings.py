#basic operations
str1="Myself"
str2=" Ananya"

str3="I am a coder"
str4="you are beautiful"

print(str1+str2)    
print(len(str1))
print(len(str2))   #7 because of initial space
print(str1[2:8])   #slicing:accessing parts of a string (ending index is not included)

#string functions
print(str3.endswith("er"))
print(str4.capitalize())
print(str4.replace("beautiful","gorgeous"))
print(str4.count("a"))