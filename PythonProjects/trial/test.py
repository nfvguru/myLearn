from lConnect import lUtils


def testDevice(utils):
   IP="10.82.43.189"
   DPW="admin1"
   handler=utils.getDeviceHandler(IP,DPW)
   ipline=utils.runCommand(handler, "/info/sys/mgmt", "System#", "255.255")
   print("IP line is: " ,ipline)
   ipline=utils.runCommand(handler, "/maint/debug/prepdbg/watcher dis", "debug#", "state")
   print("Watcher: " ,ipline)
   ipline=utils.runCommand(handler, "/maint/debug/prepdbg/watcher ena", "debug#", "state")
   print("Watcher: " ,ipline)
   utils.closeDeviceHandler(handler)

def testUlp(utils):
   #IP="10.82.16.100"
   IP="10.82.43.189"
   uHandler=utils.getUlpHandler(IP,'\$')
   utils.runUlpCommand(uHandler, "ls -lrt", '\$')
   utils.runUlpCommand(uHandler, "ps -ef | grep mp.elf | grep -v grep", '\$')
   utils.closeUlpHandler(uHandler)


def main():
   utils = lUtils();
   testDevice(utils)
   testUlp(utils)


main()
