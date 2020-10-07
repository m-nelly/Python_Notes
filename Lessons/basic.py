def variables():
    
    x = 4 # These are variable assignments.
    y = 5 # When you reference x and y in your code they will return the stored values.

    print(x,", ", y) # This will output the values of x and y to the console window.

    # Variables can contain alphanumeric characters and underscores. 
    # Variables are case sensitive.

    # Variables assigned within functions are only available in that function.
    # This is called scope and will be explained further in this course.

    return()

def data_types():
    
    # There are several data types to choose from in Python.
    # The good news is that Python handles most of this work for you.

    x = 10

    print(type(x)) # This will show us the data type for x.

    #Data type can be set by specifying the name of the data type.

    x = float(10)

    print(x)

    print(type(x))

    #Data Types and Examples:
    a = str("Hello!")
    b = int(40)
    c = float(4.5)
    d = list(1,2,"word",True)
    e = dict({"key":"value"})
    f = set({"apple","banana","orange"})
    g = bool(True)
    #There are other data types, but these are the ones you will see most often.
    #These types will be explained in greater detail in later lessons.

    return()

def numbers():
    
    # integers can be positive or negative and don't have decimals.
    print(type(-300))

    # floating point numbers can be positive or negative and have a decimal.
    print(type(23.21))

    # comlex or imaginary numbers are written with a "j" as the imaginary part.
    print(type(5j))

    # Python has a module called 'random' that can be used to generate pseudo-random numbers.

    return()

def casting():
    
    # in Python you can cast data of one type as another.
    
    x = str('5')
    y = int(x)
    print(x," ",y)
    print(type(x))
    print(type(y))

    # floats that are converted into integers will be rounded down.
    
    return()

def strings():
    # Python strings can be denoted with single '' or double "" quotes.
    # multi-line strings can be specified with triple single ''' or double quotes """

    a = "Hello!"

    # single characters within a string can be returned using their positions in the array.

    # the first character is at position [0]
    print(a[0], a[5])

    # a string can be sliced by specifying a range of characters.
    print(a[1:4]) # the function returns characters from [1] to [4], but does not inlcude [4].

    # a string can be indexed from the end using negative indexing.
    print(a[-5:-1])

    return()

def booleans():
    # booleans return True or False after comparing two values.
    # use this script to test it yourself

    a = input("A: ")
    b = input("B: ")

    print("B = A: ", (b == a))
    print("B > A: ", (b > a))
    print("B < A: ", (b < a))

    return()

def operators():
    # operators are some of the most important aspects of any programming language. 
    # operators are used for arithmetic, assignment, comparison, logic, and many other functions.

    # assignment operators include =, +=, -=, *=, and /=
    # comparison operators include ==, !=, >, <, >=, and  <=
    # logical operators include and, or, and not
    # identity operators include is and is not
    # membership operators include in and not in
    # bitwise operators include &, |, ^, ~, <<, and >> (These will not be covered.)

    # arithmetic operators
    print(4, " + ", 5, " = ", (4 + 5)) # addition  
    print(4, " - ", 5, " = ", (4 - 5)) # subtraction
    print(5, " / ", 2, " = ", (5 / 2)) # division
    print(11, " % ", 5, " = ", (11 % 5)) # modulus (returns remainder after division)
    print(2, " ** ", 4, " = ", (2 ** 4)) # exponentiation
    print(11, " // ", 2, " = ", (11 // 2)) # floor division (returns the quotient of normal division rounded down.)
    print('\n')
    # comparison operators

    x = input("Choose the first of two numbers: ")
    y = input("Choose the second of two numbers: ")

    # we will cover if statements shortly. 
    # for now experiment with different values to learn the operators.
    if (x == y):
        print(x,' == ',y)
    else:
        print(x, ' != ', y)
    
    if (x > y):
        print(x, ' > ', y)
    elif(x < y):
        print(x, ' < ', y)
    else:
        pass

    # the remaining operator types will be covered in future lessons.

    return()

def lists():
    # to define a list, use [] square brackets.
    # this is the list we will be working with for the next few lessons.
    # for now, our list is simply a set of values.
    # these values are ordered and can be changed.
    list1 = ["apple","macbook", 3, 1299.99]

    print(list1)

    # specific items within a list can be accessed using indexing.
    print(list1[0]) 
    # this prints the first entry in the list.

    # lists can also be accessed using negative indexes.
    print(list1[-1])
    # this will print the last item in the list.

    # index ranges can be specified as well.
    print(list1[1:3])
    # this will print the second, third, and fourth list items.

    # to change a list item, we can assign a value to a specific index.
    list1[3] = 2399.00

    # to add a value to a list, use the append() method.
    list1.append("ordered")

    # to insert an item into a list, use the insert method.
    list1.insert(2, "pro")
    # the first value is the index, and the second is the value being inserted.

    # to remove an item, use the remove() method.
    list1.remove(3)
    # this will remove items based on value.

    # to remove a specific index, use pop()
    list1.pop()
    # if no index is specified, the last item will be removed.

    print(list1)

    # other methods for removing list items are available including del and clear()

    # to copy a list, you can use the copy() method or the list() method.

    return()

def tuples():
    # a tuple operates very similarly to a list; however, it is unchangable.

    # to create a tuple, use () parentheses.

    tuple1 = ("apple", "macbook", "pro", 2399.00)

    print(tuple1)

    return()

def sets():
    # sets are unordered and unindexed.
    # create a set with {} curly brackets.

    set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    print(set1)

    print(set1)

    # add items to a set using add(), remove items using remove().
    # add multiple items using update().

    set1.update([10, 11 ,12 ,13 , 14, 15, 16, 17, 18, 19, 20])

    print(set1)

    # pop() will remove a random item from the set.
    return()

def dictionaries():
    # dictionaries are unordered sets of key:value pairs.
    # create a dictionary using {} curly brackets.

    dict1 = {
        "brand": "apple",
        "model": "macbook",
        "trim": "pro",
        "price": 2399.00,
        "status": "ordered"
    }

    # items in a dictionary are indexed based on the key values.
    print(dict1["price"])

    # values can be changed by assigning the key index a new value.
    dict1["status"] = "arrived"

    print(dict1["status"])

    # key:value pairs can be added in the same way.
    dict1["working"] = "yes"

    print(dict1["working"])

    # remove items with pop("key") or del dict1["key"]

    # if needed, dictionaries can be nested.

    return()

def user_input():
    # to get user input, use the input() function.

    x = input("Type your name:")

    print(x)

    return()