#!/usr/bin/python

def list_example1():
    print("=================== Example 1      ======================")
    list_one = [ 'one', 'two', 'three'];
    print(" My list is ", list_one)
    print(" First element", list_one[0])
    print(" Last element",  list_one[-1])
    

def list_example2():
    print("=================== Example 2      ======================")
   









#####  Add any new Function name to this list
my_functions = [
list_example1
               ]



#####  Main Program ######################################
def main_code():
    print("=================== Program Starts ======================")
    if my_functions == [] :
        return
    for function in my_functions :
        function()



#==================== Execution Starts Here ==============
main_code()
    
