from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Dashboard_Page import Dashboard
from System import System, Account

session1 = System(Account('did it work','maybe','i think it worked','working'))

app = QApplication(sys.argv)

window = Dashboard(session1.cont_userprofile)

window.show()
app.exec()