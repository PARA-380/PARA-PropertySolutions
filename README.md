# PARA-PropertySolutions

For GUI Pyside6 and PyQt6 with QtDesigner:

Turning .ui file into .py:
pyuic6 -x nameof.ui -o nameof.py

Turning .qrc into .py (for the icon):
pyside6-rcc nameof.qrc -o nameof.py

don't forget to import the icon in the py file:
from icon_rc.py import *