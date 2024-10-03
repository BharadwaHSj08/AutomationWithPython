input_Name=input("Enter Name:")
input_Age=int(input("Enter Age:"))
input_Current_Year=int(input("Enter Current Year:"))

Age_to_become_Hundered= 100 - input_Age
print(Age_to_become_Hundered)

Year_tobe_100=input_Current_Year + Age_to_become_Hundered
print(Year_tobe_100)

print("{}, you will become 100 in the year {}".format(input_Name,Year_tobe_100))

#print(Final_Result)
