'''
author: Egor Bakay <egor_bakay@inbox.ru>
write:  august 2022
modify: august 2022
'''

import subprocess # cmd
from threading import Thread
from time import time
import os

#====================================================================================================================================================================================
#================================================================================= CONFIG ===========================================================================================
#====================================================================================================================================================================================

path = ["D:/SERVER/cache/test.py",
        "D:/SERVER/operation/SuCCess/TelBotMain.py",
        "D:/SERVER/operation/box_distributor/TelBotMain.py",
        "D:/SERVER/cache/test.py"]



#====================================================================================================================================================================================
#================================================================================= MAIN =============================================================================================
#====================================================================================================================================================================================

class StartServer(Thread):
    
    def __init__(self,python_path): 
        Thread.__init__(self)
        self.python_path = "python " + python_path
        self.python_path_folder = python_path
        #self.disk = python_path[0:2]
        i = len(self.python_path_folder)-1
        while self.python_path_folder[i]!='/' and self.python_path_folder[i]!=chr(92):
            i-=1
        self.python_main = "python " + self.python_path_folder[(i+1):]
        self.python_path_folder = self.python_path_folder[:i]
        #print(self.python_main)
        self.timer = 0
    
    def run(self): 
        print("START: " + self.python_path)
        while time()-self.timer>5: # чтобы если крашится чаще чем каждые 5 секунд, выключить это
            if self.timer!=0:
                print("ERROR and restart: " + self.python_path)
            self.timer = time()
            #subprocess.run(self.python_path)
            subprocess.run(self.python_main,cwd=self.python_path_folder)
            
        print("FATAL ERROR: " + self.python_path)

# file = open(str(os.getcwd())+"D:/SERVER/config.txt", "r")
# path = file.read().split('\n')
# file.close()

threads = []
for a in path:
    threads.append(StartServer(a))
    threads[-1].start()

print("ALL SERVERS STARTED")