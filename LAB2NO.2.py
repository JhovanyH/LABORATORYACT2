#initialize the value of pag-ibig contribution to 100.00
Pagibig_Contribution=100.00


#Input the value of rate per hour, number of working hours per day. number of days per week, number of weeks per month.
Employee_Name=input("Enter Employee name:")
Department=input("Enter Department:")
Rate_Per_Hour=float(input("Enter Rate per hour:"))
Working_Hours_Per_Day=float(input("Enter Number of working hours per day:"))
Working_Days_Per_Week=float(input("Enter Number of Working days per week:"))
Working_Weeks_Per_Month=float(input("Enter Number of working weeks per month:"))

print()#blankSpace

#Compute the value of gross income using the formula:
Gross_Income=(Rate_Per_Hour * Working_Hours_Per_Day * Working_Days_Per_Week * Working_Weeks_Per_Month)


#Conditions for SSS
def compute_SSS():
    if Gross_Income<=20000 and Gross_Income>=0:
        return 125.75
    elif Gross_Income<=50000 and Gross_Income>=20001:
        return 2200.50
    elif Gross_Income<=75000 and Gross_Income>=50001:
        return 4800.00
    else:
        return 5800.00
SSS_Contribution=compute_SSS()


#Conditions for Philhealth
def compute_philhealth():
    if Gross_Income<=20000 and Gross_Income>=0:
        return 100.00
    if Gross_Income<=20001 and Gross_Income>=50000:
        return 1200.00
    if Gross_Income>= 50001 and Gross_Income<=75000:
        return 6800.00
    else:
        return 8800.00
Philhealth_Contribution=compute_philhealth()

print()#BlankSpace

#Compute the total deduction using the formula:
Total_Deduction=SSS_Contribution+Pagibig_Contribution+Philhealth_Contribution

#Compute Net Income
Net_Income=Gross_Income-Total_Deduction

#Display Employee's name, Department, Gross income, Total deduction, Net income
print("Employee's name:", Employee_Name)
print("Department", Department)
print("Gross Income:", Gross_Income)
print("Total Deduction:", Total_Deduction)
print("Net Income:", Net_Income)