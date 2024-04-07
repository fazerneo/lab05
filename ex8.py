
def main_menu():
    print("Student Management System")
    print("1. Add student details")
    print("2. Search a particular student")
    print("3. Delete a particular student")
    print("4. Display all dean's lis students (students with GPA >= 3.75)")
    print("5. Display all students detail in a user-friendly manner")
    print("Note: Please keep in mind that this system is command line based")
    print()
    user_input = input("Please select an option between 1 and 5 to get started: ")
    
    return user_input

''' Main Program '''
student_data = []
deans_list = []

while True:
    user_input = main_menu()
    user_input = int(user_input)
    
    if user_input == 1:
        print()
        student_ID = input("Please enter Student ID number: ")
        student_name = input("Please enter Student name: ")
    
        while True:
            GPA = float(input("Please enter student GPA between 0-4: "))
            if GPA > 0 and GPA < 4:
                break
        major = input("Please enter the major of the student: ")
        contact = input("Please enter the contact number: ")
        student_data.append([student_ID, student_name, GPA, major, contact])
        print()
        print(student_data) 
    
    if user_input == 2:
        search = input("Please enter the name of the student you want to search for: ")
        for i in student_data:
            if i[1] == search:
                print(i)
                break
            
    if user_input == 3:
        delete = input("Please enter the name of the student whose details you want to delete: ")
        for i in student_data:
            if i[1] == delete:
                student_data.remove(i)
                print(student_data)
                break
            
    if user_input == 4:
        for i in student_data:
            if i[2] >= 3.75:
                deans_list.append(i)
                print(deans_list)
                
    if user_input == 5:
        print("student ID, Name, GPA, Major, Contact ")
        for i in student_data:
            print(i[0],{} i[1],{} i[2],{} i[3],{} i[4]{}.format(""))