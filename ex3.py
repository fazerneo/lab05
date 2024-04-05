# 3. Explain the concept of alias and cloning in Python.

# Read the following Python code:

#     a = 1
#     b = a
#     b = 3                                                 '''
#  Question 1: do variables a and b refer to the same object after the second statement? Explain why. Verify your answer with the id function to see the id of each object.
'''  Answer: Yes. the two variables point to the same object. a var holds 1 and b var is just an alias of a '''

a = 1
b = a
print(a, b)
print(id(a))
print(id(b))

#  Question 2: in the 3rd statement, we assigned a new value to variable b. Would this change affect variable a? Explain why.
'''  Answer: This change won't directly affect a as no change operations have been made on a, assigning a new object to the b var broke
the alias relation between a and b. '''

b = 3
print()
print(a, b)
print(id(a))
print(id(b))

#     x = [1, 2, 3]
#     y = x           
#  Question 3: do variables x and y refer to the same object? Explain why.
'''  Answer: Yes the two variables refer to the same object. Y is an alias of x, y is just assigned the value inside x and 
no new object is being created.'''

x = [1, 2, 3]
y = x
print()
print(x, y)
print(id(x))
print(id(y))

#  y.append(4)
#  Question 4: what is the current value of y? What is the current value of x? Why?
'''  Answer: The append changes the value of both x and y as y is the alias of x and any operation on y 
will take effect on x. However, assigning a new object to y will break the alias relation'''

y.append(4)
print()
print(x, y)
print(id(x))
print(id(y))

#  y = y + [5]
#  Question 5: what is the current value of y? What is the current value of x? Are x and y having the same value or different values? Why?
'''  Answer: The values become different as y is being assigned a new value or object, this breaks the alias relation with x. x
maintains it's old object and y is assigned a new object. '''

y = y + [5]
print()
print(x, y)
print(id(x))
print(id(y))

#  z = x[:]
#  Question 6: what is the current value of z? Do variables x and z refer to the same object or different objects? Why? Can you give some concrete evidence?
'''  Answer: current value of z is the same as x as z is just a clone of x. However, they both refer to different objects as can be seen
with the id method. x holds an object and z is assigned a clone of x, which may have the same value but is different in essence.
Clone creates a copy of the object in another memory address instead of making an alias that points to the same object. '''

z = x[:]
print()
print(x, z)
print(id(x))
print(id(z))