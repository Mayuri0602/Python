class Student:
    language="Python"    
    stipend="10k"

harry = Student()
harry.name = "Harry"
print(harry.name, harry.language, harry.stipend)

jasmine = Student()
jasmine.name = "Jasmine"
print(jasmine.name, jasmine.language, jasmine.stipend)


# language,stipend are class attributes whereas name is object(instance) atttribute

#instance attribute take preference over class attribute 