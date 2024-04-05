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

def Total(Q1_marks, Q2_marks, Final_marks):
    Total = round(float((Q1_marks * 0.20) + (Q2_marks * 0.30) + (Final_marks * 0.50)))
    
    return Total
        