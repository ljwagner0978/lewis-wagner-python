# Lewis Wagner
# Assignment 1: Profile Card Builder
# Section 1

first_name = "John"
last_name = "Hubert"
age = 41
occupation = 'Janitor'
weight_lbs = 197.6
is_married = True

print(first_name, type(first_name))
print(last_name, type(last_name))
print(age, type(age))
print(occupation,type(occupation))
print(weight_lbs, type(weight_lbs))
print(is_married, type(is_married))

# Section 2

x = input("Enter your first name: ")
y = input("Enter the year you were born: ")
print(f"Hi, {x}! You are approximately {str((2026 - int(y)))} years old.")

# Section 3

number_1 = input("Please provide a number: ")
number_2 = input("Please provide a second number: ")
result = str(float(number_1)*float(number_2))

print(f"{number_1} × {number_2} = {result}")

# Section 4

membership_status = True
food_item = "Diet Coke Cola Soda - 12 pk"
regular_food_price = 10.99

def membership_price(regular_food_price, membership_status):
  if(membership_status):
      return(8.99)
  else:
      return regular_food_price
      
actual_food_price = membership_price(regular_food_price, membership_status)
quantity = 2
total_cost = round(actual_food_price * quantity, 2)
total_currency_formatted = f"${total_cost:,.2f}"

print("===========================")
print("        RECEIPT            ")
print("===========================")

print(f"Item: {food_item}")
print(f"Price: ${actual_food_price}")
print(f"Quantity: {quantity}")
print("---------------------------")
print(f"Total:   {total_currency_formatted}")
print("---------------------------")
if(regular_food_price - actual_food_price > 0):
    print("Thanks for being a member!")
    print(f"You saved ${((regular_food_price - actual_food_price) * quantity):,.2f} with us today!")
print("===========================")

# Section 5

name_s5 = input("Please provide your full name: ")
hometown_s5 = input("Please provide your hometown in (city, state initials) format: ")
hobby_s5 = input("Please provide your favorite hobby: ")
fun_fact_s5 = input("Please provide one fun fact about yourself: ")
birth_year_s5 = input("Please provide your birth year: ")

print("╔══════════════════════════════╗")
print(f"       PROFILE: {name_s5}         ")
print("╚══════════════════════════════╝")
print(f" Hometown:  {hometown_s5}")
print(f" Hobby:     {hobby_s5}")
print(f" Fun fact:  {fun_fact_s5}")
print(f" Age:       {(2026 - int(birth_year_s5))}")
