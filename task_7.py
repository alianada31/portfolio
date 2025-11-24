from unicodedata import category

print("Hello")
text = input("enter your category: ").strip().lower()
student_keywords = ["study","school","exam","university","homework"]
employee_keywords = ["work","meeting","salary","office","boss"]
student_score=0
employee_score=0
for word in student_keywords:
    if word in text:
        student_score += 1
for word in  employee_keywords:
    if word in text:
        employee_score +=1

if student_score == 0 and employee_score == 0:
    category = "unknown"
elif student_score > 0:
    category = "student"
elif employee_score > 0:
    category = "employee"
else:
    category ="unkown"
print("classificatioin:", category)
