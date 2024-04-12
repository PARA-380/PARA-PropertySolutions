from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from Dashboard_Page import Dashboard
from System import System

from src.Entities.Account import Account

def run():
    app = QApplication(sys.argv)

    session = System(Account(first="Ridham", last="Petal", username="123", password="4560"))
    window = Dashboard(session.cont_userprofile)

    window.show()
    app.exec()

run()