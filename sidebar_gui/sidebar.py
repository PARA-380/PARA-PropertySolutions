from sidebar_gui import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

class Sidebar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Sidebar Menu")

        #Hide the icon with the description when opening the program first time
        self.icon_bar.setHidden(True)

        #calling methods-------------------------------------------

        self.dashboard1.clicked.connect(self.switch_to_dashboardPage)
        self.dashboard2.clicked.connect(self.switch_to_dashboardPage)

        self.properties1.clicked.connect(self.switch_to_propertiesPage)
        self.properties2.clicked.connect(self.switch_to_propertiesPage)

        self.tenants1.clicked.connect(self.switch_to_tenantsPage)
        self.tenants2.clicked.connect(self.switch_to_tenantsPage)

        self.contractors1.clicked.connect(self.switch_to_contractorsPage)
        self.contractors2.clicked.connect(self.switch_to_contractorsPage)

        self.notifications1.clicked.connect(self.switch_to_notificationsPage)
        self.notifications2.clicked.connect(self.switch_to_notificationsPage)

        self.settings1.clicked.connect(self.switch_to_settingsPage)
        self.settings2.clicked.connect(self.switch_to_settingsPage)

        #End calling methods--------------------------------------------

    #Adding method for switching pages
    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_propertiesPage(self):
        self.stackedWidget.setCurrentIndex(1)
    
    def switch_to_tenantsPage(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_contractorsPage(self):
        self.stackedWidget.setCurrentIndex(3)
    
    def switch_to_notificationsPage(self):
        self.stackedWidget.setCurrentIndex(4)
         
    def switch_to_settingsPage(self):
        self.stackedWidget.setCurrentIndex(5)