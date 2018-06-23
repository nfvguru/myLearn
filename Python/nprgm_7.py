#!/usr/bin/python



def basic():
    """ Basic Set Examples  """
    set1 = { 1, 2,1,3,4,5,6,(7,6,5) }
    print(" Set -set1- is  {}".format(set1))
    set2 = set([3,4,5,6,7,8,"appu",(3,4,5)])
    print(" Set -set2- is  {}".format(set2))
    set3 = set()
    print(" Set -set3- is  {}".format(set3))
 
def basic_ops():
    """ Basic Operations for Set """
    set1 = { 1, 2, 3, 4, 5 }
    print(" Original set   =  {}".format(set1))
    set1.add(6)
    print(" Method add     =  {}".format(set1))
    set1.update([7,8,9])
    print(" Method update  =  {}".format(set1))
    set1.discard(9)
    print(" Method discard =  {}".format(set1))
    set1.remove(8)
    print(" Method remove  =  {}".format(set1))
    try:
        set1.remove(8)
    except KeyError:
        print(" There is no such element in set")
    else :
        print(" Method remove  =  {}".format(set1))
    print(" Method pop     =  {}".format(set1.pop()))
    print(" Method pop     =  {}".format(set1.pop()))
    print(" set after pop  =  {}".format(set1))
    set1.clear()
    print(" set after clear=  {}".format(set1))

def check_sets(set1, set2):
    print(" ==============================================================")
    print(" set1.isdisjoint(set2)     =  {}".format(set1.isdisjoint(set2)))
    print(" set1.issubset(set2)       =  {}".format(set1.issubset(set2)))
    print(" set1.issuperset(set2)     =  {}".format(set1.issuperset(set2)))
    print(" ==============================================================")
    

def more_set_ops():
    """ More Operations on Set """
    set1 = { 1, 2, 3, 4, 5 }
    print(" Set 1                     =  {}".format(set1))
    set2 = { 3, 4, 5, 6, 7 }
    print(" Set 2                     =  {}".format(set2))
    print(" Union of set1 and Set2 -1 =  {}".format(set1|set2))
    print(" Union of set1 and Set2 -2 =  {}".format(set1.union(set2)))
    print(" Intersection  -1          =  {}".format(set1&set2))
    print(" Intersection  -2          =  {}".format(set1.intersection(set2)))
    print(" Difference S1-S2   -1     =  {}".format(set1 - set2))
    print(" Difference S2-S1   -1     =  {}".format(set2 - set1))
    print(" Difference S1-S2   -2     =  {}".format(set1.difference(set2)))
    print(" Difference S2-S1   -2     =  {}".format(set2.difference(set1)))
    print(" Set 1                     =  {}".format(set1))
    print(" Set 2                     =  {}".format(set2))
    check_sets(set1, set2)    
    
    set1.difference_update(set2)      
    print(" ======== Afer set1.difference_update(set2) ===")
    print(" Set 1                     =  {}".format(set1))
    print(" Set 2                     =  {}".format(set2))
    check_sets(set1, set2)    
    
    set1.update([3,4,5])
    print(" Set updated with [3,4,5]  =  {}".format(set1))
    set1.intersection_update(set2)
    print(" ======== Afer set1.intersection_update(set2) ===")
    print(" Set 1                     =  {}".format(set1))
    print(" Set 2                     =  {}".format(set2))
    check_sets(set1, set2)    

    set1.update([1,2])
    print(" Set updated with [1,2]    =  {}".format(set1))
    print(" Set1.symmetric_difference(set2)   =  {}".format(set1.symmetric_difference(set2)))
    set1.symmetric_difference_update(set2)
    print(" ======== Afer set1.symmetric_difference_update(set2) ===")
    print(" Set 1                     =  {}".format(set1))
    print(" Set 2                     =  {}".format(set2))
    


def frozenset_example ():
    """ Fronzenset Example """
    set1=set([2,3,4,5,6])
    set2=frozenset([2,3,4,5,6])
    print(" Set 1                     =  {}".format(set1))
    print(" Set 2                     =  {}".format(set2))
    set1.add(1)
    print(" Add 1 to set1             =  {}".format(set1))
    try:
      print(" ==> Try to add 1 to set2")
      set2.add(1)
    except AttributeError:
      print(" ==> Can't add any element to set2") 

##############################################
myfunc = {
   basic,
   basic_ops,
   more_set_ops,
   frozenset_example
}

def main():
   if len(myfunc) == 0 :
      return
   for func in myfunc :
      print("============================ {} ====================".format(func.__doc__))
      func()

##############################################
main()
