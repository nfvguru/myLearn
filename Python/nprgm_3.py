#!/usr/bin/python

#########################  FUNCTIONS  ###############################
#1. Doc String Example
def docstring_sample():
    print("======================= Doc String Sample ===================================");
    def sample_function():
        """Function to show docstring"""
    print(sample_function.__doc__)


def variable_agrument_function_example():
    print("==================== Variable Argument Function Sample ======================");
    def va_function(*names):
       for name in names:
          print ( "given name is " + name )
    print("------------------------------")
    va_function("Lava", "Lalu")
    print("------------------------------")
    va_function("Johney", "Sabu","Varkey")


def recursion_example():
    print("==================== Recursion Example  =====================================");
    def rec_function( num ):
       if  num == 1 :
          return num
       return ( num * rec_function(num-1) )
    lnum = 4
    print ("Factorial of ", lnum, "is ", rec_function(lnum))


def string_format_example() :
    print("================== String Format Example ====================================");
    def string_format(names) :
        print (" First {}, Second {}, Third {}".format(names[0],names[1],names[2])) # default order
        print (" First {1}, Second {2}, Third {0}".format(names[0], names[1], names[2])) # positional order
        print (" First {a}, Second {b}, Third {c}".format(c = names[0],b = names[1],a = names[2])) # keyword order
    mynames = ("lava", "lalu", "kuttan")
    string_format(mynames)

   



#########################  Execuitons Starts Here ###################
docstring_sample()
variable_agrument_function_example()
recursion_example()
string_format_example()
