# ==========================================
# Python Input and Output
# ==========================================

# Output using print()
print("Welcome to Python!")
print()

# Output multiple values
name = "raphinha"
age = 29

print("Name:", name)
print("Age:", age)
print()

# Taking user input
username = input("Enter your name: ")
print("Hello,", username)
print()

# Input with integer conversion
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2

print("Sum =", sum_result)
print()

# Input with float conversion
height = float(input("Enter your height (in feet): "))
print("Your height is", height, "feet.")
print()

# Formatted output using f-strings
city = input("Enter your city: ")

print(f"Welcome {username} from {city}!")