# I import the neccessary functions I made and stored in functions.py.
# Please view functions.py to go through the functions
from functions import Letter_Grader, Total


''' Main Program '''
# I initialize empty variables and lists to be used in the main program
student_details = []
student_Ids = []
class_Total = int()
Average = int()
marks = []
failures = 0
deans_list = []

# I use a while loop to continuously iterate until the break condition is met
while True:
    # I take student ID as input from user and turn it into an int
    Student_Id = input("Enter Student ID: ")
    Student_Id = int(Student_Id)
    
    # If the student ID is negative, zero or already exists in student_Ids list, the loop is broken
    # If the break condition is met then an error message is printed to the screen before break
    if Student_Id <= 0 or Student_Id in student_Ids:
        print("\nError: Invalid Student ID")
        break
    
    # If the break condition is not met, the student_id is appended to the student_ids list
    student_Ids.append(Student_Id)
    
    # we then take inputs for Quiz1, Quiz2 and Final marks
    # We turn the marks into int and validate whether they are in between zero and 100.
    # If the marks are not valid, the user is continuously asked for valid marks
    # If valid marks is entered, we move on to the next step
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
    
    # We use the imported total funtion to find the total marks and store them in a variable
    # We then use the imported letter grader function to find the corresponding letter grade of the total marks
    Total_Marks = Total(Quiz1, Quiz2, Final)
    Letter_Grade = Letter_Grader(Total_Marks)
    
    # We then append the details about the student in a list form to the student_details list, which holds all student data
    student_details.append([Student_Id, Quiz1, Quiz2, Final, Total_Marks, Letter_Grade])
    
    ''' I calculate the average of the class by totalling the total marks of the class
    and dividing it by the length of the student details list where each student will have one entry'''
    class_Total = class_Total + Total_Marks
    Average = class_Total/len(student_details)
    
    # I append the total marks to a list called marks
    marks.append(Total_Marks)
    
    # I initialize a variable called highest with the value zero
    highest = 0
    
    ''' I use a for loop to iterate through the marks list and if the marks is greater than highest,
    then the marks is assigned to the highest variable and the lowest variable. Assigning to lowest
    is required so that lowest gets an initial value as having the lowest mark as zero does not work
    in practicality. '''
    for i in marks:
        if i >= highest:
            highest = i
            lowest = i
    
    ''' I use a for loop and if the marks is lower than lowest, then that marks is assigned to lowest.
    lowest initially takes the value from the for loop above to get an initial value that is not zero '''
    for i in marks:
        if i <= lowest:
            lowest = i
    
    # we use an if statement to check whether letter grade is N, which is fail
    # If letter grade is n, the count of failures is incremented by 1        
    if Letter_Grade == "N":
        failures += 1
            
    # We print out the student data to be viewed
    print()
    print(student_details)      
    print()
    print(f"the average marks in the class is: {Average}")
    print(f"the highest marks in the class is: {highest}")
    print(f"the lowest marks in the class is: {lowest}")
    print(f"the number of students failing the class is: {failures}")
    print()
    
# We use list comprehension outside the loop as inside the loop, the list would keep reiterating from the beginning
# We use list comprehension and add the student id of students scoring above 80 to a list and print it
deans_list = [i[0] for i in student_details if i[-1] == "HD"]
print(f"\nthe students scoring above 80 are: {deans_list}")         