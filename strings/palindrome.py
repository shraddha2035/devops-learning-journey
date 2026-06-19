# palindrome.py

word = input("Enter a word: ")

reverse = word[::-1]

if word.lower() == reverse.lower():
    print("Palindrome")
else:
    print("Not a palindrome")