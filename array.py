# array = [5, 4, 5, 2, 1, 9]
# print(array[:3])
# print(array[1:])
# print(array[1:3])
# print(array[:])

# array = [2, 2.0, "sabbir", 9.56 ]
# array[2] = "hossain"
# print(array[:])

# Linear Search O(N)
array = [25, 66, 55, 21, 5, 120, 3]
print(array)

max = array[0]
min = array[0]

for num in array:
    if num > max:
        max = num

    if num < min:
        min = num

print(max)
print(min)