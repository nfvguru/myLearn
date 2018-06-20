#!/usr/bin/python

import sys

def list_example1():
    print("\n=================== Example 1      ======================")
    list_one = [ 'one', 'two', 'three'];
    print(" My list is    ", list_one)
    print(" First element ", list_one[0])
    print(" Last element  ", list_one[-1])
    

def list_example2():
    print("\n=================== Example 2      ======================")
    list_two = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 ]
    print(" My list is   " , list_two)
    print(" Slice 2:5 is " , list_two[2:5] )
    print(" Slice 2: is  " , list_two[2:] )
    print(" Slice :-3 is " , list_two[:-3] )
    print(" Slice 2:2 is " , list_two[2:2] )
   

def list_example3():
    print("\n=================== Example 3      ======================")
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
    print("\n=================== Example 4      ======================")
    ##  Methods of List Copy ########################################
    list_four = [ 1, 2, 3, 4 ]
    list_five = list_four
    if sys.version_info[0] <  3:
       list_six = list_four[:] 
    else:
       list_six  = list_four.copy()  # copy supported only in 3 or more
    list_seven = list_four[:]
    print(" list_four={},  list_five={},\n list_six={}, list_seven={}".format(
        list_four, list_five, list_six, list_seven))
    list_four.extend([5, 6, 7])
    print(" list_four={},  list_five={},\n list_six={}, list_seven={}".format(
        list_four, list_five, list_six, list_seven))
    

def list_example5():
    print("\n=================== Example 5      ======================")
    #   List comprehension Example , supported only in 3 or above
    my_list = [ 2 ** x for x in range(10)]
    print("List comprehension example list = {}".format(my_list))



def list_example6():
    print("\n=================== Example 6      ======================")
    #  Checking membership
    my_list = [ 1, 2, 3, 4, 5, 6]
    print ("Check if element 7 is a member = {} ".format( 7 in my_list))
    print ("Check if element 4 is a member = {} ".format( 4 in my_list))


def list_example7():
    print("\n=================== Example 7      ======================")
    mylist = [ "lava", "lalu", "laiju", "leela" ]
    en_list = enumerate(mylist);
    print(en_list) 
    print(list(en_list))
    print("\n")
    for item in enumerate(mylist, 10):
       print ("Item is {}".format(item))
    print("\n")
    for count, item in enumerate(mylist, 20):
       print ("Count is = {} , Item is {}".format(count, item))

def list_example8():
    print("\n=================== Example 8      ======================")
    mylist = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    print (" My list is = {}".format(mylist))
    print (" Length  is = {}".format(len(mylist)))
    print (" Max  is    = {}".format(max(mylist)))
    print (" Min  is    = {}".format(min(mylist)))
    print (" Sum  is    = {}".format(sum(mylist)))

#####  Add any new Function name to this list
my_functions = [
list_example1,
list_example2,
list_example3,
list_example4,
list_example5,
list_example6,
list_example7,
list_example8
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
    
