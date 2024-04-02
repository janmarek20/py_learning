numbers = []
numbers_3 = []

for i in range(0, 101):
    if i % 5 == 0:
        numbers.append(i)

print(numbers)
print([num**3 for num in numbers])