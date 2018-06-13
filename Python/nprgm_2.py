#!/usr/bin/python
print "Hello, Python!";

def add_example():
    print("===========add Example =================")
    a = 1
    b = 2
    sum = a + b
    print(sum)

def for_example():
    print("===========for Example =================")
    for i in range(1,11):
        if i == 3 :
            continue
        if i == 5 :
            break
        print(i)

def dict_example():
    print("===========dict Example =================")
    a = ['a', 'b', 'c' ]
    print(a)
    del a[1]
    print(a)

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
    print("===========Except Example =================")
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
    

add_example()
for_example()
dict_example()
except_example()
