#!/usr/bin/python3.4
import subprocess

device_ip = "10.82.16.141"
base = 0

def getSPsessions(sp):
   cmd =list(('/home/lava/Trials/Scripts/TDHASH/mycommand' , str(sp)))
#   print(cmd)
   result = subprocess.check_output(cmd)
   value = int(result.decode('utf-8'))
#   print(value)
   return value

def getPercentage(base, cur):
   if base == 0:
     return 0
   precentage = (( cur - base) / base) * 100
   return precentage


def printVal(spno):
   global base
   numSess = getSPsessions(spno)
   if spno == 1:
     base = numSess
   else :
     perc = getPercentage(base, numSess)
   print("sp", spno," sessions ", numSess, end="")
   if spno == 1:
     print("")
   else :
     print("\t\t %.2f %%" %( perc))

def main():
   print("==============================================")
   for i in range(1,7):
     printVal(i)


main()
