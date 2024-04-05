# I made a function that takes a list as its formal parameter
# I initialized an empty variable that will hold integer value
# I initialize an empty list
# I iterate through the elements in the list
# If an item in the list is not present in the new empty list, the element is appended to the new empty list
# Then the count variable is incremented by 1
# The function returns count and temp(the new list)
def  unique_element_counter(list):
    count = 0
    temp = []
    for i in list:
        i = str(i)
        if i not in temp:
            temp.append(i)
            count += 1            
    return count, temp

# I initalize a list with 1, 0, bools and others
list_1 = [1, True, 0, False, "string", True, False]

# I call the function and store it's output in a two variables using a tuple
# I print the values of the number of unique elements and the new list with the unique elements
(count, temp) = unique_element_counter(list_1) 
print(f" the number of unique elements in list_1 is: {count}")
print(f" the new list with the unique elements is: {temp}")

# I initalize another list
list_2 = [1, 2, "0", False, "strong", [1, 1, "a"], False]

# I call the function and store it's output in a two variables using a tuple
# I print the values of the number of unique elements and the new list with the unique elements
(count, temp) = unique_element_counter(list_2)
print() 
print(f" the number of unique elements in list_2 is: {count}")
print(f" the new list with the unique elements is: {temp}")

# I initalize another list
list_3 = [[1, "a", "b"], (2,), 23, 4+5, 9]

# I call the function and store it's output in a two variables using a tuple
# I print the values of the number of unique elements and the new list with the unique elements
(count, temp) = unique_element_counter(list_3)
print() 
print(f" the number of unique elements in list_2 is: {count}")
print(f" the new list with the unique elements is: {temp}")