# 1. Print numbers from 1 to 10 using a for loop
print("1. Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# 2. Difference between a for loop and a while loop in Python
# For loop: It is used when you know the number of iterations beforehand. 
# While loop: It runs until a specified condition becomes False, and you don't necessarily know the number of iterations ahead of time.

# 3. Sum of all numbers from 1 to 100 using a for loop
sum_of_numbers = 0
for i in range(1, 101):
    sum_of_numbers += i
print("\n3. Sum of numbers from 1 to 100:", sum_of_numbers)

# 4. Iterate through a list using a for loop in Python
my_list = [10, 20, 30, 40, 50]
print("\n4. Iterating through the list:")
for item in my_list:
    print(item)

# 5. Find the product of all elements in a list using a for loop
my_list = [1, 2, 3, 4, 5]
product = 1
for num in my_list:
    product *= num
print("\n5. Product of all elements in the list:", product)

# 6. Print all even numbers from 1 to 20 using a for loop
print("\n6. Even numbers from 1 to 20:")
for i in range(2, 21, 2):
    print(i)

# 7. Calculate the factorial of a number using a for loop
num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("\n7. Factorial of", num, "is:", factorial)

# 8. Iterate through the characters of a string using a for loop
my_string = "Hello"
print("\n8. Characters in the string:")
for char in my_string:
    print(char)

# 9. Find the largest number in a list using a for loop
my_list = [10, 20, 30, 40, 50]
largest = my_list[0]
for num in my_list:
    if num > largest:
        largest = num
print("\n9. Largest number in the list:", largest)

# 10. Print Fibonacci sequence up to a specified limit using a for loop
limit = 10
a, b = 0, 1
print("\n10. Fibonacci sequence up to", limit, ":")
for _ in range(limit):
    print(a, end=" ")
    a, b = b, a + b

# 11. Count the number of vowels in a given string using a for loop
my_string = "Hello World"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in my_string:
    if char in vowels:
        vowel_count += 1
print("\n\n11. Number of vowels in the string:", vowel_count)

# 12. Generate a multiplication table for a given number using a for loop
num = 5
print("\n12. Multiplication table for", num, ":")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 13. Reverse a list using a for loop
my_list = [1, 2, 3, 4, 5]
reversed_list = []
for item in my_list:
    reversed_list.insert(0, item)
print("\n13. Reversed list:", reversed_list)

# 14. Find the common elements between two lists using a for loop
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = []
for item in list1:
    if item in list2:
        common_elements.append(item)
print("\n14. Common elements between the lists:", common_elements)

# 15. Iterate through the keys and values of a dictionary using a for loop
my_dict = {"a": 1, "b": 2, "c": 3}
print("\n15. Keys and values of the dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# 16. Find the GCD of two numbers using a for loop
num1 = 56
num2 = 98
gcd = 1
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print("\n16. GCD of", num1, "and", num2, "is:", gcd)

# 17. Check if a string is a palindrome using a for loop
my_string = "madam"
is_palindrome = True
for i in range(len(my_string) // 2):
    if my_string[i] != my_string[len(my_string) - i - 1]:
        is_palindrome = False
        break
print("\n17. Is the string a palindrome?", is_palindrome)

# 18. Remove duplicates from a list using a for loop
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = []
for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
print("\n18. List without duplicates:", unique_list)

# 19. Count the number of words in a sentence using a for loop
sentence = "This is a Python program."
words = sentence.split()
word_count = 0
for word in words:
    word_count += 1
print("\n19. Number of words in the sentence:", word_count)

# 20. Find the sum of all odd numbers from 1 to 50 using a for loop
odd_sum = 0
for i in range(1, 51, 2):
    odd_sum += i
print("\n20. Sum of odd numbers from 1 to 50:", odd_sum)

# 21. Check if a given year is a leap year using a for loop
year = 2024
is_leap = False
for i in range(1):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        is_leap = True
print("\n21. Is the year", year, "a leap year?", is_leap)

# 22. Calculate the square root of a number using a for loop
num = 16
square_root = num
for _ in range(10):
    square_root = (square_root + num / square_root) / 2
print("\n22. Square root of", num, "is approximately:", square_root)

# 23. Find the LCM of two numbers using a for loop
num1 = 12
num2 = 15
lcm = max(num1, num2)
while lcm % num1 != 0 or lcm % num2 != 0:
    lcm += 1
print("\n23. LCM of", num1, "and", num2, "is:", lcm)



If Else

# 1. Check if a number is positive, negative, or zero using an if-else statement
num = 10
if num > 0:
    print("1. The number is positive.")
elif num < 0:
    print("1. The number is negative.")
else:
    print("1. The number is zero.")

# 2. Check if a given number is even or odd using an if-else statement
num = 25
if num % 2 == 0:
    print("2. The number is even.")
else:
    print("2. The number is odd.")

# 3. Nested if-else example
age = 20
if age >= 18:
    if age >= 65:
        print("3. Senior citizen.")
    else:
        print("3. Adult.")
else:
    print("3. Minor.")

# 4. Determine the largest of three numbers using if-else
num1, num2, num3 = 10, 20, 15
if num1 >= num2 and num1 >= num3:
    print("4. The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("4. The largest number is:", num2)
else:
    print("4. The largest number is:", num3)

# 5. Calculate the absolute value of a number using if-else
num = -10
if num < 0:
    print("5. The absolute value is:", -num)
else:
    print("5. The absolute value is:", num)

# 6. Check if a given character is a vowel or consonant using if-else
char = 'a'
if char in 'aeiouAEIOU':
    print("6. The character is a vowel.")
else:
    print("6. The character is a consonant.")

# 7. Check if a user is eligible to vote based on their age using if-else
age = 18
if age >= 18:
    print("7. Eligible to vote.")
else:
    print("7. Not eligible to vote.")

# 8. Calculate the discount amount based on the purchase amount using if-else
purchase_amount = 150
if purchase_amount > 100:
    discount = 0.10 * purchase_amount
else:
    discount = 0
print("8. Discount amount:", discount)

# 9. Check if a number is within a specified range using if-else
num = 25
if 10 <= num <= 30:
    print("9. The number is within the range.")
else:
    print("9. The number is outside the range.")

# 10. Determine the grade of a student based on their score using if-else
score = 85
if score >= 90:
    grade = 'A'
elif score >= 75:
    grade = 'B'
elif score >= 60:
    grade = 'C'
else:
    grade = 'D'
print("10. The grade is:", grade)

# 11. Check if a string is empty or not using if-else
string = "Hello"
if string:
    print("11. The string is not empty.")
else:
    print("11. The string is empty.")

# 12. Identify the type of triangle based on input values using if-else
side1, side2, side3 = 5, 5, 5
if side1 == side2 == side3:
    print("12. The triangle is equilateral.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("12. The triangle is isosceles.")
else:
    print("12. The triangle is scalene.")

# 13. Determine the day of the week based on a user-provided number using if-else
day_number = 3
if day_number == 1:
    print("13. Monday")
elif day_number == 2:
    print("13. Tuesday")
elif day_number == 3:
    print("13. Wednesday")
elif day_number == 4:
    print("13. Thursday")
elif day_number == 5:
    print("13. Friday")
elif day_number == 6:
    print("13. Saturday")
elif day_number == 7:
    print("13. Sunday")
else:
    print("13. Invalid day number.")

# 14. Check if a given year is a leap year using both if-else and a function
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = 2024
print("14. Is the year", year, "a leap year?", is_leap_year(year))

# 15. Use the "assert" statement in Python to add debugging checks within if-else blocks
num = -5
assert num >= 0, "15. Number should be non-negative!"
print("15. The number is non-negative.")

# 16. Determine the eligibility of a person for a senior citizen discount based on age using if-else
age = 70
if age >= 65:
    print("16. Eligible for senior citizen discount.")
else:
    print("16. Not eligible for senior citizen discount.")

# 17. Categorize a given character as uppercase, lowercase, or neither using if-else
char = 'A'
if char.isupper():
    print("17. The character is uppercase.")
elif char.islower():
    print("17. The character is lowercase.")
else:
    print("17. The character is neither uppercase nor lowercase.")

# 18. Determine the roots of a quadratic equation using if-else
import math
a, b, c = 1, -7, 10
discriminant = b**2 - 4*a*c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"18. The roots are {root1} and {root2}.")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"18. The root is {root}.")
else:
    print("18. The equation has no real roots.")

# 19. Check if a given year is a century year or not using if-else
year = 2000
if year % 100 == 0:
    print(f"19. {year} is a century year.")
else:
    print(f"19. {year} is not a century year.")

# 20. Determine if a given number is a perfect square using if-else
num = 16
if math.isqrt(num) ** 2 == num:
    print(f"20. {num} is a perfect square.")
else:
    print(f"20. {num} is not a perfect square.")

# 21. Explain the purpose of the "continue" and "break" statements within if-else loops
# "continue": Skips the current iteration and moves to the next iteration.
# "break": Exits the loop entirely.

# 22. Calculate the BMI (Body Mass Index) of a person based on their weight and height using if-else
weight = 70  # kg
height = 1.75  # meters
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("22. BMI is underweight.")
elif bmi <= 24.9:
    print("22. BMI is normal.")
elif bmi <= 29.9:
    print("22. BMI is overweight.")
else:
    print("22. BMI is obese.")

# 23. Use the "filter()" function with if-else statements to filter elements from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("23. Even numbers from the list:", even_numbers)

# 24. Determine if a given number is prime or not using if-else
num = 29
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("24. The number is not prime.")
            break
    else:
        print("24. The number is prime.")
else:
    print("24. The number is not prime.")


Map

# 1. Explain the purpose of the `map()` function in Python and provide an example of how it can be used to apply a function to each element of an iterable.

# The `map()` function applies a given function to each item in an iterable (list, tuple, etc.) and returns a map object (iterator).
# This example squares each element of a list using map.

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print("Squared numbers:", list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

# 2. Write a Python program that uses the `map()` function to square each element of a list of numbers.

def square_number(x):
    return x * x

numbers_list = [10, 20, 30, 40]
squared_list = map(square_number, numbers_list)
print("Squared List:", list(squared_list))

# 3. How does the `map()` function differ from a list comprehension in Python, and when would you choose one over the other?

# - List comprehension is more concise and easier to read for simple transformations.
# - map() is useful when applying a function to an iterable without explicitly using a loop.

# Using map() function:
squared_map = map(lambda x: x * x, [2, 3, 4, 5])
print("Squared using map:", list(squared_map))

# Using list comprehension:
squared_comprehension = [x * x for x in [2, 3, 4, 5]]
print("Squared using list comprehension:", squared_comprehension)

# 4. Create a Python program that uses the `map()` function to convert a list of names to uppercase.

names = ["alice", "bob", "charlie"]
uppercase_names = map(lambda name: name.upper(), names)
print("Uppercase Names:", list(uppercase_names))

# 5. Write a Python program that uses the `map()` function to calculate the length of each word in a list of strings.

words = ["apple", "banana", "cherry"]
word_lengths = map(len, words)
print("Word Lengths:", list(word_lengths))

# 6. How can you use the `map()` function to apply a custom function to elements of multiple lists simultaneously in Python?

def add_elements(x, y):
    return x + y

list1 = [1, 2, 3]
list2 = [4, 5, 6]
added_elements = map(add_elements, list1, list2)
print("Added Elements from two lists:", list(added_elements))

# 7. Create a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius_temps = [0, 20, 40, 60]
fahrenheit_temps = map(celsius_to_fahrenheit, celsius_temps)
print("Fahrenheit Temperatures:", list(fahrenheit_temps))

# 8. Write a Python program that uses the `map()` function to round each element of a list of floating-point numbers to the nearest integer.

float_numbers = [1.5, 2.3, 3.7, 4.8]
rounded_numbers = map(round, float_numbers)
print("Rounded Numbers:", list(rounded_numbers))


Reduce

# You need to import reduce from the functools module to use it
from functools import reduce

# 1. What is the `reduce()` function in Python, and what module should you import to use it? Provide an example of its basic usage.

# The `reduce()` function in Python takes a function and an iterable and applies the function cumulatively to the items in the iterable.
# It reduces the iterable to a single value. You need to import it from the `functools` module.

# Example of `reduce()` usage:
numbers = [1, 2, 3, 4, 5]

# Using reduce to find the sum of the numbers
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print("Sum of numbers:", sum_of_numbers)  # Output: 15

# 2. Write a Python program that uses the `reduce()` function to find the product of all elements in a list.

numbers = [1, 2, 3, 4]

product_of_numbers = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product_of_numbers)  # Output: 24

# 3. Create a Python program that uses `reduce()` to find the maximum element in a list of numbers.

numbers = [3, 7, 2, 9, 5]

max_number = reduce(lambda x, y: x if x > y else y, numbers)
print("Maximum number:", max_number)  # Output: 9

# 4. How can you use the `reduce()` function to concatenate a list of strings into a single string?

strings = ["Hello", "world", "from", "Python"]

concatenated_string = reduce(lambda x, y: x + " " + y, strings)
print("Concatenated string:", concatenated_string)  # Output: "Hello world from Python"

# 5. Write a Python program that calculates the factorial of a number using the `reduce()` function.

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

number = 5
factorial_result = factorial(number)
print(f"Factorial of {number}:", factorial_result)  # Output: 120

# 6. Create a Python program that uses `reduce()` to find the GCD (Greatest Common Divisor) of a list of numbers.

import math

numbers = [24, 36, 60]

gcd_of_numbers = reduce(math.gcd, numbers)
print("GCD of numbers:", gcd_of_numbers)  # Output: 12

# 7. Write a Python program that uses the `reduce()` function to find the sum of the digits of a given number.

number = 12345

# Convert the number to a list of digits
digits = [int(digit) for digit in str(number)]

sum_of_digits = reduce(lambda x, y: x + y, digits)
print(f"Sum of digits of {number}:", sum_of_digits)  # Output: 15


Filter

# 1. Explain the purpose of the `filter()` function in Python and provide an example of how it can be used to filter elements from an iterable.

# The `filter()` function in Python is used to filter elements from an iterable (such as a list, tuple, or string) based on a condition. 
# It returns an iterator that yields only the elements that satisfy the condition specified in the given function.

# Example: Using `filter()` to select even numbers from a list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers:", list(even_numbers))  # Output: [2, 4, 6, 8, 10]

# 2. Write a Python program that uses the `filter()` function to select even numbers from a list of integers.

numbers = [10, 15, 23, 42, 56, 78, 99, 100]

even_numbers = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers:", list(even_numbers))  # Output: [10, 42, 56, 78, 100]

# 3. Create a Python program that uses the `filter()` function to select names that start with a specific letter from a list of strings.

names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Select names that start with 'A'
names_starting_with_A = filter(lambda name: name.startswith('A'), names)
print("Names starting with 'A':", list(names_starting_with_A))  # Output: ['Alice']

# 4. Write a Python program that uses the `filter()` function to select prime numbers from a list of integers.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

prime_numbers = filter(is_prime, numbers)
print("Prime numbers:", list(prime_numbers))  # Output: [2, 3, 5, 7, 11, 13]

# 5. How can you use the `filter()` function to remove None values from a list in Python?

data = [1, None, "Hello", None, 3.14, None, "World"]

# Filter out None values
filtered_data = filter(lambda x: x is not None, data)
print("Filtered data (without None values):", list(filtered_data))  # Output: [1, 'Hello', 3.14, 'World']

# 6. Create a Python program that uses `filter()` to select words longer than a certain length from a list of strings.

words = ["apple", "banana", "cherry", "date", "elderberry"]

# Select words longer than 5 characters
long_words = filter(lambda word: len(word) > 5, words)
print("Words longer than 5 characters:", list(long_words))  # Output: ['banana', 'cherry', 'elderberry']

# 7. Write a Python program that uses the `filter()` function to select elements greater than a specified threshold from a list of values.

values = [10, 20, 30, 40, 50, 60]

# Select values greater than 30
greater_than_30 = filter(lambda x: x > 30, values)
print("Values greater than 30:", list(greater_than_30))  # Output: [40, 50, 60]


Recursion


# 1. Explain the concept of recursion in Python. How does it differ from iteration?

# Recursion in Python is a process where a function calls itself directly or indirectly to solve a problem. 
# A recursive function repeats its calls to break down a problem into smaller sub-problems. 
# It differs from iteration (using loops) because iteration repeats a set of instructions a fixed number of times, 
# whereas recursion breaks down the problem and solves smaller instances of it until a base case is met.

# Recursion Example Problems:

# 2. Write a Python program to calculate the factorial of a number using recursion.

def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test
print("Factorial of 5:", factorial(5))  # Output: 120


# 3. Create a recursive Python function to find the nth Fibonacci number.

def fibonacci(n):
    # Base case: the first two Fibonacci numbers are 0 and 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test
print("Fibonacci of 6:", fibonacci(6))  # Output: 8


# 4. Write a recursive Python function to calculate the sum of all elements in a list.

def sum_list(lst):
    # Base case: if the list is empty, return 0
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

# Test
print("Sum of list [1, 2, 3, 4]:", sum_list([1, 2, 3, 4]))  # Output: 10


# 5. How can you prevent a recursive function from running indefinitely, causing a stack overflow error?

# To prevent a recursive function from running indefinitely, we must have a base case. The base case will stop 
# the recursion once a certain condition is met. Without a base case, the function will keep calling itself 
# leading to a stack overflow.

# Example with a base case:
def safe_recursion(n):
    # Base case to stop the recursion
    if n == 0:
        return "Done"
    else:
        return safe_recursion(n - 1)

# Test
print(safe_recursion(5))  # Output: Done


# 6. Create a recursive Python function to find the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

def gcd(a, b):
    # Base case: if b is 0, return a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Test
print("GCD of 56 and 98:", gcd(56, 98))  # Output: 14


# 7. Write a recursive Python function to reverse a string.

def reverse_string(s):
    # Base case: if the string is empty or has one character, return the string itself
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

# Test
print("Reversed string of 'hello':", reverse_string("hello"))  # Output: 'olleh'


# 8. Create a recursive Python function to calculate the power of a number (x^n).

def power(x, n):
    # Base case: if n is 0, return 1 (any number raised to the power of 0 is 1)
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

# Test
print("3^4:", power(3, 4))  # Output: 81


# 9. Write a recursive Python function to find all permutations of a given string.

def permutations(s):
    # Base case: if the string is empty, return a list with the empty string
    if len(s) == 0:
        return [""]
    else:
        perm_list = []
        for i in range(len(s)):
            part = s[:i] + s[i+1:]
            for j in permutations(part):
                perm_list.append(s[i] + j)
        return perm_list

# Test
print("Permutations of 'abc':", permutations("abc"))  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


# 10. Write a recursive Python function to check if a string is a palindrome.

def is_palindrome(s):
    # Base case: if the string is of length 0 or 1, it's a palindrome
    if len(s) <= 1:
        return True
    else:
        # Check if first and last characters are the same
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])  # Check the substring without first and last character
        else:
            return False

# Test
print("Is 'racecar' a palindrome?", is_palindrome("racecar"))  # Output: True


# 11. Create a recursive Python function to generate all possible combinations of a list of elements.

def combinations(lst):
    # Base case: if the list is empty, return an empty list of combinations
    if len(lst) == 0:
        return [[]]
    else:
        first = lst[0]
        rest = combinations(lst[1:])
        comb_with_first = [[first] + comb for comb in rest]
        comb_without_first = rest
        return comb_with_first + comb_without_first

# Test
print("Combinations of [1, 2, 3]:", combinations([1, 2, 3]))  # Output: [ [1, 2, 3], [1, 2], [1, 3], [1], [2, 3], [2], [3], [] ]


Basics of Functions:

# 1. What is a function in Python, and why is it used?

# A function in Python is a block of code that only runs when it is called. Functions allow us to organize code, 
# avoid repetition, and make programs more modular. By defining a function, we can reuse the same code in different places.
# Functions can accept inputs (parameters), process them, and return outputs (values).

# Example:
def greet():
    print("Hello, World!")

greet()  # Output: Hello, World! 

# A function is used for better organization of code, improving readability, and reducing redundancy.


# 2. How do you define a function in Python? Provide an example.

# Functions in Python are defined using the `def` keyword, followed by the function name, and a pair of parentheses (optional).
# The function body starts after a colon and is indented.

# Example of defining a function:
def add_two_numbers(a, b):
    return a + b

# Function call:
result = add_two_numbers(3, 4)  # Passing 3 and 4 as arguments to the function
print("Sum:", result)  # Output: Sum: 7


# 3. Explain the difference between a function definition and a function call.

# - **Function definition** is the process of defining a function. It defines the function's name, 
#   parameters, and the block of code that executes when the function is called.
# - **Function call** is the process of invoking a function to execute the code within it, passing arguments (if any) 
#   and getting the return value (if any).

# Function definition:
def multiply(x, y):
    return x * y

# Function call:
result = multiply(2, 3)  # We call the function `multiply` with 2 and 3 as arguments.

# The function is now executed, and we get the result (6) as the output.


# 4. Write a Python program that defines a function to calculate the sum of two numbers and then calls the function.

def sum_of_two_numbers(num1, num2):
    return num1 + num2

# Function call
result = sum_of_two_numbers(10, 20)
print("The sum is:", result)  # Output: The sum is: 30


# 5. What is a function signature, and what information does it typically include?

# A function signature in Python consists of the function's name, parameter names, and their types (if applicable).
# The function signature gives an overview of how the function should be called (i.e., what parameters it expects).
# The function signature also defines the function's return type, although Python does not enforce return type annotations.

# Example:
def subtract(x: int, y: int) -> int:  # This is the function signature
    return x - y

# Here, `subtract` is the function name, `(x: int, y: int)` indicates it accepts two integers, 
# and `-> int` means it returns an integer.

result = subtract(15, 5)
print("The result of subtraction is:", result)  # Output: The result of subtraction is: 10


# 6. Create a Python function that takes two arguments and returns their product.

def product_of_two(a, b):
    return a * b

# Function call
result = product_of_two(6, 7)
print("The product is:", result)  # Output: The product is: 42


Function Parameters and Arguments:

# 1. Explain the concepts of formal parameters and actual arguments in Python functions.

# - **Formal parameters** are the variables that are defined in the function definition. 
#   They act as placeholders for the values that will be passed to the function when it is called.
# - **Actual arguments** (or simply arguments) are the values or expressions passed to the function when it is called. 
#   These values are assigned to the corresponding formal parameters.

# Example of function with formal parameters and actual arguments:
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Function call with actual arguments
greet("Alice", 30)  # "Alice" and 30 are actual arguments passed to the function
# Output: Hello, Alice! You are 30 years old.


# 2. Write a Python program that defines a function with default argument values.

def greet(name="Guest", age=18):
    print(f"Hello, {name}! You are {age} years old.")

# Function call without arguments
greet()  # Will use default values
# Output: Hello, Guest! You are 18 years old.

# Function call with one argument
greet("Bob")  # Will use default value for 'age'
# Output: Hello, Bob! You are 18 years old.

# Function call with both arguments
greet("Charlie", 25)  # Will use provided values for both 'name' and 'age'
# Output: Hello, Charlie! You are 25 years old.


# 3. How do you use keyword arguments in Python function calls? Provide an example.

# **Keyword arguments** allow passing arguments by explicitly specifying the parameter name during the function call. 
# This can make the function calls more readable and allows the caller to pass arguments in any order.

def introduce(name, age, country):
    print(f"My name is {name}, I am {age} years old, and I live in {country}.")

# Function call using keyword arguments
introduce(age=30, name="John", country="USA")
# Output: My name is John, I am 30 years old, and I live in USA.

# The order of arguments doesn't matter when using keyword arguments.


# 4. Create a Python function that accepts a variable number of arguments and calculates their sum.

def calculate_sum(*args):
    total = sum(args)
    print(f"The sum is: {total}")

# Function call with a variable number of arguments
calculate_sum(1, 2, 3)  # Output: The sum is: 6
calculate_sum(5, 10, 15, 20)  # Output: The sum is: 50
calculate_sum(7)  # Output: The sum is: 7


# 5. What is the purpose of the `*args` and `**kwargs` syntax in function parameter lists?

# - `*args`: It allows a function to accept a variable number of positional arguments. The arguments are captured 
#   as a tuple inside the function.
# - `**kwargs`: It allows a function to accept a variable number of keyword arguments. These arguments are captured 
#   as a dictionary inside the function.

# Example of using *args and **kwargs:
def display_info(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

# Function call with both *args and **kwargs
display_info(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments (args): (1, 2, 3)
# Keyword arguments (kwargs): {'name': 'Alice', 'age': 25}

# Here, 1, 2, and 3 are passed as positional arguments (captured in 'args') 
# and name="Alice" and age=25 are passed as keyword arguments (captured in 'kwargs').




Return Values and Scoping:



# 1. Describe the role of the `return` statement in Python functions and provide examples.

# The `return` statement is used to exit a function and return a value to the caller. 
# When a function encounters the `return` statement, it immediately stops executing and sends the returned value 
# to the location where the function was called. If no `return` statement is provided, the function returns `None` by default.

def add_numbers(a, b):
    return a + b  # Return the sum of a and b

result = add_numbers(5, 10)
print(f"The sum is: {result}")  # Output: The sum is: 15

# Example of a function with no return
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
# This function does not return any value, it just prints a greeting message.


# 2. Explain the concept of variable scope in Python, including local and global variables.

# - **Local variables** are variables defined within a function and can only be used inside that function.
# - **Global variables** are variables defined outside of any function and can be accessed by any function in the script.

# Example of local and global variables
x = 10  # Global variable

def example_function():
    y = 5  # Local variable
    print(f"Local variable y: {y}")
    print(f"Global variable x: {x}")  # Accessing global variable

example_function()
# Output:
# Local variable y: 5
# Global variable x: 10


# 3. Write a Python program that demonstrates the use of global variables within functions.

# We can modify a global variable inside a function using the `global` keyword.
x = 10  # Global variable

def modify_global():
    global x  # Declare the intention to modify the global variable
    x = 20  # Modify the global variable

print(f"Before modification: x = {x}")
modify_global()
print(f"After modification: x = {x}")
# Output:
# Before modification: x = 10
# After modification: x = 20


# 4. Create a Python function that calculates the factorial of a number and returns it.

def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call

result = factorial(5)
print(f"The factorial of 5 is: {result}")  # Output: The factorial of 5 is: 120


# 5. How can you access variables defined outside a function from within the function?

# - **Global variables** can be accessed inside a function without any special declaration.
# - If you want to modify a global variable inside a function, you need to use the `global` keyword.

def access_global():
    print(f"Accessing global variable x: {x}")

access_global()  # Output: Accessing global variable x: 10

# If you want to modify the global variable x, use the `global` keyword:
def modify_global_variable():
    global x
    x = 50  # Modify global variable

modify_global_variable()
print(f"Modified global variable x: {x}")  # Output: Modified global variable x: 50



Lambda Functions and Higher-Order Functions:

# Lambda Functions in Python

# A simple lambda function that adds 10 to the given number
add_10 = lambda x: x + 10
print(add_10(5))  # Output: 15


# Lambda Functions to Sort a List of Tuples Based on the Second Element

# List of tuples
tuples = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]

# Sort by the second element (index 1) using a lambda function
sorted_tuples = sorted(tuples, key=lambda x: x[1])

print(f"Sorted tuples by second element: {sorted_tuples}")
# Output: Sorted tuples by second element: [(1, 'apple'), (3, 'banana'), (2, 'cherry')]


# Higher-Order Functions in Python

# A higher-order function that takes a function as argument and applies it to a list
def apply_function_to_list(func, data):
    return [func(x) for x in data]

# A simple function to square a number
def square(x):
    return x * x

# Using the higher-order function to apply 'square' to each element in the list
numbers = [1, 2, 3, 4, 5]
squared_numbers = apply_function_to_list(square, numbers)

print(f"Squared numbers: {squared_numbers}")
# Output: Squared numbers: [1, 4, 9, 16, 25]


# Python Function that Takes a List and a Function as Arguments

# Function that applies a given function to each element of a list
def apply_function_to_elements(func, elements):
    return [func(element) for element in elements]

# A simple lambda function to double a number
double = lambda x: x * 2

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Apply the 'double' lambda function to the list
doubled_numbers = apply_function_to_elements(double, numbers)

print(f"Doubled numbers: {doubled_numbers}")
# Output: Doubled numbers: [2, 4, 6, 8, 10]




# Built-in Functions: len(), max(), min()
print("1. Built-in Functions: len(), max(), min()")
numbers = [4, 1, 9, 7, 5]

# len() - Returns the number of elements in the list
print(f"Length of the list: {len(numbers)}")  # Output: 5

# max() - Returns the maximum value from the list
print(f"Maximum value in the list: {max(numbers)}")  # Output: 9

# min() - Returns the minimum value from the list
print(f"Minimum value in the list: {min(numbers)}")  # Output: 1


# map() Function - Apply a function to each element in a list
print("\n2. map() Function - Apply a function to each element in a list")
# Function that squares a number
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

# Use map() to apply square function to each element
squared_numbers = list(map(square, numbers))
print(f"Squared numbers: {squared_numbers}")  # Output: [1, 4, 9, 16, 25]


# filter() Function - Filter elements from a list
print("\n3. filter() Function - Filter elements from a list")
# Function to check if the number is even
def is_even(x):
    return x % 2 == 0

# Use filter() to get even numbers from the list
even_numbers = list(filter(is_even, numbers))
print(f"Even numbers: {even_numbers}")  # Output: [2, 4]


# reduce() Function - Accumulate results of applying a function on elements in a list
from functools import reduce

print("\n4. reduce() Function - Find the product of all elements in a list")
# Function to multiply two numbers
def product(x, y):
    return x * y

# Use reduce() to find the product of all numbers
product_of_all = reduce(product, numbers)
print(f"Product of all numbers: {product_of_all}")  # Output: 120






Explain the purpose of docstrings in Python functions and how to write them.


Answer

Docstrings in Python are special string literals used to document Python functions, methods, classes, and modules. They provide a convenient way of associating a description with a function to explain its behavior, parameters, return values, and any additional important information. Docstrings are helpful for users or other developers who may use or maintain the code in the future.

A docstring is written immediately following the def line of a function (or method, class, or module). It is enclosed in triple quotes (""" or ''') so that it can span multiple lines.



Describe some best practices for naming functions and variables in Python, including naming conventions and guidelines.


# Constants should be in uppercase with underscores separating words.
MAX_ITEMS_PER_ORDER = 10
DISCOUNT_RATE = 0.15

# Function that calculates the total price of items in the cart.
def calculate_total_price(items):
    """
    Calculates the total price of all items in the list.
    Arguments:
    - items: List of Item objects.
    Returns:
    - float: Total price.
    """
    total_price = 0
    for item in items:
        total_price += item.price
    return total_price

# Function that checks if a user is eligible for a discount.
def is_eligible_for_discount(user, total_price):
    """
    Checks if the user is eligible for a discount.
    Arguments:
    - user: User object containing user details.
    - total_price: Total price of items.
    Returns:
    - bool: True if eligible, False otherwise.
    """
    if user.is_vip or total_price > 100:
        return True
    return False

# Function to apply discount on total price if eligible.
def apply_discount(total_price, discount_rate):
    """
    Applies discount on the total price if the user is eligible.
    Arguments:
    - total_price: Original price before discount.
    - discount_rate: Discount rate (0.15 for 15% off).
    Returns:
    - float: Discounted price.
    """
    return total_price * (1 - discount_rate)

# Sample classes to demonstrate naming conventions.

class User:
    """
    User class with attributes such as name and VIP status.
    """
    def __init__(self, name, age, is_vip=False):
        self.name = name
        self.age = age
        self.is_vip = is_vip

    def __repr__(self):
        return f"User(name={self.name}, age={self.age}, is_vip={self.is_vip})"

class Item:
    """
    Item class with attributes for item name and price.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Item(name={self.name}, price={self.price})"


# Example usage
if __name__ == "__main__":
    # Create some items and a user.
    apple = Item("Apple", 2.0)
    banana = Item("Banana", 1.5)
    user = User("John Doe", 28, is_vip=True)

    items_in_cart = [apple, banana]

    # Calculate total price.
    total_price = calculate_total_price(items_in_cart)

    # Check if the user is eligible for discount.
    if is_eligible_for_discount(user, total_price):
        total_price = apply_discount(total_price, DISCOUNT_RATE)

    print(f"Total price for {user.name}: ${total_price:.2f}")
