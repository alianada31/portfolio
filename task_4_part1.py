# مجموعات الطلاب في كل كورس
math_students = {"Ali", "Sara", "Omar", "Laila"}
science_students = {"Sara", "Omar", "Mona"}

both_courses = math_students & science_students
print("students enrolled in the two courses together:", both_courses)


one_course_only = math_students ^ science_students
print("students enrolled in only one course", one_course_only)
print("-" * 50)


students_scores = {
    "Ali": 75,
    "Sara": 45,
    "Omar": 60,
    "Laila": 30,
    "Mona": 90
}

passed_students = set()
failed_students = set()


for name, score in students_scores.items():
    status = "Pass" if score >= 50 else "Fail"
    students_scores[name] = {"score": score, "status": status}
    print(f"{name} got {score} - {status}")
    if status == "Pass":
        passed_students.add(name)
    else:
        failed_students.add(name)

print("Number of successful:", len(passed_students))
print("Number of depositors:", len(failed_students))
