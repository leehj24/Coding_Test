n = int(input())
array = []

for _ in range(n):
    # Read a single line of input with age and name
    age, name = input().split()
    age = int(age)  # Convert age to integer
    array.append((age, name))  # Append as a tuple to the list

sorted_array = sorted(array, key=lambda x: x[0])

for age,name in sorted_array:
    print(age,name)

