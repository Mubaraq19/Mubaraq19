student_name = "Mubarak Akintola"
matric_number = "22/25PU110"
age = 22
cgpa = 3.75
is_active = True
courses_registered = ["Python", "Statistics"]
grades = {"Python": "A", "Statistics": "B"}
students = {
    "Mubarak": {"matric": "22/25PU110", "age": 21, "cgpa": 4.2, "is_active": True, "courses": ["Python", "Math"], "grades": {"Python": "A", "Math": "B"}},
    "Fatima": {"matric": "22/28PU021", "age": 20, "cgpa": 3.5, "is_active": True, "courses": ["Python", "Biology"], "grades": {"Python": "B", "Biology": "A"}},
    "Abdulrahmon": {"matric": "22/25PU034", "age": 22, "cgpa": 2.7, "is_active": False, "courses": ["Chemistry"], "grades": {"Chemistry": "C"}},
    "Luqman": {"matric": "22/25PU001", "age": 23, "cgpa": 4.8, "is_active": True, "courses": ["Physics", "Math"], "grades": {"Physics": "A", "Math": "A"}},
    "Sanusi": {"matric": "22/25PU002", "age": 24, "cgpa": 2.9, "is_active": True, "courses": ["English", "Python"], "grades": {"English": "C", "Python": "B"}},
}

unique_courses = set()
for s in students.values():
    unique_courses.update(s["courses"])
    
department_info = ("Computer Science", "Faculty of Technology", 2025)
def get_grade(score):
    if score >= 70:
        grade = 'A'
    elif score >= 60:
        grade = 'B'
    elif score >= 50:
        grade = 'C'
    elif score >= 45:
        grade = 'D'
    elif score >= 40:
        grade = 'E'
    else:
        grade = 'F'

   Match grade:
        case 'A':
            print("Excellent work!")
        case 'B':
            print("Very good work!")
        case 'C':
            print("Good effort.")
        case 'D':
            print("Fair, but room for improvement.")
        case 'E':
            print("Needs improvement.")
        case 'F':
            print("Failed. Better luck next time.")
    return grade
    def input_and_validate():
    try:
      age_input = input("Enter your age: ")
        age = int(age_input)

        cgpa_input = input("Enter your CGPA: ")
        cgpa = float(cgpa_input)

        if 16 <= age <= 40 and 0.0 <= cgpa <= 5.0:
            print("Valid input received.")
        else:
            print("Age or CGPA out of range.")
    except ValueError:
        print("Invalid input! Enter numbers only.")
        age = int(input("Enter age: "))
                cgpa = float(input("Enter CGPA: "))
                is_active = input("Is active? (yes/no): ").lower() == "yes"
                courses = input("Enter courses (comma separated): ").split(",")
                students[name] = {"matric": matric, "age": age, "cgpa": cgpa, "is_active": is_active, "courses": courses}
                print(f"{name} added successfully.")
            case '3':
                name = input("Enter student name: ")
                if name in students:
                    eligible, msg = check_eligibility(students[name])
                    print(msg)
                else:
                    print("Student not found.")
            case '4':
                top = max(students.items(), key=lambda x: x[1]['cgpa'])
                print(f"Top performer: {top[0]} with CGPA {top[1]['cgpa']}")
            case '5':
                print("Exiting...")
                break
            case _:
                print("Invalid choice.")
                def check_eligibility(profile):
    if profile['cgpa'] >= 2.5 and profile['is_active'] and len(profile.get('courses', [])) >= 1:
        return True, "Eligible for graduation"
        scores = [78, 82, 69, 91, 56, 63, 77, 85, 49, 95]

top_3 = scores[:3]
last_5 = scores[-5:]
alternate_scores = scores[::2]

print("Top 3 scores:", top_3)
print("Last 5 scores:", last_5)
print("Every other score:", alternate_scores)
set_pass = {"Mubarak", "Fatima", "Abdulrahmon", "Luqman", "Sanusi"}
set_merit = {{"Mubarak", "Fatima", "Abdulrahmon", "Luqman", "Sanusi"}

intersection = set_pass & set_merit
union = set_pass | set_merit
difference = set_pass - set_merit

print("Passed and on merit:", intersection)
print("All distinct students:", union)
print("Passed but not on merit:", difference)
def menu():
    while True:
        print("\n--- Student Menu ---")
        print("1. View all students")
        print("2. Add new student")
        print("3. Check graduation eligibility")
        print("4. Find top performer")
        print("5. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                for name in students:
                    print(name)
            case '2':
                name = input("Enter name: ")
                matric = input("Enter matric number: ")