"""
Lab Session 3A — Question 1: Student Data Processor (30 pts)
See README.md for requirements. Do NOT modify the test code below.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME:
STUDENT ID:
"""

# YOUR CODE HERE


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Student Data Processor ===")

    students = [
        {"name": "Alice", "grades": {"Math": 85, "Physics": 78, "Programming": 84}},
        {"name": "Bob", "grades": {"Math": 72, "Physics": 75, "Programming": 74}},
        {"name": "Carol", "grades": {"Math": 93, "Physics": 89, "Programming": 91}},
        {"name": "Dave", "grades": {"Math": 41, "Physics": 52, "Programming": 43}},
    ]

    processor = StudentProcessor()

    print("\nPassing students (avg >= 60):")
    for s in processor.passing_students(students):
        avg = sum(s["grades"].values()) / len(s["grades"])
        print(f"  {s['name']}: {avg:.2f}")

    print("\nGrade summary:")
    for name, avg in processor.grade_summary(students).items():
        print(f"  {name}: {avg:.2f}")

    print("\nCourse averages:")
    for course, avg in processor.course_averages(students).items():
        print(f"  {course}: {avg:.2f}")

    print("\nTop 2 students:")
    for i, s in enumerate(processor.top_students(students, n=2), 1):
        avg = sum(s["grades"].values()) / len(s["grades"])
        print(f"  {i}. {s['name']} - {avg:.2f}")

    print("\nWriting report...")
    with ReportWriter("grades.txt") as rw:
        rw.write("=== Grade Report ===")
        for s in students:
            rw.write(s["name"])

    print("\nValidation test:")
    try:
        validate_grade(110)
    except InvalidGradeError as e:
        print(f"Error caught: {e}")
