# Function with side effect. Works but it over writes the original list
# I create a function with a list as it's formal parameter
# I iterate through the length of the list
# I replace the value in index number i with capitalized form of the same, gained from using capitalize method on that specific index number in the list
# I return the list
def capitalizer(list):
    for i in range(len(list)):
        list[i] = list[i].capitalize()
                    
    return list

# I initialize a list of words
L = ["i", "am", "good", "boy"]

# I print out the capitalized words list
# I print out the original list also to compare
print(f"List with words capitalized {capitalizer(L)}")
print(f"Original list {L}")

# Function without side effects. use a new list to store the output in order to not effect the original list
# I make a function that takes a list as its formal parameter
# I initialize an empty list to store the capitalized words
# I use a for loop to iterate through the words in the list and use the capitalize method to capitalize the word
# I then append the new capitalized word to the new empty list
# The function returns the new list
def capitalizer(list):
    capitalized_list = []
    for i in list:
        i = i.capitalize()
        capitalized_list.append(i)
            
    return capitalized_list

# I initialize a list
L = ["i", "am", "good", "boy"]

# I call the function that prints out the capitalized list
# I also print the original list for comparison
print()
print(f"List with words capitalized {capitalizer(L)}")
print(f"Original list {L}")