# Attendance Counter
count = 0
while True:
    name = input("Enter employee name (or type 'done' to finish): ")
    if name.lower() == "done":
        break
    count += 1

print(f"Total employees attended today: {count}")

# Departments
departments = {"IT", "HR", "Marketing", "Sales"}
branch_departments = {"Finance", "IT", "Sales", "Support"}

# 1. Departments in both branches
both = departments.intersection(branch_departments)
print("Departments in both branches:", both)

# 2. Departments only in main branch
only_main = departments.difference(branch_departments)
print("Departments only in main branch:", only_main)

# 3. All unique departments
all_unique = departments.union(branch_departments)
print("All unique departments:", all_unique)

# 4. Add "R&D"
departments.add("R&D")
print("After adding R&D:", departments)

# 5. Remove "HR"
departments.remove("HR")
print("After removing HR:", departments)

# Project Progress
for progress in range(0, 101, 20):
    print(f"Project progress: {progress}%")