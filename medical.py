print("welcom to chatbot :) ")
faver = input("Do you have fever ? (yes/no): ").lower()
cough = input("Do you have cough ? (yes/no): ").lower()
headache = input("Do you have headache ? (yes/no): ").lower()
if faver == "yes" and cough == "yes" :
    print("possible flu")
elif headache == "yes" and faver == "no" and cough == "no" :
    print("possible migraine")
elif faver == "no" and cough == "no" and headache == "no" :
    print("Yes seem helthy")
else:
    print("Symptoms unclear")
