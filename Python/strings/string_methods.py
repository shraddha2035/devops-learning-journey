# string_methods.py

text = input("Enter a sentence: ")

print("Original:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Capitalize:", text.capitalize())

print("Replace spaces:", text.replace(" ", "_"))

print("Length:", len(text))

print("Starts with 'H':", text.startswith("H"))
print("Ends with '.':", text.endswith("."))

print("Word count:", len(text.split()))