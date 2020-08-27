# Don't worry about these, we will cover modules later!

import Lessons.basic as bas
import Lessons.logic as log
import Lessons.functions as fun
import Lessons.oop as oop
import Lessons.advanced as adv
import Lessons.files as fil

# This is a comment!

###########################################################################################
# In these notes I will be defining each lesson as a separate function.

# To start viewing the lessons, open the 2.basic.py file.

# To see the output of a lesson, uncomment that lesson's function in the main() function.
###########################################################################################
def main(): 
    
    print("Hello World!") # This is your first line of Python!
    # Indentation is important in Pythion.
    # For now, don't worry about it too much, but pay attention to indentation when you see it!

    #The notes officially start in the next file. 
    #When you're ready to see the output 
    def main_basic():
        #bas.variables()
        #bas.data_types()
        #bas.numbers()
        #bas.casting()
        #bas.strings()
        #bas.booleans()
        #bas.operators()
        #bas.lists()
        #bas.tuples()
        #bas.sets()
        #bas.dictionaries()
        #bas.user_input()
        return()
    main_basic()
    
    def main_logic():
        log.if_else()
        #log.while_loops()
        #log.for_loops()
        #log.try_except()
        return()
    main_logic()

    def main_functions():
        #fun.functions()
        #fun.lambda_functions()
        return()  
    main_functions()

    def main_oop():
        #oop.classes()
        #oop.objects()
        #oop.inheritance()
        #oop.iterators()
        #oop.modules()
        return()
    main_oop()

    def main_advanced():
        #adv.dates()
        #adv.math()
        #adv.json()
        #adv.regex()
        #adv.pip()
        #adv.string_formatting()
        return()
    main_advanced()

    def main_files():
        #fil.file_handling()
        #fil.read_files()
        #fil.write_files()
        #fil.delete_files()
        return()
    main_files()

    return()
main()

    

