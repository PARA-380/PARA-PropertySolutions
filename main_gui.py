from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Dashboard_Page import Dashboard



app = QApplication(sys.argv)

window = Dashboard()

window.show()
app.exec()