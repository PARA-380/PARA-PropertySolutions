from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QHBoxLayout, QMessageBox, QComboBox
)
from PyQt6.QtCore import Qt
import sys
# from tenantsUI_Controller import TenantsUI
# from src.gui.TenantPage_GUI. import Tenant

from src.gui.TenantPage_GUI.QtTenantPage import Ui_MainWindow

class tenantsui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.tableWidget.setColumnWidth(4, 600)
        self.tableWidget.setColumnWidth(2, 300)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(3, 200)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Tenant_page = tenantsui()
    Tenant_page.show()
    sys.exit(app.exec())