'''
author: Egor Bakay <egor_bakay@inbox.ru>
write:  august 2022
modify: september 2022
'''

from threading import Thread
from time import time,sleep
from datetime import datetime
import subprocess # cmd
from sys import platform

#====================================================================================================================================================================================
#================================================================================= CONFIG ===========================================================================================
#====================================================================================================================================================================================

very_fast_crush = 5 # если проект крашится быстрее чем раз в n секунд, то он будет автоматически отключен
sleep_after_restart = 5 # n секунд программа спит, перед рестартом проекта
NAME = "test" # для вывода в консоль
PATH = "test.py" # какой файл запускаем


#====================================================================================================================================================================================
#================================================================================= MAIN =============================================================================================
#====================================================================================================================================================================================

FLAG = 1

class StartServer(Thread):
    
    def __init__(self): 
        Thread.__init__(self)
        
    def run(self): 
        global FLAG
        FLAG = 1
        if platform.upper().find("LINUX")>-1:
            subprocess.run(["python3",PATH])
            # subprocess.run("python3 " + PATH) # linux - gavno
        else: #if platform.upper().find("WIN")>-1:
            subprocess.run("python " + PATH)
        FLAG = 0

now = datetime.now()

while 1:
    t = time()
    print("===> START SERVER (" + now.strftime("%H:%M:%S") + "): " + NAME)
    a = StartServer()
    a.start()
    while FLAG: pass
    sleep(1)
    if time()-t-1<very_fast_crush:
        print("===> FATAL ERROR (" + now.strftime("%H:%M:%S") + "): " + NAME + " - END SERVER")
        break
    else: print("===> ERROR (" + now.strftime("%H:%M:%S") + "): " + NAME + " - RESTART")
    sleep(sleep_after_restart)
