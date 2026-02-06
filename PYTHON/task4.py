#create alist of dictionaries
students = [
    {'name': 'Malak', 'grades': [85, 90, 96]},
    {'name': 'Sajed', 'grades': [78, 88, 80]},
    {'name': 'yamen', 'grades': [95, 89, 91]}
]
for marks in students:
    name = marks["name"] 
    grades =marks["grades"] 
    average_grade = sum(grades) /len(grades)
    print(f"{name} average_grade:{average_grade:.2f}")