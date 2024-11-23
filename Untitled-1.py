def grade_to_points(grade):
    if grade == 'A':
        return 5
    elif grade == 'B':
        return 4
    elif grade == 'C':
        return 3
    elif grade == 'D':
        return 2
    elif grade == 'E':
        return 1
    elif grade == 'F':
        return 0
    else:
        return None

def points_to_grade(points):
    if points >= 4.5:
        return 'A'
    elif points >= 3.5:
        return 'B'
    elif points >= 2.5:
        return 'C'
    elif points >= 1.5:
        return 'D'
    elif points >= 0.5:
        return 'E'
    else:
        return 'F'

# Read input
n = int(input("Enter number of exams: "))
total_weighted_points = 0
total_weight = 0

for _ in range(n):
    line = input("Enter weight and grade (e.g., 3 A): ").split()
    weight = float(line[0])
    grade = line[1]
    
    points = grade_to_points(grade)
    if points is not None:
        total_weighted_points += points * weight
        total_weight += weight
    else:
        print("Invalid grade:", grade)

if total_weight > 0:
    average_points = total_weighted_points / total_weight
    average_grade = points_to_grade(average_points)
    print("Average Grade:", average_grade)
else:
    print("No valid grades entered.")
