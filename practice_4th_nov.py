# Reverse a string in Python without using built-in functions

str = "DataEngineering"
rev_str = ""

for char in str:
    rev_str = char + rev_str

print("Reversed string : ",rev_str)


# Find duplicate elements in a list
numbers = [4, 2, 7, 4, 9, 2, 3, 7, 8]
duplicates = []
seen = set()

for num in numbers:
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)
print("Duplicate elements:", duplicates)


# Count word frequencies in a text file
word_count = {}
with open("data.txt", "r") as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

print("Word frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")

# Merge two dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Method 1: Using unpacking
merged_dict = {**dict1, **dict2}

# Method 2: Using update()
# dict1.update(dict2)
# merged_dict = dict1

print("Merged dictionary:", merged_dict)


# Remove stopwords from a given list of words

words = ["this", "is", "a", "sample", "sentence", "for", "data", "processing"]
stopwords = {"is", "a", "for", "this"}

filtered_words = [word for word in words if word not in stopwords]

print("Filtered words:", filtered_words)
