#!/usr/bin/python

def basic():
   """ Some basic dict samples """
   mydict=dict([("lava", 10),("saji",20)])
   print(" My dict is     : {}".format(mydict))
   print(" value for lava : {}".format(mydict["lava"]))
   print(" value for saji : {}".format(mydict.get("saji")))
   try:
      print(" value for appu : {}".format(mydict["appu"]))
   except KeyError:
      print(" No such element ")
   print(" value for appu : {}".format(mydict.get("appu")))

functions = {
 "function1" : basic,
}

def main():
   if len(functions) == 0:
     return
   for item in functions:
     func=functions[item];
     print("== {} == {} =================".format(item, func.__doc__))
     func()

main()
