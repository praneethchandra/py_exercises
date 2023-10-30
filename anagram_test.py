import anagram

def test_main_palindrome():
    anagram.first_string = "racecar"
    anagram.second_string = "racecar"
    assert anagram.main() == "Palindrome"

def test_main_not_palindrome():
    anagram.first_string = "racecar"
    anagram.second_string = "raceca"
    assert anagram.main() == "Not Palindrome"

def test_main_invalid_input():
    anagram.first_string = None
    anagram.second_string = None
    assert anagram.main() == "Invalid input"

def test_main_empty_input():
    anagram.first_string = ""
    anagram.second_string = ""
    assert anagram.main() == "Palindrome"

def test_main_one_empty_input():
    anagram.first_string = ""
    anagram.second_string = "racecar"
    assert anagram.main() == "Not Palindrome"

def test_main_one_empty_input():
    anagram.first_string = "racecar"
    anagram.second_string = ""
    assert anagram.main() == "Not Palindrome"

def test_main_one_char_input():
    anagram.first_string = "a"
    anagram.second_string = "a"
    assert anagram.main() == "Palindrome"

def test_main_one_char_input():
    anagram.first_string = "a"
    anagram.second_string = "b"
    assert anagram.main() == "Not Palindrome"

def test_main_one_char_input():
    anagram.first_string = "a"
    anagram.second_string = ""
    assert anagram.main() == "Not Palindrome"

def test_main_one_char_input():
    anagram.first_string = ""
    anagram.second_string = "a"
    assert anagram.main() == "Not Palindrome"

def test_main_one_char_input():
    anagram.first_string = None
    anagram.second_string = "a"
    assert anagram.main() == "Invalid input"