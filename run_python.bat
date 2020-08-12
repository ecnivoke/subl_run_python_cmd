@ECHO OFF
:: This batch will run a python file in cmd

set Dir=%1
set File=%2

TITLE Python from: %Dir%, File: %File%.py

if exist %Dir% (
	cd /d %Dir%
	call :runPythonFile

) else (
	echo %Dir% doesn't exist.
)

PAUSE

:: Call the File.py
:runPythonFile 		- runs a python file
	echo ============================================================
	echo Directory: %Dir%
	echo File: %File%.py
	echo ============================================================
	python %File%.py

EXIT /B
