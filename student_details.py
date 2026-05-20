
student_registry = {
    1001: ("Alen p reji", "Computer Science", 2026),
    1002: ("Jones", "Mathematics", 2027),
    1003: ("Charlie", "Physics", 2026)
}

# 2. Course Enrollment (Dictionary + Sets)
# Format: {sid: {"COURSE1", "COURSE2"}}
course_enrollments = {
    1001: {"CS101", "MATH202"},
    1002: {"MATH202", "PHY101"},
    1003: {"PHY101", "CS101"}
}

# 3. Grade Tracking (Dictionary + List of Tuples)
# Format: {sid: [("COURSE1", grade), ("COURSE2", grade)]}
grade_books = {
    1001: [("CS101", 95.0), ("MATH202", 88.0)],
    1002: [("MATH202", 90.0), ("PHY101", 82.0)],
    1003: [("PHY101", 75.0), ("CS101", 80.0)]
}

def enroll_student(sid, course_code):
    """Adds a course to student's set, preventing duplicates."""
    if sid not in course_enrollments:
        course_enrollments[sid] = set()
    
    # Set automatically handles duplicate prevention
    course_enrollments[sid].add(course_code)
    print(f"Enrolled {student_registry[sid][0]} in {course_code}.")

def get_common_courses(sid1, sid2):
    """Uses set intersection to find common courses."""
    set1 = course_enrollments.get(sid1, set())
    set2 = course_enrollments.get(sid2, set())
    return set1.intersection(set2)

def calculate_gpa(sid):
    """Calculates average grade from list of tuples."""
    grades = grade_books.get(sid, [])
    if not grades:
        return 0.0
    
    total = sum(grade for course, grade in grades)
    return total / len(grades)

def run_registry_auditor():
    """Prints a summary report of students and their courses."""
    print("\n--- Registry Auditor Report ---")
    for sid, info in student_registry.items():
        name = info[0]
        courses = course_enrollments.get(sid, set())
        print(f"Student: {name} (ID: {sid}) | Courses: {', '.join(courses)}")
    print("-------------------------------\n")
# 1. Enroll Student (Test Duplicate Prevention)
enroll_student(1001, "PHYS101")
enroll_student(1001, "CS101") # Duplicate - Set will ignore this

# 2. Common Ground Finder
common = get_common_courses(1001, 1003)
print(f"\nCommon courses between 1001 and 1003: {common}")

# 3. GPA Calculator
gpa = calculate_gpa(1001)
print(f"Alice's Average Grade: {gpa:.2f}")

# 4. Registry Auditor
run_registry_auditor()
