:: fchooser.bat
:: launches a folder chooser and outputs choice to the console
:: https://stackoverflow.com/a/15885133/1683264

@echo off
setlocal

set "psCommand="(new-object -COM 'Shell.Application')^
.BrowseForFolder(0,'Please choose a folder.',0,0).self.path""

for /f "usebackq delims=" %%I in (`powershell %psCommand%`) do set "folder=%%I"

setlocal enabledelayedexpansion

del pos_tmp.txt


opencv_annotation.exe --annotations=pos_tmp.txt --images=!folder!

for /f "delims=" %%a in (pos_tmp.txt) do (
	set word=!folder!\
	set str=%%a
	call set str=%%str:!word!=%%
	echo !str! >> !folder!/pos.txt
)
endlocal
:: ../../../img/positive/

PAUSE