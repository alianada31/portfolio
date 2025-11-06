report= ["report1", "report2" , "report3" ]
acc_active= True
bending= False
if acc_active and not bending:
    print("you have acssess to")
    print(report)
else:
    print("Account inactive or bending detected")
