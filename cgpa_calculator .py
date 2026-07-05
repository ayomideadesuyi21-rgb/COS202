print ("=================================")
print ("    PERSONAL POCKET CGPA")
print ("=================================")

total_points = 0
total_units = 0

num_courses= int(input("Enter number of courses: "))

for i in range(num_courses):
    print("\nCourse", i + 1)

    unit = int(input("Enter course unit: "))
    grade = input("Enter grade (A, B,C,D, E, F)): ").upper()

    if grade == "A":
        point = 5
    elif grade == "B":
        point = 4
    elif grade == "C":
        point = 3
    elif grade == "D":
        point = 2
    elif grade == "E":
        point = 1
    else:
        point = 0

    total_points += point * unit
    total_units += unit

cgpa = total_points / total_units

print("\n===============================")
print("Your CGPA is:", round(cgpa, 2))
print("================================")      
