echo off
color
cls
echo hai gia' installato python?
choice
if %ERRORLEVEL% == 1 goto:packages
if %ERRORLEVEL% == 0 goto:python
echo.
echo per qualsiasi problema apri il file supporto.vbs nella cartella di juno.
echo.
pause
:ext
cls
echo.
echo per qualsiasi problema consulta supporto.vbs, e' anche offline!
echo.
pause
exit

:python
color
echo installing python
cls
cd C:\Users\%username%\Downloads\Juno2.3\
quickwin.vbs
cd "\Program Files (x86)\Google\Chrome\Application"
start chrome https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe
cd ..
cd ..
goto:packages
goto:ext

:packages
color
echo.
echo sto installando i pacchetti...
echo.
color 0a
pip install arcade
pip install SpeechRecognition
pip install Tkinter
pip install googlesearch
pip install google
pip install gtts
pip install playsound
goto:ext