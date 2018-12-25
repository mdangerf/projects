@echo off 

:start

echo Select a program to run...
echo Gmail - 1
echo Gdocs - 2
echo Gcalender - 3

set /p program=

if %program%==1 (
    python ENTER__DIR_HERE (i.e: D:\googleautomation\automations\gmail.py)
) else if %program%==2 (
    python ENTER__DIR_HERE (i.e: D:\googleautomation\automations\gdocs.py)
) else if %program%==3 (
    python ENTER_DIR_HERE (i.e: D:\googleautomation\automations\gcalender.py)
) else (
    echo invalid choice
    goto :start
)