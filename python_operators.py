
# Python Operators - Examples
#Static way

# 1. Arithmetic Operators
a = 10
b = 3

print("1. Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Remainder:", a % b)

# 2. Assignment Operators
print("\n2. Assignment Operators")
x = 10
print("Initial value:", x)

x += 5
print("After += 5:", x)

x -= 3
print("After -= 3:", x)

x *= 2
print("After *= 2:", x)

x /= 4
print("After /= 4:", x)

# 3. Comparison Operators
print("\n3. Comparison Operators")
print("10 > 3:", a > b)
print("10 < 3:", a < b)
print("10 >= 3:", a >= b)
print("10 <= 3:", a <= b)
print("10 == 3:", a == b)
print("10 != 3:", a != b)

# 4. Logical Operators
print("\n4. Logical Operators")
age = 21
print("and:", age > 18 and age < 30)
print("or:", age < 18 or age > 20)
print("not:", not age > 18)

# 5. Identity Operators
print("\n5. Identity Operators")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list3:", list1 is not list3)

# 6. Membership Operators
print("\n6. Membership Operators")
fruits = ["apple", "mango", "banana"]

print("'mango' in fruits:", "mango" in fruits)
print("'grapes' not in fruits:", "grapes" not in fruits)

#Dynamic way


# Python Operators - Dynamic Examples

# Get input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# 1. Arithmetic Operators
print("\n1. Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
    print("Remainder:", a % b)
else:
    print("Division and remainder by zero are not allowed.")

# 2. Assignment Operators
print("\n2. Assignment Operators")
x = a
print("Initial value:", x)

x += b
print("After += :", x)

x -= b
print("After -= :", x)

x *= b
print("After *= :", x)

if b != 0:
    x /= b
    print("After /= :", x)

# 3. Comparison Operators
print("\n3. Comparison Operators")
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print("a == b:", a == b)
print("a != b:", a != b)

# 4. Logical Operators
print("\n4. Logical Operators")
print("Both positive:", a > 0 and b > 0)
print("At least one positive:", a > 0 or b > 0)
print("a is not positive:", not a > 0)

# 5. Identity Operators
print("\n5. Identity Operators")
list1 = [int(a), int(b)]
list2 = list1
list3 = [int(a), int(b)]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list3:", list1 is not list3)

# 6. Membership Operators
print("\n6. Membership Operators")
value = input("Enter a value to search in the list: ")
items = [str(int(a)), str(int(b))]

print("Value in list:", value in items)
print("Value not in list:", value not in items)
