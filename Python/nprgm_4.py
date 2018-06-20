#!/usr/bin/python

import sys

def list_example1():
    print("=================== Example 1      ======================")
    list_one = [ 'one', 'two', 'three'];
    print(" My list is    ", list_one)
    print(" First element ", list_one[0])
    print(" Last element  ", list_one[-1])
    

def list_example2():
    print("=================== Example 2      ======================")
    list_two = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
    print(" My list is   " , list_two)
    print(" Slice 2:5 is " , list_two[2:5] )
    print(" Slice 2: is  " , list_two[2:] )
    print(" Slice :-3 is " , list_two[:-3] )
    print(" Slice 2:2 is " , list_two[2:2] )
   

def list_example3():
    print("=================== Example 3      ======================")
    list_three = [ 'a' ,'b' , 'c' , 'd']
    print (" My list is     " , list_three)
    print (" Print it twice " , 2 * list_three)
    list_three[1:3] = [ 1 , 2 ]
    print (" Replace 2 & 3  " , list_three)
    list_three[2:2] = [ 5, 6, 7, 8]
    print (" Insert Trick 1 " , list_three)
    list_three.append('k')
    print (" Append Method  " , list_three)
    list_three.extend([7, 8, 9])
    print (" Extend Method  " , list_three)
    list_three.insert(4, 'w')
    print (" Insert Method  " , list_three)
    del list_three[1:12]
    print (" Delete 1:12    " , list_three)
    list_three[1:4] = [ 9, 'c', 'd', 9 ]
    print (" Insert again   " , list_three)
    print (" count   9      " , list_three.count(9))
    print (" Index of 9     " , list_three.index(9))
    list_three.remove(9)
    print (" Remove Method  " , list_three)
    print (" Pop with index " , list_three.pop(3))
    print (" List after pop " , list_three)
    print (" Pop no index   " , list_three.pop())
    print (" List after pop " , list_three)
    
    if sys.version_info[0] <  3:
        list_three = []
    else :
        list_three.clear()   # Clear supported only in version 3
    print (" List clear     " , list_three)
    list_three.extend([1,3,2,5,4,7,6,9,8,0])
    print (" Fresh List     " , list_three)
    list_three.sort()
    print (" Sorted Lit     " , list_three)
    list_three.reverse()
    print (" Reversed Lit   " , list_three)

    

def list_example4():
    print("=================== Example 4      ======================")








#####  Add any new Function name to this list
my_functions = [
list_example1,
list_example2,
list_example3,
list_example4
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
    
