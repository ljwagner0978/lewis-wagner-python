# Lewis Wagner
# Assignment 1: Profile Card Builder

import datetime

# Section 1
first_name = "John"
last_name = "Hubert"
age = 41
weight_lbs = 197.6
is_married = True

print(first_name, type(first_name))
print(last_name, type(last_name))
print(age, type(age))
print(weight_lbs, type(weight_lbs))
print(is_married, type(is_married))

# Section 2
date = datetime.datetime.now()
x = input("Enter your first name: ")
y = input("Enter the year you were born: ")
print(f"Hi, {x}! You are approximately {str((date.year - int(y)))} years old.")

# Section 3

number_1 = float(input("Please provide a number: "))
number_2 = float(input("Please provide a second number: "))
result = number_1 * number_2

print(f"{number_1} × {number_2} = {result}")

# Section 4

membership_status = True
food_item = "Diet Coke Cola Soda - 12 pk"
food_price = 10.99
quantity = 2
total_cost = round((food_price * quantity), 2)

print("===========================")
print("        RECEIPT            ")
print("===========================")
Total:     
print(f"Item:      {food_item}")
print(f"Price:     ${food_price}")
print(f"Quantity:  {quantity}")
print("---------------------------")
print(f"Total:     ${total_cost}")
print("===========================")

# Section 5

name_s5 = input("Please provide your full name: ")
hometown_s5 = input("Please provide your hometown in (city, state initials) format: ")
hobby_s5 = input("Please provide your favorite hobby: ")
fun_fact_s5 = input("Please provide one fun fact about yourself: ")
birth_year_s5 = input("Please provide your birth year: ")

print("╔══════════════════════════════╗")
print(f"     PROFILE: {name_s5}        ")
print("╚══════════════════════════════╝")
print(f" Hometown:  {hometown_s5}")
print(f" Hobby:     {hobby_s5}")
print(f" Fun fact:  {fun_fact_s5}")
print(f" Age:       {(date.year - int(birth_year_s5))}")
