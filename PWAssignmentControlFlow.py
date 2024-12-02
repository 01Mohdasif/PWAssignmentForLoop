Basic If-Else Statements

# 1. Check if a given number is positive or negative.
def check_positive_negative(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example Output:
print(check_positive_negative(5))  # Positive

# 2. Determine if a person is eligible to vote based on their age.
def is_eligible_to_vote(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

# Example Output:
print(is_eligible_to_vote(20))  # Eligible to vote

# 3. Find the maximum of two numbers.
def max_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Example Output:
print(max_of_two(4, 7))  # 7

# 4. Classify a given year as a leap year or not.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

# Example Output:
print(is_leap_year(2020))  # Leap Year

# 5. Check whether a character is a vowel or a consonant.
def check_vowel_consonant(char):
    vowels = "aeiou"
    if char.lower() in vowels:
        return "Vowel"
    else:
        return "Consonant"

# Example Output:
print(check_vowel_consonant('A'))  # Vowel

# 6. Determine whether a number is even or odd.
def is_even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example Output:
print(is_even_or_odd(3))  # Odd

# 7. Calculate the absolute value of a number without using `abs()` function.
def absolute_value(num):
    if num < 0:
        return -num
    else:
        return num

# Example Output:
print(absolute_value(-10))  # 10

# 8. Determine the largest of three given numbers.
def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Example Output:
print(max_of_three(3, 5, 2))  # 5

# 9. Check if a given string is a palindrome.
def is_palindrome(string):
    if string == string[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

# Example Output:
print(is_palindrome("racecar"))  # Palindrome

# 10. Calculate the grade based on a student's score.
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Example Output:
print(calculate_grade(85))  # B


Nested If-Else Statements


# 11. Find the largest among three numbers using nested if-else.
def largest_of_three(num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            return num1
        else:
            return num3
    else:
        if num2 >= num3:
            return num2
        else:
            return num3

# Example Output:
print(largest_of_three(5, 7, 3))  # 7

# 12. Determine if a triangle is equilateral, isosceles, or scalene.
def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Example Output:
print(triangle_type(3, 3, 5))  # Isosceles

# 13. Check if a year is a leap year and also if it is a century year.
def is_century_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Century Leap Year"
            else:
                return "Century Not Leap Year"
        else:
            return "Leap Year"
    else:
        return "Not a Leap Year"

# Example Output:
print(is_century_leap_year(2000))  # Century Leap Year

# 14. Determine if a number is positive, negative, or zero.
def number_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example Output:
print(number_sign(-5))  # Negative

# 15. Check if a person is a teenager (between 13 and 19 years old).
def is_teenager(age):
    if 13 <= age <= 19:
        return "Teenager"
    else:
        return "Not a Teenager"

# Example Output:
print(is_teenager(16))  # Teenager

# 16. Determine the type of angle based on its measure.
def angle_type(angle):
    if angle < 90:
        return "Acute"
    elif angle == 90:
        return "Right"
    else:
        return "Obtuse"

# Example Output:
print(angle_type(45))  # Acute

# 17. Calculate the roots of a quadratic equation.
import math
def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return "No Real Roots"

# Example Output:
print(quadratic_roots(1, -3, 2))  # (2.0, 1.0)

# 18. Determine the day of the week based on a number.
def day_of_week(num):
    if num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    elif num == 7:
        return "Sunday"
    else:
        return "Invalid Day Number"

# Example Output:
print(day_of_week(3))  # Wednesday

# 19. Check if a year is a leap year and if it's divisible by 400.
def leap_and_century(year):
    if year % 400 == 0:
        return "Leap Year and Divisible by 400"
    elif year % 4 == 0 and year % 100 != 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"

# Example Output:
print(leap_and_century(2000))  # Leap Year and Divisible by 400

# 20. Check if a number is prime.
def is_prime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return "Not Prime"
        return "Prime"
    else:
        return "Not Prime"

# Example Output:
print(is_prime(7))  # Prime



Here are Python solutions for the Basic If-Else Statements, Nested If-Else Statements, and Elif Statements practice problems:

Basic If-Else Statements
python
Copy code
# 1. Check if a given number is positive or negative.
def check_positive_negative(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example Output:
print(check_positive_negative(5))  # Positive

# 2. Determine if a person is eligible to vote based on their age.
def is_eligible_to_vote(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

# Example Output:
print(is_eligible_to_vote(20))  # Eligible to vote

# 3. Find the maximum of two numbers.
def max_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Example Output:
print(max_of_two(4, 7))  # 7

# 4. Classify a given year as a leap year or not.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

# Example Output:
print(is_leap_year(2020))  # Leap Year

# 5. Check whether a character is a vowel or a consonant.
def check_vowel_consonant(char):
    vowels = "aeiou"
    if char.lower() in vowels:
        return "Vowel"
    else:
        return "Consonant"

# Example Output:
print(check_vowel_consonant('A'))  # Vowel

# 6. Determine whether a number is even or odd.
def is_even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example Output:
print(is_even_or_odd(3))  # Odd

# 7. Calculate the absolute value of a number without using `abs()` function.
def absolute_value(num):
    if num < 0:
        return -num
    else:
        return num

# Example Output:
print(absolute_value(-10))  # 10

# 8. Determine the largest of three given numbers.
def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Example Output:
print(max_of_three(3, 5, 2))  # 5

# 9. Check if a given string is a palindrome.
def is_palindrome(string):
    if string == string[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

# Example Output:
print(is_palindrome("racecar"))  # Palindrome

# 10. Calculate the grade based on a student's score.
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Example Output:
print(calculate_grade(85))  # B
Nested If-Else Statements
python
Copy code
# 11. Find the largest among three numbers using nested if-else.
def largest_of_three(num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            return num1
        else:
            return num3
    else:
        if num2 >= num3:
            return num2
        else:
            return num3

# Example Output:
print(largest_of_three(5, 7, 3))  # 7

# 12. Determine if a triangle is equilateral, isosceles, or scalene.
def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Example Output:
print(triangle_type(3, 3, 5))  # Isosceles

# 13. Check if a year is a leap year and also if it is a century year.
def is_century_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Century Leap Year"
            else:
                return "Century Not Leap Year"
        else:
            return "Leap Year"
    else:
        return "Not a Leap Year"

# Example Output:
print(is_century_leap_year(2000))  # Century Leap Year

# 14. Determine if a number is positive, negative, or zero.
def number_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example Output:
print(number_sign(-5))  # Negative

# 15. Check if a person is a teenager (between 13 and 19 years old).
def is_teenager(age):
    if 13 <= age <= 19:
        return "Teenager"
    else:
        return "Not a Teenager"

# Example Output:
print(is_teenager(16))  # Teenager

# 16. Determine the type of angle based on its measure.
def angle_type(angle):
    if angle < 90:
        return "Acute"
    elif angle == 90:
        return "Right"
    else:
        return "Obtuse"

# Example Output:
print(angle_type(45))  # Acute

# 17. Calculate the roots of a quadratic equation.
import math
def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return "No Real Roots"

# Example Output:
print(quadratic_roots(1, -3, 2))  # (2.0, 1.0)

# 18. Determine the day of the week based on a number.
def day_of_week(num):
    if num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    elif num == 7:
        return "Sunday"
    else:
        return "Invalid Day Number"

# Example Output:
print(day_of_week(3))  # Wednesday

# 19. Check if a year is a leap year and if it's divisible by 400.
def leap_and_century(year):
    if year % 400 == 0:
        return "Leap Year and Divisible by 400"
    elif year % 4 == 0 and year % 100 != 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"

# Example Output:
print(leap_and_century(2000))  # Leap Year and Divisible by 400

# 20. Check if a number is prime.
def is_prime(num):
    if num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return "Not Prime"
        return "Prime"
    else:
        return "Not Prime"

# Example Output:
print(is_prime(7))  # Prime


Elif Statements

# 21. Assign grades based on different ranges of scores.
def assign_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Example Output:
print(assign_grade(85))  # B

# 22. Determine the type of a triangle based on its angles.
def triangle_by_angle(angle1, angle2, angle3):
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        return "Right Triangle"
    elif angle1 < 90 and angle2 < 90 and angle3 < 90:
        return "Acute Triangle"
    else:
        return "Obtuse Triangle"

# Example Output:
print(triangle_by_angle(60, 60, 60))  # Acute Triangle

# 23. Categorize a given person's BMI into underweight, normal, overweight, or obese.
def bmi_category(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Example Output:
print(bmi_category(70, 1.75))  # Normal

# 24. Determine if a number is positive, negative, or zero.
def check_number_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example Output:
print(check_number_sign(-10))  # Negative

# 25. Determine the type of a character.
def char_type(char):
    if char.isupper():
        return "Uppercase"
    elif char.islower():
        return "Lowercase"
    else:
        return "Special Character"

# Example Output:
print(char_type('A'))  # Uppercase

# 26. Calculate the discounted price based on different purchase amounts.
def discounted_price(amount):
    if amount >= 1000:
        return amount * 0.9
    elif amount >= 500:
        return amount * 0.95
    else:
        return amount

# Example Output:
print(discounted_price(1200))  # 1080.0

# 27. Calculate the electricity bill based on consumption slabs.
def electricity_bill(consumption):
    if consumption <= 100:
        return consumption * 5
    elif consumption <= 300:
        return consumption * 7
    else:
        return consumption * 10

# Example Output:
print(electricity_bill(250))  # 1750

# 28. Determine the type of quadrilateral.
def quadrilateral_type(a, b, c, d):
    if a == b == c == d:
        return "Square"
    elif a == c and b == d:
        return "Rectangle"
    else:
        return "Other Quadrilateral"

# Example Output:
print(quadrilateral_type(4, 4, 4, 4))  # Square

# 29. Determine the season based on a user-provided month.
def season_of_month(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    else:
        return "Autumn"

# Example Output:
print(season_of_month(5))  # Spring

# 30. Determine the type of a year and month.
def year_month_type(year, month):
    if year % 4 == 0:
        if month == 2:
            if year % 100 == 0 and year % 400 != 0:
                return "28 Days (Common Year)"
            else:
                return "29 Days (Leap Year)"
        elif month in [4, 6, 9, 11]:
            return "30 Days"
        else:
            return "31 Days"
    else:
        if month == 2:
            return "28 Days (Common Year)"
        elif month in [4, 6, 9, 11]:
            return "30 Days"
        else:
            return "31 Days"

# Example Output:
print(year_month_type(2024, 2))  # 29 Days (Leap Year)



# 1. Check if a given number is positive, negative, or zero.
def check_number_sign(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Example Output:
print(check_number_sign(5))  # Positive
print(check_number_sign(-3))  # Negative
print(check_number_sign(0))  # Zero


# 2. Determine if a person is eligible to vote based on their age.
def is_eligible_to_vote(age):
    if age >= 18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"

# Example Output:
print(is_eligible_to_vote(20))  # Eligible to vote
print(is_eligible_to_vote(17))  # Not eligible to vote


# 3. Find the maximum of two given numbers using conditional statements.
def max_of_two(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Example Output:
print(max_of_two(10, 15))  # 15


# 4. Calculate the grade of a student based on their exam score.
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Example Output:
print(calculate_grade(85))  # B


# 5. Check if a year is a leap year or not.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

# Example Output:
print(is_leap_year(2020))  # Leap Year
print(is_leap_year(2021))  # Not a Leap Year


# 6. Classify a triangle based on its sides' lengths.
def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Example Output:
print(triangle_type(3, 3, 3))  # Equilateral
print(triangle_type(3, 4, 3))  # Isosceles
print(triangle_type(3, 4, 5))  # Scalene


# 7. Determine the largest of three given numbers.
def largest_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Example Output:
print(largest_of_three(5, 10, 3))  # 10


# 8. Check whether a character is a vowel or a consonant.
def check_vowel_consonant(char):
    if char.lower() in 'aeiou':
        return "Vowel"
    else:
        return "Consonant"

# Example Output:
print(check_vowel_consonant('A'))  # Vowel
print(check_vowel_consonant('b'))  # Consonant


# 9. Calculate the total cost of a shopping cart based on discounts.
def calculate_total_cost(cart_total):
    if cart_total >= 100:
        return cart_total * 0.9
    elif cart_total >= 50:
        return cart_total * 0.95
    else:
        return cart_total

# Example Output:
print(calculate_total_cost(120))  # 108.0
print(calculate_total_cost(60))   # 57.0
print(calculate_total_cost(30))   # 30.0


# 10. Check if a given number is even or odd.
def is_even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Example Output:
print(is_even_or_odd(4))  # Even
print(is_even_or_odd(7))  # Odd


# 11. Calculate the roots of a quadratic equation.
import math
def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root
    else:
        return "No Real Roots"

# Example Output:
print(quadratic_roots(1, -3, 2))  # (2.0, 1.0)


# 12. Determine the day of the week based on the day number (1-7).
def day_of_week(num):
    if num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    elif num == 7:
        return "Sunday"
    else:
        return "Invalid Day Number"

# Example Output:
print(day_of_week(3))  # Wednesday
print(day_of_week(6))  # Saturday


# 13. Calculate the factorial of a given number using recursion.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example Output:
print(factorial(5))  # 120


# 14. Find the largest among three numbers without using the `max()` function.
def largest_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Example Output:
print(largest_of_three(7, 2, 5))  # 7


# 15. Simulate a basic ATM transaction menu.
def atm_transaction(balance):
    print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        return f"Deposited {amount}. New balance: {balance}"
    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            return f"Withdrew {amount}. New balance: {balance}"
        else:
            return "Insufficient balance"
    elif choice == 3:
        return f"Current balance: {balance}"
    elif choice == 4:
        return "Exiting..."
    else:
        return "Invalid choice"

# Example Output:
print(atm_transaction(1000))


# 16. Check if a given string is a palindrome or not.
def is_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

# Example Output:
print(is_palindrome("madam"))  # Palindrome
print(is_palindrome("hello"))  # Not a Palindrome


# 17. Calculate the average of a list of numbers, excluding the smallest and largest values.
def average_excluding_extremes(numbers):
    numbers.sort()
    numbers = numbers[1:-1]
    return sum(numbers) / len(numbers)

# Example Output:
print(average_excluding_extremes([1, 2, 3, 4, 5]))  # 3.0


# 18. Convert a given temperature from Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example Output:
print(celsius_to_fahrenheit(0))  # 32.0


# 19. Simulate a basic calculator for addition, subtraction, multiplication, and division.
def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")
    
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        return "Invalid operation"

# Example Output:
print(calculator())


# 21. Calculate the income tax based on the user's income and tax brackets.
def calculate_tax(income):
    if income <= 10000:
        return income * 0.1
    elif income <= 20000:
        return income * 0.2
    else:
        return income * 0.3

# Example Output:
print(calculate_tax(15000))  # 3000


# 22. Simulate a rock-paper-scissors game against the computer.
import random
def rock_paper_scissors(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    if player_choice == computer_choice:
        return f"Tie! Both chose {player_choice}"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return f"You win! {player_choice} beats {computer_choice}"
    else:
        return f"You lose! {computer_choice} beats {player_choice}"

# Example Output:
print(rock_paper_scissors("rock"))  # Output depends on the computer's random choice


# 23. Generate a random password based on user preferences (length, complexity).
import random
import string
def generate_password(length=8, complexity=2):
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Example Output:
print(generate_password(10, 3))  # Randomly generated complex password


# 24. Implement a simple text-based adventure game with branching scenarios.
def adventure_game():
    print("You are standing at a crossroads. Do you want to go left or right?")
    choice = input("Enter 'left' or 'right': ")
    if choice.lower() == "left":
        print("You walk into a dark forest and find a treasure chest!")
    elif choice.lower() == "right":
        print("You walk into a sunny meadow and find a peaceful stream.")
    else:
        print("Invalid choice! Please enter 'left' or 'right'.")

# Example Output:
adventure_game()


# 25. Solve a linear equation for x: ax + b = 0
def solve_linear_equation(a, b):
    if a == 0:
        return "No solution" if b != 0 else "Infinite solutions"
    else:
        return -b / a

# Example Output:
print(solve_linear_equation(2, -4))  # 2.0


# 26. Write a program that simulates a basic quiz game with multiple-choice questions and scoring.

def quiz_game():
    score = 0
    print("Welcome to the quiz game!")
    
    # Question 1
    print("1. What is the capital of France?")
    print("a) Berlin\nb) Madrid\nc) Paris\nd) Rome")
    answer1 = input("Your answer: ").lower()
    if answer1 == "c":
        score += 1
    
    # Question 2
    print("\n2. Who wrote 'Romeo and Juliet'?")
    print("a) William Shakespeare\nb) Charles Dickens\nc) Jane Austen\nd) Mark Twain")
    answer2 = input("Your answer: ").lower()
    if answer2 == "a":
        score += 1
    
    # Question 3
    print("\n3. What is the largest planet in our solar system?")
    print("a) Earth\nb) Mars\nc) Jupiter\nd) Saturn")
    answer3 = input("Your answer: ").lower()
    if answer3 == "c":
        score += 1
    
    # Display final score
    print(f"\nYour final score is: {score} out of 3")

# 27. Develop a program that determines whether a given year is a prime number or not.

def is_prime(year):
    if year < 2:
        return False
    for i in range(2, int(year ** 0.5) + 1):
        if year % i == 0:
            return False
    return True

year = int(input("Enter a year to check if it's prime: "))
if is_prime(year):
    print(f"{year} is a prime number.")
else:
    print(f"{year} is not a prime number.")

# 28. Create a program that sorts three numbers in ascending order using conditional statements.

def sort_three_numbers(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

sorted_numbers = sort_three_numbers(a, b, c)
print(f"The numbers in ascending order are: {sorted_numbers[0]}, {sorted_numbers[1]}, {sorted_numbers[2]}")

# 29. Build a program that determines the roots of a quartic equation using numerical methods.

import numpy as np

def quartic_roots(a, b, c, d, e):
    # Solving a quartic equation ax^4 + bx^3 + cx^2 + dx + e = 0 using numpy's roots function
    coefficients = [a, b, c, d, e]
    roots = np.roots(coefficients)
    return roots

a = float(input("Enter coefficient a for x^4: "))
b = float(input("Enter coefficient b for x^3: "))
c = float(input("Enter coefficient c for x^2: "))
d = float(input("Enter coefficient d for x: "))
e = float(input("Enter coefficient e: "))

roots = quartic_roots(a, b, c, d, e)
print(f"The roots of the quartic equation are: {roots}")

# 30. Write a program that calculates the BMI (Body Mass Index) and provides health recommendations based on the user's input.

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def health_recommendation(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

weight = float(input("Enter your weight (in kg): "))
height = float(input("Enter your height (in meters): "))

bmi = calculate_bmi(weight, height)
category = health_recommendation(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"Health Recommendation: {category}")


# 31. Create a program that validates a password based on complexity rules (length, characters, etc.).

import re

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r"[A-Za-z]", password):
        return "Password must contain at least one letter."
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one number."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain at least one special character."
    return "Password is valid."

password = input("Enter your password: ")
print(validate_password(password))

# 32. Develop a program that performs matrix addition and subtraction based on user input.

import numpy as np

def matrix_operations():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    print("\nEnter the elements of the first matrix:")
    matrix1 = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        matrix1.append(row)
    
    print("\nEnter the elements of the second matrix:")
    matrix2 = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        matrix2.append(row)
    
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    print("\nMatrix 1:")
    print(matrix1)
    print("\nMatrix 2:")
    print(matrix2)

    # Addition
    addition = matrix1 + matrix2
    print("\nMatrix Addition:")
    print(addition)

    # Subtraction
    subtraction = matrix1 - matrix2
    print("\nMatrix Subtraction:")
    print(subtraction)

matrix_operations()

# 33. Write a program that calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")

# 34. Build a program that performs matrix multiplication using nested loops and conditional statements.

def matrix_multiplication():
    rows1 = int(input("Enter number of rows of first matrix: "))
    cols1 = int(input("Enter number of columns of first matrix: "))
    rows2 = int(input("Enter number of rows of second matrix: "))
    cols2 = int(input("Enter number of columns of second matrix: "))

    if cols1 != rows2:
        print("Matrix multiplication is not possible. Number of columns of first matrix must equal number of rows of second matrix.")
        return
    
    print("\nEnter the elements of the first matrix:")
    matrix1 = []
    for i in range(rows1):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        matrix1.append(row)
    
    print("\nEnter the elements of the second matrix:")
    matrix2 = []
    for i in range(rows2):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        matrix2.append(row)
    
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    print("\nMatrix Multiplication Result:")
    for row in result:
        print(row)

matrix_multiplication()

# 35. Create a program that simulates a basic text-based tic-tac-toe game against the computer.

import random

def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--------")
    
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        if turn % 2 == 0:
            print("Player X's turn")
            row, col = map(int, input("Enter row and column (0, 1, 2): ").split())
            if board[row][col] != " ":
                print("Cell already taken! Try again.")
                continue
            board[row][col] = "X"
        else:
            print("Computer's turn")
            empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
            row, col = random.choice(empty_cells)
            board[row][col] = "O"
        
        if check_winner(board, players[turn % 2]):
            print_board(board)
            print(f"{players[turn % 2]} wins!")
            break
        
        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            print_board(board)
            print("It's a tie!")
            break
        
        turn += 1

tic_tac_toe()

# 36. Write a program that generates Fibonacci numbers up to a specified term using iterative methods.

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

n = int(input("Enter the number of terms for Fibonacci sequence: "))
fib_sequence = fibonacci(n)
print(f"Fibonacci sequence up to {n} terms: {fib_sequence}")

# 37. Develop a program that calculates the nth term of the Fibonacci sequence using memoization.

memo = {0: 0, 1: 1}

def fibonacci_memo(n):
    if n not in memo:
        memo[n] = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    return memo[n]

n = int(input("Enter the term number to get from Fibonacci sequence: "))
print(f"The {n}th Fibonacci number is: {fibonacci_memo(n)}")

# 38. Create a program that generates a calendar for a given month and year using conditional statements.

import calendar

def generate_calendar():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    print(calendar.month(year, month))

generate_calendar()

# 39. Build a program that simulates a basic text-based blackjack game against the computer.

import random

def blackjack():
    def draw_card():
        return random.choice(["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])

    def card_value(card):
        if card in ["J", "Q", "K"]:
            return 10
        if card == "A":
            return 11
        return int(card)
    
    def hand_value(hand):
        value = sum(card_value(card) for card in hand)
        aces = hand.count("A")
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value

    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]
    
    print("Your hand:", player_hand)
    print("Dealer's hand: [", dealer_hand[0], ", ?]")

    while hand_value(player_hand) < 21:
        action = input("Do you want to 'hit' or 'stand'? ").lower()
        if action == "hit":
            player_hand.append(draw_card())
            print("Your hand:", player_hand)
        elif action == "stand":
            break

    if hand_value(player_hand) > 21:
        print("You busted! Dealer wins.")
    else:
        print("Dealer's hand:", dealer_hand)
        while hand_value(dealer_hand) < 17:
            dealer_hand.append(draw_card())
            print("Dealer's hand:", dealer_hand)
        
        if hand_value(dealer_hand) > 21:
            print("Dealer busted! You win.")
        elif hand_value(player_hand) > hand_value(dealer_hand):
            print("You win!")
        elif hand_value(player_hand) < hand_value(dealer_hand):
            print("Dealer wins.")
        else:
            print("It's a tie!")

blackjack()

# 40. Write a program that generates the prime factors of a given number using trial division.

def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

number = int(input("Enter a number to find its prime factors: "))
factors = prime_factors(number)
print(f"The prime factors of {number} are: {factors}")






