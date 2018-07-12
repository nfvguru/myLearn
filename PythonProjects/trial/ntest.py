import pexpect
import re

def myExpect(handler, expected, optional, opt_answers):
    expList=expected
    maxtrial=2
    limit=len(expList) 
    print("limit is " + str(limit))
    expList.extend(optional)
    matchindex=handler.expect(expList)
    #matchindex=len(expList) - 1
    print ("===> Opt is " + str(matchindex))
    print(handler.before)
    while matchindex >= limit :
       handler.sendline(opt_answers[matchindex-limit])
       matchindex=handler.expect(expList)
       print("answer is " + opt_answers[matchindex-limit] )
       #matchindex -= 1
       print ("===> Opt is " + str(matchindex))
       print(handler.before)
       maxtrial -= 1
       if maxtrial == 0 :
          break

def chumma3():
     IP="10.82.43.189"
     child = pexpect.spawn("ssh -p 6188 radware@" + IP)
     myExpect(child,['password'], ['\?'], ['yes'])
     child.sendline('radware')
     myExpect(child,['\$'],[], [])
     child.sendline('exit')
      
	
    

def chumma2():
     IP="10.82.43.189"
     child = pexpect.spawn("ssh admin@" + IP)
     myExpect(child,['password'], ['\?'], ['yes'])
     child.sendline('admin1')
     myExpect(child,['Main#'], ['y]:'], ['y'])
     child.sendline('quit')
     myExpect(child,['closed\.', 'pipe'], ['n]: '], ['y'])


def chumma():
    IP="10.82.43.187"
    child = pexpect.spawn("ssh admin@" + IP)
    expList=["password:","\?"]
    matchindex=child.expect(expList)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Opt 1 is " + str(matchindex))
    print(child.before)
    if matchindex != 0:  
        child.sendline('yes')
        child.expect('password:')
    child.sendline('admin1')
    expList=['Main#', 'y]:']
    matchindex=child.expect(expList)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Opt 2 is " + str(matchindex))
    print(child.before)
    if matchindex != 0 :
        child.sendline('y')
        child.expect('Main#')
        print(child.before)
    child.sendline('quit')
    expList=['closed\.','pipe','n]: ']
    matchindex=child.expect(expList)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> opt 3 is " + str(matchindex))
    print(child.before)
    while matchindex >= 2:
         child.sendline('y')
         matchindex=child.expect(expList)
         print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> opt 4 is " + str(matchindex))
         print(child.before)


#chumma()
#chumma2()
chumma3()
    
      

      
