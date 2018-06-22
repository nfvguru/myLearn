#!/usr/bin/python


def basic_function():
    """ Just some basic string samples """
    string1 = ' String 1 '
    string2 = " String 2 "
    string3 = """ String with
                 multi lines """
    print(" String 1 is  = {}".format(string1)) 
    print(" String 2 is  = {}".format(string2)) 
    print(" String 3 is  = {}".format(string3)) 



def example1():
    """ String Formatting """
    value1=10
    value2="Appu"
    print("I can format the string like value={}, Name={}".format(value1, value2))
    print("I can format the string like value={a}, Name={b}".format(a=value1, b = value2))
    print("I can format the string like value={1}, Name={0}".format(value2, value1))
    print('Old Style format, value=%d' %value1 )
    print('Old Style format, name=%(name)s, value=%(value)d' % {"value":value1, "name":value2} )
    print('Old Style format, name=%s, value=%d' % (value2, value1) )


def example2():
    """ String builtin functions  """
    mystring="Appu is a good boy . Number 1\t(Testing)"
    print(" Original      = {} ".format(mystring))
    print(" lower         = {} ".format(mystring.lower()))
    print(" upper         = {} ".format(mystring.upper()))
    print(" replace       = {} ".format(mystring.replace("good","bad")))
    splited=mystring.split()
    print(" split         = {} ".format(splited))
    print(" join - 1      = {} ".format("".join(splited)))
    print(" join - 2      = {} ".format(" ".join(splited)))
    print(" join - 3      = {} ".format("~".join(splited)))



########################################################################################

my_functions = [
   basic_function,
   example1,
   example2
]

def main() :
    if len(my_functions) == 0 :
        return
    for func in my_functions:
        print("======================  {} ====================".format(func.__doc__))
        func()


########################################################################################

main()

     
