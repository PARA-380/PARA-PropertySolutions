from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Property_main import Property_Page

app = QApplication(sys.argv)

window = Property_Page()

window.show()
app.exec()