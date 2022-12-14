'''
author: Egor Bakay <egor_bakay@inbox.ru>
write:  august 2022
modify: september 2022
'''

import subprocess # cmd
from threading import Thread
from time import time
import os
import os.path
from sys import platform
from time import sleep

#====================================================================================================================================================================================
#================================================================================= CONFIG ===========================================================================================
#====================================================================================================================================================================================

very_fast_crush = 5 # если проект крашится быстрее чем раз в n секунд, то он будет автоматически отключен
sleep_after_restart = 5 # n секунд программа спит, перед рестартом проекта

'''
path = ["D:/SERVER/cache/test.py",
        "D:/SERVER/operation/SuCCess/TelBotMain.py",
        "D:/SERVER/operation/box_distributor/TelBotMain.py",
        "D:/SERVER/cache/test.py"]
'''
#====================================================================================================================================================================================
#================================================================================= AUTO SET =========================================================================================
#====================================================================================================================================================================================

run_command = 0
if   platform.upper().find("LINUX")>-1: run_command = "python3 "
elif platform.upper().find("WIN")>-1:   run_command = "python "
else: 
    print("ERROR: unknown OC")
    exit()

config_path = __file__
while config_path[-1]!='/' and config_path[-1]!=chr(92):
    config_path = config_path[0:-1]
config_path += "config.txt"
#print("config_path:",config_path)

if not os.path.isfile(config_path):
    print("ERROR: not <config.txt> in catalog")
    exit()
file = open(config_path, "r")
path = file.readlines()
for i in range(0,len(path)):
    if path[i][-1]=='\n':
        path[i] = path[i][0:-1]
#print(path)
file.close()

#====================================================================================================================================================================================
#================================================================================= MAIN =============================================================================================
#====================================================================================================================================================================================

class StartServer(Thread):
    
    def __init__(self,python_path): 
        Thread.__init__(self)
        self.python_path = run_command + python_path
        self.python_path_folder = python_path
        #self.disk = python_path[0:2]
        i = len(self.python_path_folder)-1
        while self.python_path_folder[i]!='/' and self.python_path_folder[i]!=chr(92):
            i-=1
        self.python_main = run_command + self.python_path_folder[(i+1):]
        self.python_path_folder = self.python_path_folder[:i]
        #print(self.python_main)
        self.timer = 0
    
    def run(self): 
        print("START: " + self.python_path)
        while time()-self.timer>very_fast_crush: # чтобы если крашится чаще чем каждые 5 секунд, выключить это
            if self.timer!=0:
                print("ERROR and restart: " + self.python_path)
                sleep(sleep_after_restart)
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