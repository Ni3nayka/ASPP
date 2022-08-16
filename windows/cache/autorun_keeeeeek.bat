@ECHO OFF
echo project: keeeeeek
:METKA

IF EXIST D:\GitHub/box_distributor\src/TelBotMain.py (
	echo start project: keeeeeek
	D:
	cd D:/GitHub/box_distributor/src
	python TelBotMain.py
) ELSE (
	echo ERROR: no project - exit
	TIMEOUT 5
	exit
)
echo ERROR: project broke down - restart project
TIMEOUT 5

goto METKA
echo END
TIMEOUT 5
