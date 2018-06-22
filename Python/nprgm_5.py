#!/usr/bin/python


def function1():
    """ Simple Tuple Examples """
    my_tuple1 = ( 1, 2, "lava")
    print(" Tuple Example 1: {}".format(my_tuple1))
    my_tuple2 = 2 , 3, 4, 5
    print(" Tuple Example 2: {}".format(my_tuple2))
    a, b, c, d = my_tuple2
    print(" Unpacking Tuple\n\ta={}\n\tb={}\n\tc={}\n\td={}".format(a,b,c,d))


def function2():
    """ Immutable - Tuple  Demo"""
    mytuple = ( 1, 2, 3, 4)
    print("Contents of my mytuple = {}".format(mytuple))
    try :
      del mytuple[0]
    except TypeError :
      print("You can't delete an element from Tuple")
    print("Contents of my mytuple = {}".format(mytuple))

#############################################
my_functions = (
   function1,
   function2
)


def main():
    if len(my_functions) == 0 :
       return
    for funct in my_functions :
       print("============== {} ===============".format(funct.__doc__))
       funct()
    

##############################################
main()
