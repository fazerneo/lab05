# I made a function that takes a list as its formal parameter
# I initialized an empty variable that will hold integer value
# I initialize an empty list
# I iterate through the elements in the list
# If an item in the list is not present in the new empty list, the element is appended to the new empty list
# Then the count variable is incremented by 1
# The function returns count
def  unique_element_counter(list):
    count = 0
    temp = []
    for i in list:
        if i not in temp:
            temp.append(i)
            count += 1            
    return count

# I initialize a new list and call the function using this list
list_1 = [1, "cat", 2.0, 3, 1, 2.0]
print(f" the number of unique elements in list_1 is: {unique_element_counter(list_1)}")

# I initialize a new list and call the function using this list
list_2 = [1, True, 0, False, "string", True]
print(f" the number of unique elements in list_2 is: {unique_element_counter(list_2)}")

# I made another function so that 1 and True are differentiated by python
# int and float methods dont work as both end up with 1 still being equal to True, thus I made the element that is being iterated into a string
def  unique_element_counter_2(list):
    count = 0
    temp = []
    for i in list:
        i = str(i)
        if i not in temp:
            temp.append(i)
            count += 1            
    return count

# I initialized a list with 1 and True, 0 and False and other elements
# I then call the function and since all elements are treated as string, it gives the actual number of unique elements
list_3 = [1, True, 0, False, "string", True]
print(f" the number of unique elements in list_3 is: {unique_element_counter_2(list_3)}")