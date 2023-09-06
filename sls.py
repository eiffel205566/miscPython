'''
###This is a Screen Lock Preventer###
---------------------------------------
#How to use:
Place the __ScrnLockStopper decorator
to whichever function you would like
to run continuously
---------------------------------------
---------------------------------------
#Example:
#Function want to be ran indefinitely:
def RunMeForever():
    print('running indefinitely unless Ctrl + C')
    While True:
        pass
#Add decorator
import ScreenLockStopper as SLS
@SLS.__ScrnLockStopper
def RunMeForever():
    print('running indefinitely unless Ctrl + C')
    While True:
        pass
Now your function will run indefinitely without
worrying about it falling asleep
---------------------------------------
Reference:
https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate
'''

import ctypes

def _SetThreadState(states):
    ctypes.windll.kernel32.SetThreadExecutionState(states)


def __ScrnLockStopper(func,
                      SysStatContinue = 0x80000000,
                      SysStateRequire = 0x00000001,
                      SysScreenUp = 0x00000002):

    def inside(*args, **kwargs):
        _SetThreadState(SysStatContinue | SysStateRequire | SysScreenUp)
        ExpectResult = func(*args, **kwargs)
        return ExpectResult
    return inside

@__ScrnLockStopper
def run():
    while True:
        pass

@__ScrnLockStopper
def initialize():
    return 'done'


