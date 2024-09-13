#Input the student name, value of final quizzes, final research/assignment. final project, and final exam
Student_Name=str(input("Enter Student name:"))
Final_Quiz=float(input("Enter Final Quiz grade:"))
Final_Research=float(input("Enter Final research grade:"))
Final_Project=float(input("Enter Final project grade:"))
Final_Exam=float(input("Enter Final exam grade:"))

#Determine the value of final grade
Final_Grade=(0.30*Final_Quiz)+(0.10*Final_Research)+(0.40*Final_Exam)+(0.20*Final_Project)
if Final_Grade>100:
    print("Error: Must not exceed 100")
else:print("Your Final Grade is:",Final_Grade)
    #papa mo
#Determine the equivalent grade using the conditions:
def Equivalent_Grade():
    if Final_Grade>=98 and Final_Grade<=100:
        return 4.00
    elif Final_Grade>=95 and Final_Grade<=97:
        return 3.75
    elif Final_Grade>=92 and Final_Grade<=94:
        return 3.50
    elif Final_Grade>= 89 and Final_Grade<=91:
        return 3.25
    elif Final_Grade>=86 and Final_Grade<=88:
        return 3.00
    elif Final_Grade>=83 and Final_Grade<=85:
        return 2.75
    elif Final_Grade>= 80 and Final_Grade<=82:
        return 2.50
    elif Final_Grade>=77 and Final_Grade<=79:
        return 2.25
    elif Final_Grade>=74 and Final_Grade<=76:
        return 2.00
    elif Final_Grade>=71 and Final_Grade<=73:
        return 1.75
    elif Final_Grade>=68 and Final_Grade<=70:
        return 1.50
    elif Final_Grade>=64 and Final_Grade<=67:
        return 1.25
    elif Final_Grade>=60 and Final_Grade<=63:
        return 1.00
    elif Final_Grade<60:
        return 0.00
    else:
        return ("INVALID")


#Display the equivalent grade base
Equivalent_grade=Equivalent_Grade()

#BlankSpace
print()

#Display the student's name, midterm grade, minor B, Final exam, Final grade, and the equivalent grading remark.
print("Your Student name is:", Student_Name)
print("Your Final Quiz is:", Final_Quiz)
print("Your Final Research is:", Final_Research)
print("Your Final Project is:", Final_Project)
print("Your Final Exam is:", Final_Exam)
print("Your Final Grade is:", Final_Grade)
print("Your Equivalent Grade is:", Equivalent_grade)

#Blankspace
print()

#Error notice for condition
if Final_Grade>100:
    print("\033[92mERROR! THE GRADE MUST NOT EXCEED 100!\033[92m")





