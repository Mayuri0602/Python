# 1. Find Maximum Element (Without max())

numbers = [10, 20, 4, 45, 99]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print("The maximum element is:", max_num)
print(len(numbers))

# 2. Sum All Elements in a List

numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total += num
print("The sum of all elements is:", total)


# 3. Reverse List Without reverse() or Slicing

numbers = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])
print("Reversed list:", reversed_list)


# 4. Sort List in Ascending Order Without sort()
numbers = [5, 2, 8, 1, 3]
# Using simple bubble sort
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
print("Sorted list in ascending order:", numbers)


# 5. Remove Duplicates While Maintaining Order

numbers = [1, 2, 2, 3, 4, 4, 5]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("List after removing duplicates:", unique)


# 6. Find All Pairs With a Given Sum

numbers = [1, 2, 3, 4, 3, 5, 6]
target_sum = 6
pairs = []
visited = set()
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target_sum:
            pair = (numbers[i], numbers[j])
            if pair not in pairs and (numbers[j], numbers[i]) not in pairs:
                pairs.append(pair)
print("Pairs that add up to", target_sum, ":", pairs)


# 7. Flatten a Nested List

nested_list = [1, [2, 3], [4, [5, 6], 7], 8]
flattened = []

def flatten(lst):
    for item in lst:
        if isinstance(item, list):
            flatten(item)
        else:
            flattened.append(item)

flatten(nested_list)
print("Flattened list:", flattened)


# 8. Sum Excluding Largest and Smallest (No max() or min()):

numbers = [1, 2, 3, 4, 5]

# Find max and min manually
max_num = numbers[0]
min_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

# Compute total sum
total = 0
for num in numbers:
    total += num

# Subtract max and min
sum_excluding = total - max_num - min_num
print("Sum excluding the largest and smallest element:", sum_excluding)