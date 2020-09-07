'''
Find window study notes:

Typical tasks include:

1. Find a specific window
2. Close that window
3. Click specific button of that window



'''

import win32gui
import win32api
import time
import win32con
from multiprocessing import Process
from selenium import webdriver
_driver = r'C:\Automation\chromedriver.exe'

def getDriver(driver=_driver):
    return webdriver.Chrome(Driver)


def WindowEnnumerationHandler(hwnd, top_windows):
    #hwnd: top window handle, returned by win32gui.FindWindow(None, Window Name)
    #top_windows is simply a god damn list where you put result of the function in
    #dont know why people are using this stupid and confusing name
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    

'''
win32gui.EnumChildWindows(top_level_handle_an_integer, a_callback_function, a_list_as_container)

if you pass top level handle (an integer) to above function
then it will output all the cihldwindow and elements in the container

'''

def runModule(windowText='Error Loading Extension', buttonText='OK'):
    #Check for parent window to show up
    while True:
        ParentWindowID = win32gui.FindWindow(None, windowText)
        if ParentWindowID==0:
            time.sleep(1)
            print(f'Parent Window {windowText} hasnt show up yet')
            continue
        else:
            break
    #Cihld Windows Container
    ChildWindowList = []
    win32gui.EnumChildWindows(ParentWindowID, WindowEnnumerationHandler, ChildWindowList)
    TargetID = list(filter(lambda x: x[1] == buttonText, ChildWindowList))[0][0]

    while True:
        if win32gui.FindWindow(None, windowText) != 0:
            time.sleep(1)
            print(f'Parent Window {windowText} still exist! wait 1 sec and re-click ok')
            win32gui.SendMessage(TargetID, win32con.BM_CLICK, 0, 0)
            continue
        else:
            break
    print('finish')
    return

def decoratorClickOk(func):
    def inside(*args,**kwargs):
        p = Process(target=runModule,args=())
        p.start()
        result = func(*args, **kwargs)
        return result
    return inside

    
        
        

    
