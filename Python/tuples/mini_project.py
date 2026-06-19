students = (
    ("shraddha", 85),
    ("devansh", 92),
    ("mehwish", 78),
    ("meghraj", 95)
)

print("Student Records:\n")

for s in students:
    print("Name:", s[0], "| Marks:", s[1])

print()

top = students[0]

for s in students:
    if s[1] > top[1]:
        top = s

print("Top Scorer:")
print("Name:", top[0])
print("Marks:", top[1])

print()

total = 0
for s in students:
    total += s[1]

print("Average Marks:", total / len(students))