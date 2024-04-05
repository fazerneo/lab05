# This is the letter grader function for exercise 6 and exercise 7. To make the main program cleaner I put the function in another file
''' I define a function that takes three formal parameters and uses the given formula to calculate 
the total marks and round them up to a whole number. '''
def Total(Q1_marks, Q2_marks, Final_marks):
    Total = round(float((Q1_marks * 0.20) + (Q2_marks * 0.30) + (Final_marks * 0.50)))
    
    return Total

# This is the letter grader function for exercise 6 and exercise 7. To make the main program cleaner I put the function in another file
''' This function takes one formal parameter, which is the total marks and calculates the letter grade
as per the murdoch guidelines. '''
# I believe this function may be useful someday and might be useful to have it along
def Letter_Grader(Total_Marks):
    if Total_Marks in range(80, 101):
        Letter_Grade = "HD"
    elif Total_Marks in range(70, 80):
        Letter_Grade = "D"
    elif Total_Marks in range(60, 70):
        Letter_Grade = "C"
    elif Total_Marks in range(50, 60):
        Letter_Grade = "P"
    else:
        Letter_Grade = "N"
        
    return Letter_Grade        

def average(total_marks, list):
    class_Total = 0
    class_Total = class_Total + total_marks
    Average = class_Total/len(list)
    
    return Average