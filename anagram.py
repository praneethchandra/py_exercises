import cProfile

first_string = input("Enter first string: ")
second_string = input("Enter second string: ")

def main():
    not_palindrome = False

    if first_string is None or second_string is None:
        print("Invalid input")

    if len(first_string) != len(second_string):
        not_palindrome = True
    else:
        for i in range(len(first_string)):
            if first_string[i] != second_string[i]:
                not_palindrome = True
                break

    if not_palindrome:
        print("Not Palindrome")
    else:
        print("Palindrome")

if __name__ == "__main__":
    cProfile.run('main()')