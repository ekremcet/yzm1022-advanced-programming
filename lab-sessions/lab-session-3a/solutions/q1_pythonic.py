"""Lab Session 3 — Q1 Solution: Student Data Processor"""


class InvalidGradeError(Exception):
    pass


def validate_grade(grade: float):
    if grade < 0 or grade > 100:
        raise InvalidGradeError(f"Grade {grade} is out of range (0-100)")


class StudentProcessor:
    def passing_students(self, students):
        for s in students:
            avg = sum(s["grades"].values()) / len(s["grades"])
            if avg >= 60:
                yield s

    def grade_summary(self, students):
        return {s["name"]: sum(s["grades"].values()) / len(s["grades"]) for s in students}

    def top_students(self, students, n=3):
        return sorted(students, key=lambda s: sum(s["grades"].values()) / len(s["grades"]), reverse=True)[:n]

    def course_averages(self, students):
        all_courses = {c for s in students for c in s["grades"]}
        return {
            course: sum(s["grades"][course] for s in students if course in s["grades"]) /
                    sum(1 for s in students if course in s["grades"])
            for course in sorted(all_courses)
        }


class ReportWriter:
    def __init__(self, filename: str):
        self.filename = filename
        self._file = None

    def __enter__(self):
        self._file = open(self.filename, 'w')
        return self

    def __exit__(self, *args):
        if self._file:
            self._file.close()
        print(f"Report saved to: {self.filename}")

    def write(self, text: str):
        self._file.write(text + "\n")


if __name__ == "__main__":
    print("=== Student Data Processor ===")
    students = [
        {"name": "Alice", "grades": {"Math": 85, "Physics": 78, "Programming": 84}},
        {"name": "Bob",   "grades": {"Math": 72, "Physics": 75, "Programming": 74}},
        {"name": "Carol", "grades": {"Math": 93, "Physics": 89, "Programming": 91}},
        {"name": "Dave",  "grades": {"Math": 41, "Physics": 52, "Programming": 43}},
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
