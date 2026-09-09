# Student Grade Calculator

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i} (0-100): "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
grade = calculate_grade(average)

print("\n----- Result -----")
print("Student:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
