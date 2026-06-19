numbers = (1, 2, 3, 2, 4, 2, 5, 1, 3)

print("Tuple:", numbers)

print()

for n in set(numbers):
    print(n, "occurs", numbers.count(n), "times")

print()

max_count = 0
most_common = None

for n in numbers:
    if numbers.count(n) > max_count:
        max_count = numbers.count(n)
        most_common = n

print("Most common element:", most_common)