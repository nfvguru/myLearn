#!/usr/bin/python
import pexpect
import re
import sys

myip="10.175.112.5"
#myip="10.82.16.141"
spDist=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ipthird=2
ipfourth=2
iplen=2

def getIPline():
   global ipthird
   global ipfourth
   ipfourth += 1
   if ipfourth > 255:
     ipfourth=1
     ipthird += 1
   ipbase="2.2."
   ipmask="255.255.255.255"
   return (ipbase + str(ipthird) + "." + str(ipfourth)+ " " + ipmask)

def spCount(buffer):
   global spDist
   printNextLine=0
   for line in buffer.splitlines(): 
     if re.search("====", line):
       printNextLine=1
       continue
     if printNextLine == 1:
       stats=line.split()
       spindex=int(stats[1])-1
       spDist[spindex] += 1
       print("IP={},\tSP={},\tTotal count on this SP= {}".format(stats[0],stats[1], spDist[spindex])) 
       break

def findvmasp(child):
   global iplen
   if len(sys.argv) == 2 :
      iplen=int(sys.argv[1])
   for i in range(1,iplen+1):
      vmaip=getIPline()
      vmacmd="/maint/debug/vmasp " + vmaip
      child.sendline(vmacmd)
      child.expect('Debug#')
      spCount(child.before)
   child.sendline('/')

def getPercentage(cur):
   precentage = (cur/(iplen * 1.0 )) * 100
   return precentage

def printResult():
   global spDist
   spind=1
   print("============= Distribution of SPs =========================")
   for spscount in spDist:
      perc = getPercentage(spscount)
      print "sp", spind, " IPs handled ", spscount,
      print("\t\t %.2f %%" %( perc))
      spind += 1
      



def doprocess():
   global myip
   child = pexpect.spawn("ssh admin@" + myip)
   child.expect('password:')
   child.sendline('admin')
   child.expect('Main#')
   findvmasp(child)
   child.expect('Main#')
   child.sendline('quit')
   printResult()


doprocess()

    
