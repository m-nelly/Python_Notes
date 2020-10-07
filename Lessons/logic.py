def if_else():
    # if statements are one of the most powerful tools in a programmer's arsenal. 
    # if statements evaluate a value againsta a condition, and executes code if the condition is met.
    a = input("a: ")
    b = input("b: ")

    if a > b:
        print(a," > ", b)
    elif a <= b:
        print(a, " <= ", b)
    else:
        print("Try again!")

    # the first condition will be evaluated and, if it is true, the code associated with it will be executed.
    # each consecutive condition will be evaluated provided the preceding conditions are false.
    # if all conditions are false, the else code will be executed. 
    # a condition can be ignored at any step by using the 'pass' keyword.

    c = input("c: ")

    if a > b and b >= c:
        print(a > c)
    else:  
        print("a cannot be determined to be greater than c")

    # this if statement evaluated two conditions at once using the 'and' operator.
    # 'or' can be used in similar fashion.

    if a > b or a > c:
        print('a is not the smallest number')
    else:
        print('a is the smallest number')

    return()

def while_loops():
    # while loops can be used to run the same bit of code for as long as a condition is true. 
    i = 1

    while i < 10:
        
        print(i)

        i+= 1
    else:
        i = 1
    # this loop will give us a list of numbers 1-10. 
    # the else statement in this case is optional.

    # we can break the loop before it is finished by using a break statement.

    while i <= 100:

        print(i)

        if i == 5:
            i = 0
            break

        i = ((i**i) + 1)
    else:
        i = 1

    #to execute code in the middle of a loop, use 'continue'
    while i < 100: 
        i += 1
        
        print(i)

        if i == 30:
            i = i + 60
            continue

    return()

def for_loops():
    # for loops can be used to loop through entities in a list, string, or range.
    # for loops work similarly to while loops, except over a set number of iterations.

    list1 = [1, 2, 3, 4, 5]
    
    for i in list1:
        print(i)
    # this loop will print each item in the list.

    str1 = "welcome"

    for x in str1:
        print("welcome")
    # this loop will print welcome for each character in str1.

    # you can break or continue a for loop the same way you do with a while loop.

    # when for loops are nested, the inner loop is executed for each iteration of the outer.

    for i in str1:
        for x in list1:
            print(i)

    # this loop will print five of each character in str1.

    return()

def try_except():
    # the try: block lets you test code for errors.
    # the except: block provides error handling.

    try:
        print(x)
    except:
        print("x is not defined!")

    # as a best practice, use these blocks to handle known potential errors.
    return()
