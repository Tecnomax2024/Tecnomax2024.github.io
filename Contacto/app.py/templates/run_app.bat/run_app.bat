@echo off

REM Crea un entorno virtual utilizando virtualenv
python -m pip install virtualenv
python -m virtualenv venv

REM Activa el entorno virtual
venv\Scripts\activate  REM En Windows
source venv/bin/activate  REM En Linux/Mac

REM Instala las dependencias
python -m pip install Flask Flask-Mail Flask-WTF

REM Ejecuta la aplicación Flask
python app.py

REM Mantén la ventana abierta para ver mensajes
pause
