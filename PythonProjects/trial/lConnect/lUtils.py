import pexpect
import re

class lUtils:
    def __init__(self):
       return

    def myExpect(self, handler, expected, optional, opt_answers):
        expList=expected
        maxtrial=5
        limit=len(expList)
        expList.extend(optional)
        matchindex=handler.expect(expList)
        while matchindex >= limit :
            handler.sendline(opt_answers[matchindex-limit])
            matchindex=handler.expect(expList)
            maxtrial -= 1
            if maxtrial == 0 :
                break

    def getDeviceHandler(self,IP,PW):
       child = pexpect.spawn("ssh admin@" + IP)
       self.myExpect(child,['password'], ['\?'], ['yes'])
       child.sendline(PW)
       self.myExpect(child,['Main#'], ['y]:'], ['y'])
       return child

    def closeDeviceHandler(self,handler):
       handler.sendline('quit')
       self.myExpect(handler,['closed\.', 'pipe'], ['n]: '], ['y'])

    def getUlpHandler(self,IP,prompt):
       child = pexpect.spawn("ssh -p 6188 radware@" + IP)
       self.myExpect(child,['password'], ['\?'], ['yes'])
       child.sendline('radware')
       child.expect(prompt)
       return child

    def closeUlpHandler(self,handler):
       handler.sendline('exit')

    def matchMyPattern(self,buffer, pattern):
       printNextLine=0
       for line in buffer.splitlines():
          if re.search(pattern, line):
              return line
       return None
          
    def runCommand(self, handler, cmd, prompt, searchStr):
       handler.sendline(cmd)
       handler.expect(prompt)
       matchline=self.matchMyPattern(handler.before,searchStr)
       handler.sendline("/")
       handler.expect('Main#')
       return matchline


    def runUlpCommand(self, handler, cmd, prompt):
       handler.sendline(cmd)
       handler.expect(prompt)
       print(handler.before)

