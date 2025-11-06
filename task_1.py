import math
employee_name =input("enter your name")
basic_salary = int(input("Enter your alary"))
bonus_percentage = float(input("Enter bounus persentage"))
tax_rate = float(input("Enter your tax rate"))
bonus = basic_salary * bonus_percentage / 100
tax = (basic_salary + bonus) * tax_rate / 100
final_salary=(basic_salary+bonus)-tax 
final_salary=math.ceil(final_salary)
Squaare_boot=math.sqrt(bonus)
print("---------------------")
print(f"your name{employee_name}") # f معناها اني اقدر ابعت ال printفيه حروف و ارقام من غير +هينظم 
print(f"your salary{basic_salary}")
print(f"your bonus{bonus}")
print(f"your tax{tax}")
print(f"your final salary{final_salary}")
print(f"your nquared bouns{Squaare_boot}")
print("-----------------------")