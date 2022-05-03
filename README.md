# Data Types, Values and Functions  

Data types are classifications, or ways that Python organizes the different ways that data can exist in the language. It is a way of representing the value type, and what operations can be performed on that data. As everything in Python is an object, we can treat Data types like classes and variables as instances of them.

If you are not sure what Classes and Objects are and how they relate to Python, check out these resources:

https://www.youtube.com/watch?v=xoL6WvCARJY

https://www.codecrashcourse.com/introduction-to-object-oriented-programming/

It is essential to understand what OOP (Object Oriented Programming) is in order to grasp how Python works. If it elludes you for now, don't worry, we will go over it in our course. 

Here are the standard or built-in data types of Python:

![image](https://user-images.githubusercontent.com/100561922/166401077-ceac5b8f-7678-458e-b5b4-00a078267e3f.png)

These Data Types are fundamental to a lot of Python programs and effectively all are built upon any framework. In order to become more comfortable with them all, we will go through some tests to get used to working with them.


## Instructions

The collections data types (Dictionary, Lists, Tuples, Sets) do not expect anything other than a string, you should not convert any of the inputted variables to any type other than what is returned by input().

Some skeleton code is given to you to help make it clearer what is it you are meant to do.

### Program Process

1. A user inputs a name of a data type
   ```python
    data_type = input("Choose a data type\n") 
    # The \n is an escape character to indicate that it is a new line
    # like pressing enter at the end of a sentence
   ```
3. Using that input, the program either lets them input a value straight away in the case of integer or Booleans
4. If it is a collection type then the program needs to ask how many values they would like to create it with
   ```python
   length = int(input("How many variables?\n"))
   ```
5. Using that length, the program asks the user for what value they would like to add to it
   ```python
    for i in range(length):
      # do something
   ```  
6. Once complete, the program prints out the object for the user
     ```python
      print(created_object)
     ```

## Hints
This test requires a lot of dealing with user inputs, casting data types, for loops, creating, managing, adding to sequences and finally conditional flow.

This is a lot of things so I will provide some resources to help make this a bit easier.
Code has also been provided to give you somewhere to start.

### Good Luck!

[User Inputs](https://www.w3schools.com/python/ref_func_input.asp)

[Casting Data Types](https://www.w3schools.com/python/python_casting.asp)

[For Loops](https://www.w3schools.com/python/python_for_loops.asp)

[Sequences](https://www.pythontutorial.net/advanced-python/python-sequences/)

[Lists](https://developers.google.com/edu/python/lists)

[Sets](https://www.programiz.com/python-programming/set)

[Dictionaries](https://www.geeksforgeeks.org/python-dictionary/) 

[Tuples](https://www.programiz.com/python-programming/tuple) 

[Conditional Flow](https://www.openbookproject.net/books/bpp4awd/ch04.html) 
