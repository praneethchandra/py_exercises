first_string = input("Enter first string: ")
second_string = input("Enter second string: ")

not_palindrome = False

if len(first_string) != len(second_string):
    print("Not Palindrome")

for i in range(len(first_string)):
    if first_string[i] != second_string[i]:
        not_palindrome = True

if not_palindrome:
    print("Not Palindrome")
else:
    print("Palindrome")