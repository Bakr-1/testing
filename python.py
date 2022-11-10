
# type casting
# int()
# float()
# str()
# list()
# tuple()
# set()
# dict()

# use of type() to show what type of data it is
# example
i = 1.1
print(type(i))
print(i)
i = int(i)
print(type(i))
print(i)

# =============================================================================

# lists are mutable and can be changed
books = ["The Grapes of Wrath", "The Great Gatsby", "The Catcher in the Rye"]
print(books[0])
books.pop(0)
print(books[0])
#tuple is immutable and cannot be changed
numbers = (1, 2, "hello tuple!")
print(numbers[2])

#dictionary is a key value pair and can be changed
students = {"Alice": 25, "Bob": 27, "Claire": 17, "Dan": "dictionary", "Emma": 22}
print(students["Dan"])

#set is a collection of unique elements and can be changed but cannot be indexed
vowles = {"a", "e", "i", "o", "u"}
vowles.pop()
print(vowles)
vowles.add("w")
print(vowles)
# =============================================================================

# OOP (Object Oriented Programming) is a way of programming that is based on the concept of objects and classes
# class is a blueprint for creating objects (a particular data structure), providing initial values for state
# (member variables or attributes), and implementations of behavior (member functions or methods)
# two chaarcteristics of an object are its attributes and its behavior
# attributes are data stored inside a class or instance
# behavior is the only way objects can do anything to themselves or have anything done to them

# =============================================================================
