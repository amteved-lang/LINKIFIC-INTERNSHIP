# Python Practice - Task 2

# 1. Variables
name = "Ved"
age = 21
cgpa = 8.0
is_student = True

print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Student:", is_student)


# 2. Data Types
integer_value = 10
float_value = 10.5
string_value = "Python"
boolean_value = True
list_value = [10, 20, 30]
tuple_value = (1, 2, 3)
dictionary_value = {"name": "Ved", "course": "B.Tech"}

print("\nData Types:")
print(type(integer_value))
print(type(float_value))
print(type(string_value))
print(type(boolean_value))
print(type(list_value))
print(type(tuple_value))
print(type(dictionary_value))


# 3. Conditional Statement
marks = 75

if marks >= 90:
    print("\nGrade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: F")


# 4. For Loop
print("\nFor Loop:")
for i in range(1, 6):
    print(i)


# 5. While Loop
print("\nWhile Loop:")
counter = 1
while counter <= 5:
    print(counter)
    counter += 1


# 6. Function
def greet(name):
    return f"Hello, {name}!"

print("\nFunction:")
print(greet("Ved"))


# 7. List Loop
numbers = [10, 20, 30, 40, 50]

print("\nList Elements:")
for number in numbers:
    print(number)
