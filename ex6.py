from functions import Letter_Grader

# I initialize two empty lists, one to hold the student details and one to hold only student ids so that deuplicate entries are not made
student_details = []
student_Ids = []

while True:
    Student_Id = input("Enter Student ID: ")
    Student_Id = int(Student_Id)
    
    if Student_Id <= 0 or Student_Id in student_Ids:
        print("\nError: Invalid Student ID")
        break
    
    student_Ids.append(Student_Id)
    
    Quiz1 = input("Enter Q1: ")
    Quiz1 = int(Quiz1)
    while Quiz1 not in range(0, 101):
        Quiz1 = input("Please enter valid marks between 0 and 100: ")
        Quiz1 = int(Quiz1)
        if Quiz1 in range(0, 101):
            break
        
    Quiz2 = input("Enter Q2: ")
    Quiz2 = int(Quiz2)
    while Quiz2 not in range(0, 101):
        Quiz2 = input("Please enter valid marks between 0 and 100: ")
        Quiz2 = int(Quiz2)
        if Quiz2 in range(0, 101):
            break
        
    Final = input("Enter Final: ")
    Final = int(Final)
    while Final not in range(0, 101):
        Final = input("Please enter valid marks between 0 and 100: ")
        Final = int(Final)
        if Final in range(0, 101):
            break
    
    Total_Marks = Total(Quiz1, Quiz2, Final)
    Letter_Grade = Letter_Grader(Total_Marks)
    
    student_details.append([Student_Id, Quiz1, Quiz2, Final, Total_Marks, Letter_Grade])
    print()
    print(student_details)      
    print()  