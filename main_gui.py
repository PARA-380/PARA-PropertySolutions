from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Dashboard_Page import Dashboard
from Login_Page_GUI import Login_Page

app = QApplication(sys.argv)

first_window = Login_Page()



main_window = Dashboard()

main_window.show()
app.exec()