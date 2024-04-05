# I take an input from the user and store it inside a variable
# I then use the split method to split the words using the default argument, which is whitespace and store it in a variable
# I print out the number of words in the sentence by using the length method on the list created from the split method
sentence = input("Please enter a long english sentenceof atleast 5 words: ")
list_of_words = sentence.split()
print(f"the number of words in the sentence are: {len(list_of_words)}")