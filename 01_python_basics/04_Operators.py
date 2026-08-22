# Python Operators

# 1. Arithmetic Operators
a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)


# 2. Comparison Operators
x = 10
y = 5

print("\nComparison Operators:")
print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater Than or Equal:", x >= y)
print("Less Than or Equal:", x <= y)


# 3. Assignment Operators
num = 10

print("\nAssignment Operators:")
num += 5
print("+= :", num)

num -= 3
print("-= :", num)

num *= 2
print("*= :", num)

num /= 4
print("/= :", num)


# 4. Logical Operators
age = 18
has_id = True

print("\nLogical Operators:")
print("AND:", age >= 18 and has_id)
print("OR:", age >= 18 or has_id)
print("NOT:", not has_id)


# 5. Membership Operators
players = ["Yamal", "Pedri", "Raphinha"]

print("\nMembership Operators:")
print("Yamal" in players)
print("Messi" not in players)


# 6. Identity Operators
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("\nIdentity Operators:")
print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list3:", list1 is not list3)