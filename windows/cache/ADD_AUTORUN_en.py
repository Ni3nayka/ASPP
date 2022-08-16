'''
author: Egor Bakay <egor_bakay@inbox.ru>
write:  august 2022
modify: august 2022
'''

# PATH_PROJECT = "D:\GitHub/box_distributor\src/TelBotMain.py"
# NAME = "qwerty_2"
print("enter the full path to the file to run (D:/test/test.py)")
PATH_PROJECT = input()
print("enter the project name (just for beauty)")
NAME = input()

PATH_CMD = "autorun_" + NAME + ".bat"
print("put the file in the autorun folder? (if not, the file will remain in the directory of this executable) y[yes]/n[no]")
if input().upper()[0]=='Y':
    PATH_CMD = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Startup/" + PATH_CMD

operation_path = PATH_PROJECT.replace(chr(92),'/').split('/')
disk = operation_path[0]
path = disk + "/" + '/'.join(operation_path[1:-1])
py_file = operation_path[-1]

file = open(PATH_CMD, "w")

file.write("@ECHO OFF\n")
file.write("echo project: " + NAME + "\n")
file.write(":METKA\n")
file.write("\n")
file.write("IF EXIST " + PATH_PROJECT + " (\n")
file.write("	echo start project: " + NAME + "\n")
file.write("	" + disk + "\n")
file.write("	cd " + path + "\n")
file.write("	python " + py_file + "\n")
file.write(") ELSE (\n")
file.write("	echo ERROR: no project - exit\n")
file.write("	TIMEOUT 5\n")
file.write("	exit\n")
file.write(")\n")
file.write("echo ERROR: project broke down - restart project\n")
file.write("echo error data and time:\n")
file.write("date /T\n")
file.write("time /t\n")
file.write("TIMEOUT 5\n")
file.write("\n")
file.write("goto METKA\n")
file.write("echo END\n")
file.write("TIMEOUT 5\n")

file.close()
