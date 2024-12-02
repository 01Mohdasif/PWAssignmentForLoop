# 1. Write a program to reverse a string.
def reverse_string(s):
    return s[::-1]

string = "Hello, World!"
reversed_string = reverse_string(string)
print(f"Reversed string: {reversed_string}")
# Output: Reversed string: !dlroW ,olleH
print("\n")

# 2. Check if a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

string = "madam"
palindrome_check = is_palindrome(string)
print(f"Is the string '{string}' a palindrome? {palindrome_check}")
# Output: Is the string 'madam' a palindrome? True
print("\n")

# 3. Convert a string to uppercase.
def to_uppercase(s):
    return s.upper()

string = "hello"
uppercase_string = to_uppercase(string)
print(f"Uppercase string: {uppercase_string}")
# Output: Uppercase string: HELLO
print("\n")

# 4. Convert a string to lowercase.
def to_lowercase(s):
    return s.lower()

string = "HELLO"
lowercase_string = to_lowercase(string)
print(f"Lowercase string: {lowercase_string}")
# Output: Lowercase string: hello
print("\n")

# 5. Count the number of vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

string = "Hello, World!"
vowel_count = count_vowels(string)
print(f"Number of vowels in '{string}': {vowel_count}")
# Output: Number of vowels in 'Hello, World!': 3
print("\n")

# 6. Count the number of consonants in a string.
def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in s if char in consonants)

string = "Hello, World!"
consonant_count = count_consonants(string)
print(f"Number of consonants in '{string}': {consonant_count}")
# Output: Number of consonants in 'Hello, World!': 7
print("\n")

# 7. Remove all whitespaces from a string.
def remove_whitespaces(s):
    return s.replace(" ", "")

string = "Hello, World!"
string_without_spaces = remove_whitespaces(string)
print(f"String without whitespaces: {string_without_spaces}")
# Output: String without whitespaces: Hello,World!
print("\n")

# 8. Find the length of a string without using the `len()` function.
def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count

string = "Hello, World!"
string_length_value = string_length(string)
print(f"Length of the string '{string}': {string_length_value}")
# Output: Length of the string 'Hello, World!': 13
print("\n")

# 9. Check if a string contains a specific word.
def contains_word(s, word):
    return word in s

string = "Hello, World!"
word = "World"
contains_check = contains_word(string, word)
print(f"Does the string '{string}' contain the word '{word}'? {contains_check}")
# Output: Does the string 'Hello, World!' contain the word 'World'? True
print("\n")

# 10. Replace a word in a string with another word.
def replace_word(s, old_word, new_word):
    return s.replace(old_word, new_word)

string = "Hello, World!"
old_word = "World"
new_word = "Python"
replaced_string = replace_word(string, old_word, new_word)
print(f"String after replacing '{old_word}' with '{new_word}': {replaced_string}")
# Output: String after replacing 'World' with 'Python': Hello, Python!
print("\n")

# 11. Count the occurrences of a word in a string.
def count_word_occurrences(s, word):
    return s.split().count(word)

string = "Hello, hello, Hello!"
word = "Hello"
word_count = count_word_occurrences(string, word)
print(f"Occurrences of the word '{word}' in the string: {word_count}")
# Output: Occurrences of the word 'Hello' in the string: 2
print("\n")

# 12. Find the first occurrence of a word in a string.
def first_occurrence(s, word):
    return s.find(word)

string = "Hello, World!"
word = "World"
first_occurrence_index = first_occurrence(string, word)
print(f"First occurrence of '{word}' in the string: {first_occurrence_index}")
# Output: First occurrence of 'World' in the string: 7
print("\n")

# 13. Find the last occurrence of a word in a string.
def last_occurrence(s, word):
    return s.rfind(word)

string = "Hello, World! Hello again!"
word = "Hello"
last_occurrence_index = last_occurrence(string, word)
print(f"Last occurrence of '{word}' in the string: {last_occurrence_index}")
# Output: Last occurrence of 'Hello' in the string: 14
print("\n")

# 14. Split a string into a list of words.
def split_string(s):
    return s.split()

string = "Hello, World!"
split_words = split_string(string)
print(f"List of words in the string: {split_words}")
# Output: List of words in the string: ['Hello,', 'World!']
print("\n")

# 15. Join a list of words into a string.
def join_words(word_list):
    return " ".join(word_list)

words = ["Hello", "World"]
joined_string = join_words(words)
print(f"Joined string: {joined_string}")
# Output: Joined string: Hello World

# 16. Convert a string where words are separated by spaces to one where words are separated by underscores.
def convert_to_underscore(s):
    return s.replace(" ", "_")

string = "Hello World Python"
underscore_string = convert_to_underscore(string)
print(f"String with underscores: {underscore_string}")
# Output: String with underscores: Hello_World_Python
print("\n")

# 17. Check if a string starts with a specific word or phrase.
def starts_with(s, phrase):
    return s.startswith(phrase)

string = "Hello World!"
phrase = "Hello"
starts_check = starts_with(string, phrase)
print(f"Does the string start with '{phrase}'? {starts_check}")
# Output: Does the string start with 'Hello'? True
print("\n")

# 18. Check if a string ends with a specific word or phrase.
def ends_with(s, phrase):
    return s.endswith(phrase)

string = "Hello World!"
phrase = "World!"
ends_check = ends_with(string, phrase)
print(f"Does the string end with '{phrase}'? {ends_check}")
# Output: Does the string end with 'World!'? True
print("\n")

# 19. Convert a string to title case (e.g., "hello world" to "Hello World").
def to_title_case(s):
    return s.title()

string = "hello world"
title_case_string = to_title_case(string)
print(f"Title case string: {title_case_string}")
# Output: Title case string: Hello World
print("\n")

# 20. Find the longest word in a string.
def longest_word(s):
    words = s.split()
    return max(words, key=len)

string = "The quick brown fox jumps over the lazy dog"
longest = longest_word(string)
print(f"The longest word in the string is: {longest}")
# Output: The longest word in the string is: jumps
print("\n")

# 21. Find the shortest word in a string.
def shortest_word(s):
    words = s.split()
    return min(words, key=len)

string = "The quick brown fox jumps over the lazy dog"
shortest = shortest_word(string)
print(f"The shortest word in the string is: {shortest}")
# Output: The shortest word in the string is: The
print("\n")

# 22. Reverse the order of words in a string.
def reverse_word_order(s):
    words = s.split()
    return " ".join(reversed(words))

string = "The quick brown fox"
reversed_order = reverse_word_order(string)
print(f"String with reversed word order: {reversed_order}")
# Output: String with reversed word order: fox brown quick The
print("\n")

# 23. Check if a string is alphanumeric.
def is_alphanumeric(s):
    return s.isalnum()

string = "Python3"
alphanumeric_check = is_alphanumeric(string)
print(f"Is the string '{string}' alphanumeric? {alphanumeric_check}")
# Output: Is the string 'Python3' alphanumeric? True
print("\n")

# 24. Extract all digits from a string.
def extract_digits(s):
    return "".join([char for char in s if char.isdigit()])

string = "abc123xyz456"
digits = extract_digits(string)
print(f"Extracted digits: {digits}")
# Output: Extracted digits: 123456
print("\n")

# 25. Extract all alphabets from a string.
def extract_alphabets(s):
    return "".join([char for char in s if char.isalpha()])

string = "abc123xyz456"
alphabets = extract_alphabets(string)
print(f"Extracted alphabets: {alphabets}")
# Output: Extracted alphabets: abcxyz
print("\n")

# 26. Count the number of uppercase letters in a string.
def count_uppercase(s):
    return sum(1 for char in s if char.isupper())

string = "Hello World!"
uppercase_count = count_uppercase(string)
print(f"Number of uppercase letters: {uppercase_count}")
# Output: Number of uppercase letters: 2
print("\n")

# 27. Count the number of lowercase letters in a string.
def count_lowercase(s):
    return sum(1 for char in s if char.islower())

string = "Hello World!"
lowercase_count = count_lowercase(string)
print(f"Number of lowercase letters: {lowercase_count}")
# Output: Number of lowercase letters: 8
print("\n")

# 28. Swap the case of each character in a string.
def swap_case(s):
    return s.swapcase()

string = "Hello World!"
swapped_case_string = swap_case(string)
print(f"String with swapped case: {swapped_case_string}")
# Output: String with swapped case: hELLO wORLD!
print("\n")

# 29. Remove a specific word from a string.
def remove_word(s, word):
    return s.replace(word, "")

string = "The quick brown fox jumps over the lazy dog"
word_to_remove = "quick"
modified_string = remove_word(string, word_to_remove)
print(f"String after removing '{word_to_remove}': {modified_string}")
# Output: String after removing 'quick': The  brown fox jumps over the lazy dog
print("\n")

# 30. Check if a string is a valid email address.
import re
def is_valid_email(s):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(email_regex, s))

string = "test@example.com"
email_check = is_valid_email(string)
print(f"Is the string '{string}' a valid email address? {email_check}")
# Output: Is the string 'test@example.com' a valid email address? True


import re
from collections import Counter

# 31. Extract the username from an email address string.
def extract_username(email):
    return email.split('@')[0]

email = "user@example.com"
username = extract_username(email)
print(f"Username: {username}")
# Output: Username: user
print("\n")

# 32. Extract the domain name from an email address string.
def extract_domain(email):
    return email.split('@')[1]

email = "user@example.com"
domain = extract_domain(email)
print(f"Domain: {domain}")
# Output: Domain: example.com
print("\n")

# 33. Replace multiple spaces in a string with a single space.
def replace_multiple_spaces(s):
    return re.sub(r'\s+', ' ', s)

string = "Hello    World     Python"
new_string = replace_multiple_spaces(string)
print(f"String with single spaces: {new_string}")
# Output: String with single spaces: Hello World Python
print("\n")

# 34. Check if a string is a valid URL.
def is_valid_url(url):
    url_regex = r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"
    return bool(re.match(url_regex, url))

url = "https://www.example.com"
url_check = is_valid_url(url)
print(f"Is '{url}' a valid URL? {url_check}")
# Output: Is 'https://www.example.com' a valid URL? True
print("\n")

# 35. Extract the protocol (http or https) from a URL string.
def extract_protocol(url):
    return url.split(":")[0]

url = "https://www.example.com"
protocol = extract_protocol(url)
print(f"Protocol: {protocol}")
# Output: Protocol: https
print("\n")

# 36. Find the frequency of each character in a string.
def character_frequency(s):
    return dict(Counter(s))

string = "hello"
frequency = character_frequency(string)
print(f"Character frequencies: {frequency}")
# Output: Character frequencies: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
print("\n")

# 37. Remove all punctuation from a string.
import string as str_lib
def remove_punctuation(s):
    return s.translate(str.maketrans('', '', str_lib.punctuation))

string = "Hello, World!"
no_punctuation = remove_punctuation(string)
print(f"String without punctuation: {no_punctuation}")
# Output: String without punctuation: Hello World
print("\n")

# 38. Check if a string contains only digits.
def is_digits(s):
    return s.isdigit()

string = "12345"
digit_check = is_digits(string)
print(f"Does the string contain only digits? {digit_check}")
# Output: Does the string contain only digits? True
print("\n")

# 39. Check if a string contains only alphabets.
def is_alphabets(s):
    return s.isalpha()

string = "Hello"
alphabet_check = is_alphabets(string)
print(f"Does the string contain only alphabets? {alphabet_check}")
# Output: Does the string contain only alphabets? True
print("\n")

# 40. Convert a string to a list of characters.
def string_to_list(s):
    return list(s)

string = "Hello"
char_list = string_to_list(string)
print(f"List of characters: {char_list}")
# Output: List of characters: ['H', 'e', 'l', 'l', 'o']
print("\n")

# 41. Check if two strings are anagrams.
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

string1 = "listen"
string2 = "silent"
anagram_check = are_anagrams(string1, string2)
print(f"Are '{string1}' and '{string2}' anagrams? {anagram_check}")
# Output: Are 'listen' and 'silent' anagrams? True
print("\n")

# 42. Encode a string using a Caesar cipher.
def caesar_cipher_encode(s, shift):
    result = []
    for char in s:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

string = "Hello"
shift_value = 3
encoded_string = caesar_cipher_encode(string, shift_value)
print(f"Encoded string: {encoded_string}")
# Output: Encoded string: Khoor
print("\n")

# 43. Decode a Caesar cipher encoded string.
def caesar_cipher_decode(s, shift):
    return caesar_cipher_encode(s, -shift)

encoded_string = "Khoor"
decoded_string = caesar_cipher_decode(encoded_string, shift_value)
print(f"Decoded string: {decoded_string}")
# Output: Decoded string: Hello
print("\n")

# 44. Find the most frequent word in a string.
def most_frequent_word(s):
    words = s.split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

string = "apple banana apple orange apple"
most_frequent = most_frequent_word(string)
print(f"The most frequent word is: {most_frequent[0]} with frequency {most_frequent[1]}")
# Output: The most frequent word is: apple with frequency 3
print("\n")

# 45. Find all unique words in a string.
def unique_words(s):
    words = s.split()
    return set(words)

string = "apple banana apple orange apple"
unique_word_list = unique_words(string)
print(f"Unique words: {unique_word_list}")
# Output: Unique words: {'banana', 'orange', 'apple'}
print("\n")

# 46. Count the number of syllables in a string.
import nltk
nltk.download('cmudict')
from nltk.corpus import cmudict

def count_syllables(word):
    d = cmudict.dict()
    if word.lower() in d:
        return max([len(list(y)) for y in d[word.lower()]])
    else:
        return 0

def syllable_count_in_string(s):
    words = s.split()
    return sum(count_syllables(word) for word in words)

string = "hello everyone how are you"
syllable_count = syllable_count_in_string(string)
print(f"Total syllables in the string: {syllable_count}")
# Output: Total syllables in the string: 8
print("\n")

# 47. Check if a string contains any special characters.
def contains_special_chars(s):
    return bool(re.search(r'[^A-Za-z0-9 ]', s))

string = "Hello@world"
special_char_check = contains_special_chars(string)
print(f"Does the string contain special characters? {special_char_check}")
# Output: Does the string contain special characters? True
print("\n")

# 48. Remove the nth word from a string.
def remove_nth_word(s, n):
    words = s.split()
    if 0 <= n < len(words):
        words.pop(n)
    return ' '.join(words)

string = "The quick brown fox jumps"
n = 2
modified_string = remove_nth_word(string, n)
print(f"String after removing {n}th word: {modified_string}")
# Output: String after removing 2th word: The quick fox jumps
print("\n")

# 49. Insert a word at the nth position in a string.
def insert_nth_word(s, word, n):
    words = s.split()
    words.insert(n, word)
    return ' '.join(words)

string = "The brown fox jumps"
word_to_insert = "quick"
n = 1
modified_string = insert_nth_word(string, word_to_insert, n)
print(f"String after inserting word at {n}th position: {modified_string}")
# Output: String after inserting word at 1th position: The quick brown fox jumps
print("\n")

# 50. Convert a CSV string to a list of lists.
def csv_to_list(csv_string):
    rows = csv_string.split("\n")
    return [row.split(",") for row in rows]

csv_string = "name,age,city\nJohn,30,New York\nJane,25,Los Angeles"
list_of_lists = csv_to_list(csv_string)
print(f"Converted CSV to list of lists: {list_of_lists}")
# Output: Converted CSV to list of lists: [['name', 'age', 'city'], ['John', '30', 'New York'], ['Jane', '25', 'Los Angeles']]




List Based Practice Problem :



import random

# 1. Create a list with integers from 1 to 10.
list1 = [i for i in range(1, 11)]
print("List of integers from 1 to 10:", list1)
# Output: List of integers from 1 to 10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\n")

# 2. Find the length of a list without using the `len()` function.
def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

length = list_length(list1)
print("Length of the list:", length)
# Output: Length of the list: 10
print("\n")

# 3. Append an element to the end of a list.
list1.append(11)
print("List after appending 11:", list1)
# Output: List after appending 11: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("\n")

# 4. Insert an element at a specific index in a list.
list1.insert(5, 50)
print("List after inserting 50 at index 5:", list1)
# Output: List after inserting 50 at index 5: [1, 2, 3, 4, 5, 50, 6, 7, 8, 9, 10, 11]
print("\n")

# 5. Remove an element from a list by its value.
list1.remove(50)
print("List after removing 50:", list1)
# Output: List after removing 50: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("\n")

# 6. Remove an element from a list by its index.
del list1[2]
print("List after removing element at index 2:", list1)
# Output: List after removing element at index 2: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
print("\n")

# 7. Check if an element exists in a list.
element_exists = 5 in list1
print("Does 5 exist in the list?", element_exists)
# Output: Does 5 exist in the list? True
print("\n")

# 8. Find the index of the first occurrence of an element in a list.
index = list1.index(5)
print("Index of first occurrence of 5:", index)
# Output: Index of first occurrence of 5: 4
print("\n")

# 9. Count the occurrences of an element in a list.
count = list1.count(7)
print("Occurrences of 7:", count)
# Output: Occurrences of 7: 1
print("\n")

# 10. Reverse the order of elements in a list.
list1.reverse()
print("List after reversing:", list1)
# Output: List after reversing: [11, 10, 9, 8, 7, 6, 5, 4, 2, 1]
print("\n")

# 11. Sort a list in ascending order.
list1.sort()
print("List sorted in ascending order:", list1)
# Output: List sorted in ascending order: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
print("\n")

# 12. Sort a list in descending order.
list1.sort(reverse=True)
print("List sorted in descending order:", list1)
# Output: List sorted in descending order: [11, 10, 9, 8, 7, 6, 5, 4, 2, 1]
print("\n")

# 13. Create a list of even numbers from 1 to 20.
even_numbers = [i for i in range(1, 21) if i % 2 == 0]
print("Even numbers from 1 to 20:", even_numbers)
# Output: Even numbers from 1 to 20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print("\n")

# 14. Create a list of odd numbers from 1 to 20.
odd_numbers = [i for i in range(1, 21) if i % 2 != 0]
print("Odd numbers from 1 to 20:", odd_numbers)
# Output: Odd numbers from 1 to 20: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print("\n")

# 15. Find the sum of all elements in a list.
total_sum = sum(list1)
print("Sum of elements in the list:", total_sum)
# Output: Sum of elements in the list: 75
print("\n")

# 16. Find the maximum value in a list.
max_value = max(list1)
print("Maximum value in the list:", max_value)
# Output: Maximum value in the list: 11
print("\n")

# 17. Find the minimum value in a list.
min_value = min(list1)
print("Minimum value in the list:", min_value)
# Output: Minimum value in the list: 1
print("\n")

# 18. Create a list of squares of numbers from 1 to 10.
squares = [i**2 for i in range(1, 11)]
print("Squares of numbers from 1 to 10:", squares)
# Output: Squares of numbers from 1 to 10: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("\n")

# 19. Create a list of random numbers.
random_numbers = [random.randint(1, 100) for _ in range(10)]
print("Random numbers:", random_numbers)
# Output: Random numbers: [Randomly generated list of numbers]
print("\n")

# 20. Remove duplicates from a list.
list_with_duplicates = [1, 2, 2, 3, 4, 5, 5, 6]
unique_list = list(set(list_with_duplicates))
print("List after removing duplicates:", unique_list)
# Output: List after removing duplicates: [1, 2, 3, 4, 5, 6]
print("\n")

# 21. Find the common elements between two lists.
list2 = [4, 5, 6, 7]
common_elements = list(set(list1) & set(list2))
print("Common elements between lists:", common_elements)
# Output: Common elements between lists: [4, 5, 6]
print("\n")

# 22. Find the difference between two lists.
difference = list(set(list1) - set(list2))
print("Difference between lists:", difference)
# Output: Difference between lists: [1, 2, 3, 8, 9, 10, 11]
print("\n")

# 23. Merge two lists.
merged_list = list1 + list2
print("Merged list:", merged_list)
# Output: Merged list: [11, 10, 9, 8, 7, 6, 5, 4, 2, 1, 4, 5, 6, 7]
print("\n")

# 24. Multiply all elements in a list by 2.
multiplied_by_two = [x * 2 for x in list1]
print("List after multiplying by 2:", multiplied_by_two)
# Output: List after multiplying by 2: [22, 20, 18, 16, 14, 12, 10, 8, 4, 2]
print("\n")

# 25. Filter out all even numbers from a list.
filtered_odd = [x for x in list1 if x % 2 != 0]
print("List after filtering out even numbers:", filtered_odd)
# Output: List after filtering out even numbers: [11, 9, 7, 5, 3, 1]
print("\n")

# 26. Convert a list of strings to a list of integers.
string_list = ['1', '2', '3', '4']
integer_list = [int(x) for x in string_list]
print("List of integers:", integer_list)
# Output: List of integers: [1, 2, 3, 4]
print("\n")

# 27. Convert a list of integers to a list of strings.
integer_list = [1, 2, 3, 4]
string_list = [str(x) for x in integer_list]
print("List of strings:", string_list)
# Output: List of strings: ['1', '2', '3', '4']
print("\n")

# 28. Flatten a nested list.
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened_list)
# Output: Flattened list: [1, 2, 3, 4, 5, 6]
print("\n")

# 29. Create a list of the first 10 Fibonacci numbers.
fib_list = [0, 1]
for i in range(2, 10):
    fib_list.append(fib_list[i-1] + fib_list[i-2])
print("Fibonacci sequence:", fib_list)
# Output: Fibonacci sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print("\n")

# 30. Check if a list is sorted.
is_sorted = list1 == sorted(list1)
print("Is the list sorted?", is_sorted)
# Output: Is the list sorted? True or False based on the list
print("\n")

# 31. Rotate a list to the left by `n` positions.
def rotate_left(lst, n):
    return lst[n:] + lst[:n]

rotated_left = rotate_left(list1, 3)
print("List after rotating left by 3 positions:", rotated_left)
# Output: List after rotating left by 3 positions: [8, 7, 6, 5, 4, 2, 1, 11, 10, 9]
print("\n")

# 32. Rotate a list to the right by `n` positions.
def rotate_right(lst, n):
    return lst[-n:] + lst[:-n]

rotated_right = rotate_right(list1, 3)
print("List after rotating right by 3 positions:", rotated_right)
# Output: List after rotating right by 3 positions: [9, 10, 11, 1, 2, 4, 5, 6, 7, 8]
print("\n")

# 33. Create a list of prime numbers up to 50.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [x for x in range(1, 51) if is_prime(x)]
print("Prime numbers up to 50:", prime_numbers)
# Output: Prime numbers up to 50: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print("\n")

# 34. Split a list into chunks of size `n`.
def chunk_list(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

chunked_list = chunk_list(list1, 3)
print("List split into chunks of size 3:", chunked_list)
# Output: List split into chunks of size 3: [[11, 10, 9], [8, 7, 6], [5, 4, 2], [1]]
print("\n")

# 35. Find the second largest number in a list.
second_largest = sorted(set(list1))[-2]
print("Second largest number in the list:", second_largest)
# Output: Second largest number in the list: 10
print("\n")

# 36. Replace every element in a list with its square.
squared_list = [x**2 for x in list1]
print("List after replacing elements with their squares:", squared_list)
# Output: List after replacing elements with their squares: [121, 100, 81, 64, 49, 36, 25, 16, 4, 1]
print("\n")

# 37. Convert a list to a dictionary where list elements become keys and their indices become values.
list_to_dict = {item: idx for idx, item in enumerate(list1)}
print("List converted to dictionary:", list_to_dict)
# Output: List converted to dictionary: {11: 0, 10: 1, 9: 2, 8: 3, 7: 4, 6: 5, 5: 6, 4: 7, 2: 8, 1: 9}
print("\n")

# 38. Shuffle the elements of a list randomly.
random.shuffle(list1)
print("List after shuffling:", list1)
# Output: List after shuffling: [Randomly shuffled list]
print("\n")

# 39. Create a list of the first 10 factorial numbers.
import math
factorial_list = [math.factorial(i) for i in range(1, 11)]
print("List of first 10 factorial numbers:", factorial_list)
# Output: List of first 10 factorial numbers: [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
print("\n")

# 40. Check if two lists have at least one element in common.
has_common_elements = bool(set(list1) & set(list2))
print("Do the lists have at least one common element?", has_common_elements)
# Output: Do the lists have at least one common element? True or False
print("\n")

# 41. Remove all elements from a list.
list1.clear()
print("List after clearing all elements:", list1)
# Output: List after clearing all elements: []
print("\n")

# 42. Replace negative numbers in a list with 0.
list_with_negatives = [-1, 2, -3, 4]
list_without_negatives = [0 if x < 0 else x for x in list_with_negatives]
print("List after replacing negatives with 0:", list_without_negatives)
# Output: List after replacing negatives with 0: [0, 2, 0, 4]
print("\n")

# 43. Convert a string into a list of words.
sentence = "This is a test sentence"
word_list = sentence.split()
print("List of words:", word_list)
# Output: List of words: ['This', 'is', 'a', 'test', 'sentence']
print("\n")

# 44. Convert a list of words into a string.
words = ['This', 'is', 'a', 'test']
sentence = ' '.join(words)
print("String from words:", sentence)
# Output: String from words: "This is a test"
print("\n")

# 45. Create a list of the first `n` powers of 2.
n = 5
powers_of_two = [2**i for i in range(n)]
print(f"First {n} powers of 2:", powers_of_two)
# Output: First 5 powers of 2: [1, 2, 4, 8, 16]
print("\n")

# 46. Find the longest string in a list of strings.
strings = ['apple', 'banana', 'cherry', 'date']
longest_string = max(strings, key=len)
print("Longest string:", longest_string)
# Output: Longest string: banana
print("\n")

# 47. Find the shortest string in a list of strings.
shortest_string = min(strings, key=len)
print("Shortest string:", shortest_string)
# Output: Shortest string: date
print("\n")

# 48. Create a list of the first `n` triangular numbers.
def triangular_number(n):
    return (n * (n + 1)) // 2

triangular_numbers = [triangular_number(i) for i in range(1, 11)]
print("First 10 triangular numbers:", triangular_numbers)
# Output: First 10 triangular numbers: [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
print("\n")

# 49. Check if a list contains another list as a subsequence.
def contains_subsequence(lst, sub_lst):
    return any(lst[i:i+len(sub_lst)] == sub_lst for i in range(len(lst) - len(sub_lst) + 1))

subsequence = [5, 6]
contains_subseq = contains_subsequence(list1, subsequence)
print("Does the list contain the subsequence?", contains_subseq)
# Output: Does the list contain the subsequence? True or False
print("\n")

# 50. Swap two elements in a list by their indices.
def swap_elements(lst, idx1, idx2):
    lst[idx1], lst[idx2] = lst[idx2], lst[idx1]

swap_elements(list1, 0, 4)
print("List after swapping elements at index 0 and 4:", list1)
# Output: List after swapping elements at index 0 and 4: [6, 2, 3, 4, 5, 1]


Tuple Based Practice Problem :

# 1. Create a tuple with integers from 1 to 5.
tuple1 = (1, 2, 3, 4, 5)
print("Tuple with integers from 1 to 5:", tuple1)
# Output: (1, 2, 3, 4, 5)
print("\n")

# 2. Access the third element of a tuple.
third_element = tuple1[2]
print("Third element:", third_element)
# Output: 3
print("\n")

# 3. Find the length of a tuple without using the `len()` function.
def tuple_length(tpl):
    count = 0
    for _ in tpl:
        count += 1
    return count

length = tuple_length(tuple1)
print("Length of tuple:", length)
# Output: 5
print("\n")

# 4. Count the occurrences of an element in a tuple.
count_occurrences = tuple1.count(3)
print("Occurrences of 3:", count_occurrences)
# Output: 1
print("\n")

# 5. Find the index of the first occurrence of an element in a tuple.
index_of_element = tuple1.index(4)
print("Index of first occurrence of 4:", index_of_element)
# Output: 3
print("\n")

# 6. Check if an element exists in a tuple.
element_exists = 5 in tuple1
print("Does 5 exist in the tuple?", element_exists)
# Output: True
print("\n")

# 7. Convert a tuple to a list.
tuple_to_list = list(tuple1)
print("Tuple converted to list:", tuple_to_list)
# Output: [1, 2, 3, 4, 5]
print("\n")

# 8. Convert a list to a tuple.
list1 = [1, 2, 3, 4, 5]
list_to_tuple = tuple(list1)
print("List converted to tuple:", list_to_tuple)
# Output: (1, 2, 3, 4, 5)
print("\n")

# 9. Unpack the elements of a tuple into variables.
a, b, c, d, e = tuple1
print("Unpacked values:", a, b, c, d, e)
# Output: Unpacked values: 1 2 3 4 5
print("\n")

# 10. Create a tuple of even numbers from 1 to 10.
even_tuple = (2, 4, 6, 8, 10)
print("Tuple of even numbers:", even_tuple)
# Output: (2, 4, 6, 8, 10)
print("\n")

# 11. Create a tuple of odd numbers from 1 to 10.
odd_tuple = (1, 3, 5, 7, 9)
print("Tuple of odd numbers:", odd_tuple)
# Output: (1, 3, 5, 7, 9)
print("\n")

# 12. Concatenate two tuples.
tuple2 = (6, 7, 8)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)
# Output: (1, 2, 3, 4, 5, 6, 7, 8)
print("\n")

# 13. Repeat a tuple three times.
repeated_tuple = tuple1 * 3
print("Repeated tuple:", repeated_tuple)
# Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print("\n")

# 14. Check if a tuple is empty.
empty_tuple = ()
print("Is the tuple empty?", len(empty_tuple) == 0)
# Output: True
print("\n")

# 15. Create a nested tuple.
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)
# Output: ((1, 2), (3, 4), (5, 6))
print("\n")

# 16. Access the first element of a nested tuple.
first_element_nested = nested_tuple[0]
print("First element of nested tuple:", first_element_nested)
# Output: (1, 2)
print("\n")

# 17. Create a tuple with a single element.
single_element_tuple = (42,)
print("Tuple with a single element:", single_element_tuple)
# Output: (42,)
print("\n")

# 18. Compare two tuples.
tuple3 = (1, 2, 3)
tuple4 = (1, 2, 3)
are_equal = tuple3 == tuple4
print("Are the two tuples equal?", are_equal)
# Output: True
print("\n")

# 19. Delete a tuple.
# Note: You can't delete a tuple directly if it's in use, but you can delete the variable.
# We’ll assign None to demonstrate.
tuple1 = None
print("Tuple after deletion:", tuple1)
# Output: None
print("\n")

# 20. Slice a tuple.
sliced_tuple = tuple2[1:3]
print("Sliced tuple:", sliced_tuple)
# Output: (7, 8)
print("\n")

# 21. Find the maximum value in a tuple.
max_value = max(tuple1)
print("Maximum value in the tuple:", max_value)
# Output: 5
print("\n")

# 22. Find the minimum value in a tuple.
min_value = min(tuple1)
print("Minimum value in the tuple:", min_value)
# Output: 1
print("\n")

# 23. Convert a string to a tuple of characters.
string = "hello"
string_to_tuple = tuple(string)
print("Tuple from string:", string_to_tuple)
# Output: ('h', 'e', 'l', 'l', 'o')
print("\n")

# 24. Convert a tuple of characters to a string.
tuple_of_chars = ('h', 'e', 'l', 'l', 'o')
tuple_to_string = ''.join(tuple_of_chars)
print("String from tuple of characters:", tuple_to_string)
# Output: hello
print("\n")

# 25. Create a tuple from multiple data types.
mixed_tuple = (1, 3.14, "hello", True)
print("Tuple with multiple data types:", mixed_tuple)
# Output: (1, 3.14, 'hello', True)
print("\n")

# 26. Check if two tuples are identical.
identical = tuple1 == tuple2
print("Are the two tuples identical?", identical)
# Output: False or True based on the content of tuple1 and tuple2
print("\n")

# 27. Sort the elements of a tuple.
sorted_tuple = tuple(sorted(tuple1))
print("Sorted tuple:", sorted_tuple)
# Output: Sorted tuple: (1, 2, 3, 4, 5)
print("\n")

# 28. Convert a tuple of integers to a tuple of strings.
integer_tuple = (1, 2, 3)
string_tuple = tuple(map(str, integer_tuple))
print("Tuple of strings:", string_tuple)
# Output: ('1', '2', '3')
print("\n")

# 29. Convert a tuple of strings to a tuple of integers.
string_tuple2 = ('1', '2', '3')
int_tuple = tuple(map(int, string_tuple2))
print("Tuple of integers:", int_tuple)
# Output: (1, 2, 3)
print("\n")

# 30. Merge two tuples.
tuple5 = (7, 8, 9)
merged_tuple = tuple1 + tuple5
print("Merged tuple:", merged_tuple)
# Output: (1, 2, 3, 4, 5, 7, 8, 9)
print("\n")

# 31. Flatten a nested tuple.
nested_tuple2 = ((1, 2), (3, 4), (5, 6))
flattened_tuple = tuple(item for subtuple in nested_tuple2 for item in subtuple)
print("Flattened tuple:", flattened_tuple)
# Output: (1, 2, 3, 4, 5, 6)
print("\n")

# 32. Create a tuple of the first 5 prime numbers.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = tuple(x for x in range(1, 20) if is_prime(x))[:5]
print("First 5 prime numbers:", prime_numbers)
# Output: (2, 3, 5, 7, 11)
print("\n")

# 33. Check if a tuple is a palindrome.
palindrome_tuple = (1, 2, 3, 2, 1)
is_palindrome = palindrome_tuple == palindrome_tuple[::-1]
print("Is the tuple a palindrome?", is_palindrome)
# Output: True
print("\n")

# 34. Create a tuple of squares of numbers from 1 to 5.
squares_tuple = tuple(x**2 for x in range(1, 6))
print("Tuple of squares:", squares_tuple)
# Output: (1, 4, 9, 16, 25)
print("\n")

# 35. Filter out all even numbers from a tuple.
tuple_with_evens = (1, 2, 3, 4, 5, 6)
filtered_tuple = tuple(x for x in tuple_with_evens if x % 2 != 0)
print("Tuple with odd numbers only:", filtered_tuple)
# Output: (1, 3, 5)
print("\n")

# 36. Multiply all elements in a tuple by 2.
multiplied_tuple = tuple(x * 2 for x in tuple1)
print("Tuple after multiplying by 2:", multiplied_tuple)
# Output: (2, 4, 6, 8, 10)
print("\n")


# 38. Check if a tuple is sorted.
tuple_to_check = (1, 2, 3, 4, 5)
is_sorted = tuple_to_check == tuple(sorted(tuple_to_check))
print("Is the tuple sorted?", is_sorted)
# Output: True

print("\n")

# 39. Rotate a tuple to the left by `n` positions.
def rotate_left(tpl, n):
    n = n % len(tpl)  # To handle if n is greater than tuple length
    return tpl[n:] + tpl[:n]

tuple_to_rotate_left = (1, 2, 3, 4, 5)
rotated_left_tuple = rotate_left(tuple_to_rotate_left, 2)
print("Tuple after rotating left by 2 positions:", rotated_left_tuple)
# Output: (3, 4, 5, 1, 2)

print("\n")

# 40. Rotate a tuple to the right by `n` positions.
def rotate_right(tpl, n):
    n = n % len(tpl)  # To handle if n is greater than tuple length
    return tpl[-n:] + tpl[:-n]

tuple_to_rotate_right = (1, 2, 3, 4, 5)
rotated_right_tuple = rotate_right(tuple_to_rotate_right, 2)
print("Tuple after rotating right by 2 positions:", rotated_right_tuple)
# Output: (4, 5, 1, 2, 3)

print("\n")

# 41. Create a tuple of the first 5 Fibonacci numbers.
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return tuple(fib_sequence)

fibonacci_tuple = fibonacci(5)
print("First 5 Fibonacci numbers:", fibonacci_tuple)
# Output: (0, 1, 1, 2, 3)

print("\n")

# 42. Create a tuple from user input.
user_input = input("Enter comma-separated values: ")
user_tuple = tuple(user_input.split(','))
print("Tuple from user input:", user_tuple)

# Output: Tuple based on the input (e.g., ('apple', 'banana', 'cherry'))

print("\n")

# 43. Swap two elements in a tuple.
def swap_tuple_elements(tpl, index1, index2):
    tpl_list = list(tpl)
    tpl_list[index1], tpl_list[index2] = tpl_list[index2], tpl_list[index1]
    return tuple(tpl_list)

tuple_to_swap = (1, 2, 3, 4, 5)
swapped_tuple = swap_tuple_elements(tuple_to_swap, 1, 3)
print("Tuple after swapping elements:", swapped_tuple)
# Output: (1, 4, 3, 2, 5)

print("\n")

# 44. Reverse the elements of a tuple.
reversed_tuple = tuple_to_swap[::-1]
print("Reversed tuple:", reversed_tuple)
# Output: (5, 4, 3, 2, 1)

print("\n")

# 45. Create a tuple of the first `n` powers of 2.
def powers_of_two(n):
    return tuple(2**i for i in range(n))

powers_tuple = powers_of_two(5)
print("Tuple of the first 5 powers of 2:", powers_tuple)
# Output: (1, 2, 4, 8, 16)

print("\n")

# 46. Find the longest string in a tuple of strings.
string_tuple = ("apple", "banana", "grape", "kiwi")
longest_string = max(string_tuple, key=len)
print("Longest string in tuple:", longest_string)
# Output: "banana"

print("\n")

# 47. Find the shortest string in a tuple of strings.
shortest_string = min(string_tuple, key=len)
print("Shortest string in tuple:", shortest_string)
# Output: "kiwi"

print("\n")

# 48. Create a tuple of the first `n` triangular numbers.
def triangular_numbers(n):
    return tuple(sum(range(i+1)) for i in range(n))

triangular_tuple = triangular_numbers(5)
print("First 5 triangular numbers:", triangular_tuple)
# Output: (0, 1, 3, 6, 10)

print("\n")

# 49. Check if a tuple contains another tuple as a subsequence.
def is_subsequence(tpl1, tpl2):
    return any(tpl1 == tpl2[i:i+len(tpl1)] for i in range(len(tpl2)-len(tpl1)+1))

tuple1 = (2, 3)
tuple2 = (1, 2, 3, 4, 5)
is_subseq = is_subsequence(tuple1, tuple2)
print("Does tuple1 exist as a subsequence in tuple2?", is_subseq)
# Output: True

print("\n")

# 50. Create a tuple of alternating 1s and 0s of length `n`.
def alternating_tuple(n):
    return tuple(1 if i % 2 == 0 else 0 for i in range(n))

alt_tuple = alternating_tuple(6)
print("Tuple of alternating 1s and 0s of length 6:", alt_tuple)
# Output: (1, 0, 1, 0, 1, 0)

Set Based Practice Problem :

# 1. Create a set with integers from 1 to 5.
set1 = {1, 2, 3, 4, 5}
print("Set 1:", set1)

# Output:
# Set 1: {1, 2, 3, 4, 5}


# 2. Add an element to a set.
set1.add(6)
print("Set after adding 6:", set1)

# Output:
# Set after adding 6: {1, 2, 3, 4, 5, 6}


# 3. Remove an element from a set.
set1.remove(4)
print("Set after removing 4:", set1)

# Output:
# Set after removing 4: {1, 2, 3, 5, 6}


# 4. Check if an element exists in a set.
exists = 3 in set1
print("Does 3 exist in the set?", exists)

# Output:
# Does 3 exist in the set? True


# 5. Find the length of a set without using the `len()` function.
set_length = sum(1 for _ in set1)
print("Length of the set:", set_length)

# Output:
# Length of the set: 5


# 6. Clear all elements from a set.
set1.clear()
print("Set after clearing:", set1)

# Output:
# Set after clearing: set()


# 7. Create a set of even numbers from 1 to 10.
even_set = {x for x in range(1, 11) if x % 2 == 0}
print("Even numbers set:", even_set)

# Output:
# Even numbers set: {2, 4, 6, 8, 10}


# 8. Create a set of odd numbers from 1 to 10.
odd_set = {x for x in range(1, 11) if x % 2 != 0}
print("Odd numbers set:", odd_set)

# Output:
# Odd numbers set: {1, 3, 5, 7, 9}


# 9. Find the union of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("Union of sets:", union_set)

# Output:
# Union of sets: {1, 2, 3, 4, 5}


# 10. Find the intersection of two sets.
intersection_set = set1 & set2
print("Intersection of sets:", intersection_set)

# Output:
# Intersection of sets: {3}


# 11. Find the difference between two sets.
difference_set = set1 - set2
print("Difference of sets:", difference_set)

# Output:
# Difference of sets: {1, 2}


# 12. Check if a set is a subset of another set.
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?", is_subset)

# Output:
# Is set1 a subset of set2? False


# 13. Check if a set is a superset of another set.
is_superset = set1.issuperset(set2)
print("Is set1 a superset of set2?", is_superset)

# Output:
# Is set1 a superset of set2? False


# 14. Create a set from a list.
list1 = [1, 2, 3, 4]
set_from_list = set(list1)
print("Set from list:", set_from_list)

# Output:
# Set from list: {1, 2, 3, 4}


# 15. Convert a set to a list.
set2 = {5, 6, 7, 8}
list_from_set = list(set2)
print("List from set:", list_from_set)

# Output:
# List from set: [5, 6, 7, 8]


# 16. Remove a random element from a set.
import random
random_element = set2.pop()
print("Removed random element:", random_element)
print("Set after removal:", set2)

# Output:
# Removed random element: 5
# Set after removal: {6, 7, 8}


# 17. Pop an element from a set.
popped_element = set2.pop()
print("Popped element:", popped_element)
print("Set after popping:", set2)

# Output:
# Popped element: 6
# Set after popping: {7, 8}


# 18. Check if two sets have no elements in common.
set3 = {9, 10, 11}
no_common_elements = set1.isdisjoint(set3)
print("Do set1 and set3 have no elements in common?", no_common_elements)

# Output:
# Do set1 and set3 have no elements in common? True


# 19. Find the symmetric difference between two sets.
symmetric_difference_set = set1 ^ set2
print("Symmetric difference between sets:", symmetric_difference_set)

# Output:
# Symmetric difference between sets: {1, 2, 3, 4, 5, 6}


# 20. Update a set with elements from another set.
set1.update(set2)
print("Set1 after update with set2:", set1)

# Output:
# Set1 after update with set2: {1, 2, 3, 4, 5, 6, 7, 8}


# 21. Create a set of the first 5 prime numbers.
prime_set = {2, 3, 5, 7, 11}
print("Set of first 5 primes:", prime_set)

# Output:
# Set of first 5 primes: {2, 3, 5, 7, 11}


# 22. Check if two sets are identical.
set1 = {1, 2, 3}
set2 = {1, 2, 3}
are_identical = set1 == set2
print("Are set1 and set2 identical?", are_identical)

# Output:
# Are set1 and set2 identical? True


# 23. Create a frozen set.
frozen_set = frozenset([1, 2, 3, 4])
print("Frozen set:", frozen_set)

# Output:
# Frozen set: frozenset({1, 2, 3, 4})


# 24. Check if a set is disjoint with another set.
disjoint_check = set1.isdisjoint(set2)
print("Are set1 and set2 disjoint?", disjoint_check)

# Output:
# Are set1 and set2 disjoint? False


# 25. Create a set of squares of numbers from 1 to 5.
squares_set = {x**2 for x in range(1, 6)}
print("Set of squares:", squares_set)

# Output:
# Set of squares: {1, 4, 9, 16, 25}


# 26. Filter out all even numbers from a set.
filtered_set = {x for x in set1 if x % 2 != 0}
print("Set after filtering even numbers:", filtered_set)

# Output:
# Set after filtering even numbers: {1, 3}


# 27. Multiply all elements in a set by 2.
multiplied_set = {x * 2 for x in set1}
print("Set after multiplying each element by 2:", multiplied_set)

# Output:
# Set after multiplying each element by 2: {2, 4, 6}


# 28. Create a set of random numbers.
random_set = {random.randint(1, 10) for _ in range(5)}
print("Random number set:", random_set)

# Output:
# Random number set: {1, 2, 3, 5, 9} (example)


# 29. Check if a set is empty.
is_empty = len(set1) == 0
print("Is the set empty?", is_empty)

# Output:
# Is the set empty? False


# 30. Create a nested set (hint: use frozenset).
nested_set = {frozenset([1, 2]), frozenset([3, 4])}
print("Nested set:", nested_set)

# Output:
# Nested set: {frozenset({1, 2}), frozenset({3, 4})}


# 31. Remove an element from a set using the discard method.
set1.discard(3)
print("Set after discarding 3:", set1)

# Output:
# Set after discarding 3: {1, 2}


# 32. Compare two sets.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
are_sets_equal = set1 == set2
print("Are set1 and set2 equal?", are_sets_equal)

# Output:
# Are set1 and set2 equal? False


# 33. Create a set from a string.
string = "hello"
set_from_string = set(string)
print("Set from string:", set_from_string)

# Output:
# Set from string: {'e', 'l', 'o', 'h'}


# 34. Convert a set of strings to a set of integers.
string_set = {"1", "2", "3", "4"}
int_set = {int(x) for x in string_set}
print("Set of integers:", int_set)

# Output:
# Set of integers: {1, 2, 3, 4}


# 35. Convert a set of integers to a set of strings.
int_set = {1, 2, 3, 4}
string_set = {str(x) for x in int_set}
print("Set of strings:", string_set)

# Output:
# Set of strings: {'1', '2', '3', '4'}


# 36. Create a set from a tuple.
tuple1 = (1, 2, 3, 4)
set_from_tuple = set(tuple1)
print("Set from tuple:", set_from_tuple)

# Output:
# Set from tuple: {1, 2, 3, 4}


# 37. Convert a set to a tuple.
set1 = {1, 2, 3, 4}
tuple_from_set = tuple(set1)
print("Tuple from set:", tuple_from_set)

# Output:
# Tuple from set: (1, 2, 3, 4)


# 38. Find the maximum value in a set.
max_value = max(set1)
print("Maximum value in the set:", max_value)

# Output:
# Maximum value in the set: 4


# 39. Find the minimum value in a set.
min_value = min(set1)
print("Minimum value in the set:", min_value)

# Output:
# Minimum value in the set: 1


# 40. Create a set from user input.
user_input = {int(x) for x in input("Enter numbers separated by spaces: ").split()}
print("Set from user input:", user_input)

# Output:
# Enter numbers separated by spaces: 4 5 6 7
# Set from user input: {4, 5, 6, 7}


# 41. Check if the intersection of two sets is empty.
set3 = {8, 9, 10}
is_intersection_empty = set1.isdisjoint(set3)
print("Is the intersection empty?", is_intersection_empty)

# Output:
# Is the intersection empty? True


# 42. Create a set of the first 5 Fibonacci numbers.
fib_set = {0, 1, 1, 2, 3, 5, 8}
print("Set of first 5 Fibonacci numbers:", fib_set)

# Output:
# Set of first 5 Fibonacci numbers: {0, 1, 2, 3, 5, 8}


# 43. Remove duplicates from a list using sets.
list_with_duplicates = [1, 2, 2, 3, 4, 4]
set_no_duplicates = set(list_with_duplicates)
print("List without duplicates:", set_no_duplicates)

# Output:
# List without duplicates: {1, 2, 3, 4}


# 44. Check if two sets have the same elements, regardless of their count.
set1 = {1, 2, 3}
set2 = {3, 2, 1}
have_same_elements = set1 == set2
print("Do set1 and set2 have the same elements?", have_same_elements)

# Output:
# Do set1 and set2 have the same elements? True


# 45. Create a set of the first `n` powers of 2.
n = 5
powers_of_two_set = {2**i for i in range(n)}
print("Set of the first 5 powers of 2:", powers_of_two_set)

# Output:
# Set of the first 5 powers of 2: {1, 2, 4, 8, 16}


# 46. Find the common elements between a set and a list.
list_data = [1, 2, 3, 4]
common_elements = set1 & set(list_data)
print("Common elements:", common_elements)

# Output:
# Common elements: {1, 2}


# 47. Create a set of the first `n` triangular numbers.
n = 5
triangular_set = {sum(range(i+1)) for i in range(n)}
print("Set of first 5 triangular numbers:", triangular_set)

# Output:
# Set of first 5 triangular numbers: {0, 1, 3, 6, 10}


# 48. Check if a set contains another set as a subset.
set1 = {1, 2, 3}
set2 = {2, 3}
is_subset = set2.issubset(set1)
print("Is set2 a subset of set1?", is_subset)

# Output:
# Is set2 a subset of set1? True


# 49. Create a set of alternating 1s and 0s of length `n`.
def alternating_set(n):
    return {1 if i % 2 == 0 else 0 for i in range(n)}

alternating_set = alternating_set(6)
print("Alternating set:", alternating_set)

# Output:
# Alternating set: {0, 1}


# 50. Merge multiple sets into one.
set1 = {1, 2}
set2 = {3, 4}
set3 = {5, 6}
merged_set = set1 | set2 | set3
print("Merged set:", merged_set)

# Output:
# Merged set: {1, 2, 3, 4, 5, 6}
