#!/usr/bin/python3.4
import subprocess
from time import gmtime, strftime
import sys

device_ip = "10.82.16.141"
base = 0


def decodeResults(result):
   valueString=str(result.decode('utf-8'))
   valueString = valueString.replace('\n','')
   valueString = valueString.replace('\r',',')
   valueList=list(valueString.split(','))
#   print("===========>>", valueList, "<<====")
   return valueList
 

def getSPsessions(sp):
   cmd =list(('/home/lava/Trials/Scripts/TDHASH/mycommandNew' , str(sp)))
   result = subprocess.check_output(cmd)
   return decodeResults(result)

def getPercentage(base, cur):
   if base == 0:
     return 0
   precentage = (( cur - base) / base) * 100
   return precentage


def printVal(spno):
   global base
   mylist = getSPsessions(spno)
   for val in range(0,spno):
       numSess = int(mylist[val])
       if val == 0:
          base = numSess
       else :
          perc = getPercentage(base, numSess)
       print("sp", val+1," sessions ", numSess, end="")
       if val == 0:
          print("")
       else :
          print("\t\t %.2f %%" %( perc))

def main():
   print("==============================================   ", strftime("%Y-%m-%d %H:%M:%S", gmtime()))
   #print("==============================================")
   sp=1
   if len(sys.argv) == 2 :
      sp=int(sys.argv[1])
#   print("hi", sp)
   printVal(sp)


main()
#mylist=getSPsessions(6)
#print("====", mylist , "<<<<<<<<<")
#for val in range(0,6):
#   print("SP {} is {}".format(val+1, mylist[val]))
