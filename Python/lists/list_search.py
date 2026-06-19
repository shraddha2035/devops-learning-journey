fruits = ["Apple", "Banana", "Mango", "Orange"]

item = input("Enter fruit to search: ")

if item in fruits:
    print(item, "found in list")
else:
    print(item, "not found")