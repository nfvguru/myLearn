#!/usr/bin/python

#################################### SAMPLE FUNCTIONS WILL BE WRITTEN BELOW ##########################

########################################################################################################
def add_example():
    print("===========add Example =================")
    a = 1
    b = 2
    sum = a + b
    print(sum)

########################################################################################################
def for_example():
    print("===========for Example =================")
    for i in range(1,11):
        if i == 3 :
            continue
        if i == 5 :
            break
        print(i)

########################################################################################################
def list_example():
    print("===========list Example =================")
    a = ['a', 'b', 'c' ]
    print(a)
    del a[1]
    print(a)

########################################################################################################
def reciprocal(a):
    if a == 5 :
        raise ValueError("I don't like this value")
        return
    try:
        num = 1 / a 
    except :
        print("Exception caught")
        raise ZeroDivisionError(" Zero")
        return
    print(num)
    raise TypeError("just for FUN")
    return


def except_example():
    print("==========Except Example ================")
    try :
        reciprocal(10)
        reciprocal(0)
        reciprocal(5)     
    except ZeroDivisionError:
        print("Zero Devision")
    except ValueError:
        print("Value Error")
    except TypeError:
        print("Type Error")
    else :
        print("My own Exception Caught")
    finally:
        print(" Done with Exception handling ")    
    
########################################################################################################
def for_name_example():
    print("======== For Name Example ===============")
    names = [ 'lava', 'prabhu', 'hanu', 'manoj' ]
    for i in names:
       print ('Hello ' + i )

########################################################################################################

lambda_test = lambda a,b: a * b 
def lambda_example():
    print("========= Lambda Example =================")
    print(lambda_test(2, 3))

########################################################################################################
def nonlocal_example() :
    print("======= Non local Example ================")
    a = 10
    print("a from Outer Fucntion" , a)
    def inner_function1():
        global a
        a = 5
        print("a from inner function 1" , a)

    def inner_function2():
        a = 15
        print("a from inner function 2" , a)
    inner_function2()
    print("a after first call" , a)
    inner_function1()
    print("a after second call" , a)
########################################################################################################

def while_example():
    print("=======   While Example   ================")
    a = 10
    while ( a ):
       print(a)
       a = a - 2
########################################################################################################

def with_example():
    print("=======    With Example   ================")
    with open('../Logs/lava_logs.txt', 'w') as fp :
        fp.write('Hi to Logs')

########################################################################################################
def generator_example():
    print("=======    Generator Example =============")
    g = ( 2**x for x in range(5))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
########################################################################################################

def yield_example():
    print("=======    Yield Example     =============")
    def mygenerator():
        for i in range(6) :
            yield i * i
    g = mygenerator()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    
'''########################################################################################################
#                           EXECUTION STARTS HERE .............
########################################################################################################'''

add_example()                        #  Simple Function to add
for_example()                        #  Function to demonstrte the use of for
list_example()                       #  Function to demonstrate the use of dic
except_example()                     #  Function to demonstrate the use of except
for_name_example()                   #  Function to demonstrate the use of for with strings
lambda_example()                     #  Function to demonstrate the use of  lambda
nonlocal_example()                   #  Function to demonstrate the use of nonlocal, but it was not supported 
                                     #  with the version I have. so used global instead, which is not working 
                                     #  expected
while_example()                      #  Function to demonstrate the use of while
with_example()                       #  Function to demonstrate the use of  with
generator_example()                  #  Function to demonstrate the use of  Generator
yield_example()                      #  Function to demonstrate the use of  yield
