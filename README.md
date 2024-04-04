# lab05
week 5 python lab

Exercises

1. Define a function that takes a list as a parameter, count and return the number of unique elements in the list.

For example, if the list is [1, "cat", 2, "cat", 2.3, 2 ], your function should return 4 as there are only four unique elements in the list.

Test the function by calling it three times each with a different list.

Hint: maintaining a temporary list inside the function, and adding an element into the list if it is not already in it.

Food for thought: if your list contains both 1 and True or 0 and False, does your program still work correctly? If not, how to correct it?

2. Revising Exercise 1 above, so that the function still takes a list as its parameter, but it would return both the number of unique elements in the original list as well as the new list with only the unique elements. Test the function by calling it three times each with a different list.

3. Explain the concept of alias and cloning in Python.

Read the following Python code:

     a = 1
     b = a
     b = 3
  Question 1: do variables a and b refer to the same object after the second statement? Explain why. Verify your answer with the id function to see the id of each object.

  Question 2: in the 3rd statement, we assigned a new value to variable b. Would this change affect variable a? Explain why.

     x = [1, 2, 3]
     y = x
  Question 3: do variables x and y refer to the same object? Explain why.

     y.append(4)
  Question 4: what is the current value of y? What is the current value of x? Why?

    y = y + [5]
  Question 5: what is the current value of y? What is the current value of x? Are x and y having the same value or different values? Why?

    z = x[:]
  Question 6: what is the current value of z? Do variables x and z refer to the same object or different objects? Why? Can you give some concrete evidence?

4. Write a program that reads a long English sentence from the keyboard into a string and then break the sentence into a list words. Count and print out the number of words in the sentence.

5. Write a function that takes a list of words as its formal parameter and capitalise each word in the list.

Outside the function, create a list of words L and call the this function to capitalise each word in the list and print out these capitalised words.

Discussion: what is the "side-effect" of a function? Does your solution use or have a side-effect? Can you create one version of the function with side-effects and another version of the function without side-effects?

6. Write a program that will take the marks (for three assessments Quiz1 (20%), Quiz2(30%) and Final(50%)) of all the students of a unit as input and stores all the detail in a list. Your program should have following features and constrains:

Check the input validity: each mark must be between 0 and 100, and each mark must be a whole number
Compute the total mark and letter grade. The total mark is the weighted average of the three marks, ie total = Q1 * 0.20 + Q2 * 0.30 + Final * 0.50. The total mark must be rounded to the nearest whole number. Use the Murdoch University grade conversion table to calculate the letter grade
Keep taking the input unless a negative number or zero is given as the input for student ID
Save the data for each student in a list in following format:
[st_ID, Q1_mark, Q2_mark, Final_mark, Total, Letter grade]
Display the whole list
A typical input output screenshot might be as follows:

Student ID:1001
Enter Q1: 60
Enter Q2: 65
Enter Final: 55
Student ID:1002
Enter Q1: 80
Enter Q2: 75
Enter Final: 68
Student ID:1003
Enter Q1: 45
Enter Q2: 50
Enter Final: 52
Student ID:0
[[1001, 60, 65, 55, 59, 'P'], [1002, 80, 75, 68, 73, 'D'], [1003, 45, 50, 52, 50, 'P']]

7.Expand Exercise 6 above. Show the following statistics:

Average, highest and lowest mark
Total number of students failed in the unit (assuming 50% is the pass mark)
Create a list containing the IDs of those students whose total mark is 80 or more from the list generated from Exercise 6 and print the list out. Please use list comprehension to create this list.

8. Write a student management system that can perform following operations repeatedly (use a continuous menu that would not exit until the user wants to do so):

Add student detail (ID, name, GPA(0~4), major, contact number etc.)
Search a particular student
Delete a particular student
Display all dean's list students (students with GPA>=3.75)
Display all students detail in a user-friendly manner. Note: you may use a 'list' to store all the information.
