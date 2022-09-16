'''
author: Egor Bakay <egor_bakay@inbox.ru>
write:  august 2022
modify: september 2022
'''

#  ONLY LINUX !!!

import subprocess # cmd
from threading import Thread
from time import time, sleep
import os
import os.path
from sys import platform
from datetime import datetime

#====================================================================================================================================================================================
#================================================================================= CONFIG ===========================================================================================
#====================================================================================================================================================================================

very_fast_crush = 0 # если проект крашится быстрее чем раз в n секунд, то он будет автоматически отключен
sleep_after_restart = 5 # n секунд программа спит, перед рестартом проекта
run_command = "python3 "

#====================================================================================================================================================================================
#================================================================================= AUTO SET =========================================================================================
#====================================================================================================================================================================================

if not platform.upper().find("LINUX")>-1: 
    print("===> ERROR: this is not LINUX OC")
    sleep(10)
    exit()
from os.path import abspath
config_path = os.path.abspath(__file__)#.replace(__file__, "config.txt")
while config_path[-1]!='/' and config_path[-1]!=chr(92):
    config_path = config_path[0:-1]
config_path += "config.txt"
print(config_path)

if not os.path.isfile(config_path):
    print("===> ERROR: not <config.txt> in catalog")
    sleep(10)
    exit()
file = open(config_path, "r")
path = file.readlines()
print(path)
for i in range(0,len(path)):
    if path[i][-1]=='\n':
        path[i] = path[i][0:-1]
#print(path)
file.close()

#====================================================================================================================================================================================
#================================================================================= MAIN =============================================================================================
#====================================================================================================================================================================================

def real_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")

class StartServer(Thread):
    
    def __init__(self,python_path): 
        Thread.__init__(self)
        self.python_path_basic = python_path
        self.python_path = run_command + python_path
        self.python_path_folder = python_path
        i = len(self.python_path_folder)-1
        while self.python_path_folder[i]!='/' and self.python_path_folder[i]!=chr(92):
            i-=1
        self.python_main = run_command + self.python_path_folder[(i+1):]
        self.python_path_folder = self.python_path_folder[:i]
        self.timer = 0
    
    def run(self): 
        print("===> START  (" + real_time() + "): " + self.python_path)
        while time()-self.timer>very_fast_crush: # чтобы если крашится чаще чем каждые 5 секунд, выключить это
            if self.timer!=0:
                print("===> ERROR and restart (" + real_time() + "): " + self.python_path)
                sleep(sleep_after_restart)
            self.timer = time()
            #subprocess.run(["python3",self.python_path_basic])
            #subprocess.call('python3 test.py', shell=True, cwd='/home/ni3mayka/Документы/GitHub/ASPP/universal/') 
            subprocess.call(self.python_main, shell=True, cwd=self.python_path_folder) 
            #print("===",self.python_path_basic,"===",self.python_path,"===",self.python_path_folder,"===",self.python_main)
            
        print("===> FATAL ERROR (" + real_time() + "): " + self.python_path)

threads = []
for a in path:
    threads.append(StartServer(a))
    threads[-1].start()

print("===> ALL SERVERS STARTED (" + real_time() + ")")
