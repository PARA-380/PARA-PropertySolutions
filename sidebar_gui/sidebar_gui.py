# Form implementation generated from reading ui file 'sidebar.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
from icon_rc import *

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1053, 797)
        MainWindow.setStyleSheet("background-color: rgb(245, 250, 254);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_image = QtWidgets.QWidget(parent=self.centralwidget)
        self.icon_image.setStyleSheet("QWidget{\n"
"    \n"
"    background-color: rgb(232, 133, 4);\n"
"}\n"
"\n"
"QPushButton{\n"
"     color: black;\n"
"    height:30;\n"
"    border:none;\n"
"    border-top-left-radius:10px;\n"
"    border-top-right-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #F5FAFE;\n"
"    color: black;\n"
"    font-weight:bold;\n"
"}")
        self.icon_image.setObjectName("icon_image")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_image)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(parent=self.icon_image)
        self.label.setMinimumSize(QtCore.QSize(40, 40))
        self.label.setMaximumSize(QtCore.QSize(40, 40))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/sidebar icon/user.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(17)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dashboard1 = QtWidgets.QPushButton(parent=self.icon_image)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dashboard1.setFont(font)
        self.dashboard1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/sidebar icon/grid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.dashboard1.setIcon(icon)
        self.dashboard1.setCheckable(True)
        self.dashboard1.setAutoExclusive(True)
        self.dashboard1.setObjectName("dashboard1")
        self.verticalLayout.addWidget(self.dashboard1)
        self.properties1 = QtWidgets.QPushButton(parent=self.icon_image)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.properties1.setFont(font)
        self.properties1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/sidebar icon/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.properties1.setIcon(icon1)
        self.properties1.setCheckable(True)
        self.properties1.setAutoExclusive(True)
        self.properties1.setObjectName("properties1")
        self.verticalLayout.addWidget(self.properties1)
        self.tenants1 = QtWidgets.QPushButton(parent=self.icon_image)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tenants1.setFont(font)
        self.tenants1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/sidebar icon/users.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tenants1.setIcon(icon2)
        self.tenants1.setCheckable(True)
        self.tenants1.setAutoExclusive(True)
        self.tenants1.setObjectName("tenants1")
        self.verticalLayout.addWidget(self.tenants1)
        self.contractors1 = QtWidgets.QPushButton(parent=self.icon_image)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contractors1.setFont(font)
        self.contractors1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/sidebar icon/tool.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.contractors1.setIcon(icon3)
        self.contractors1.setCheckable(True)
        self.contractors1.setAutoExclusive(True)
        self.contractors1.setObjectName("contractors1")
        self.verticalLayout.addWidget(self.contractors1)
        self.notifications1 = QtWidgets.QPushButton(parent=self.icon_image)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.notifications1.setFont(font)
        self.notifications1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/sidebar icon/bell.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.notifications1.setIcon(icon4)
        self.notifications1.setCheckable(True)
        self.notifications1.setAutoExclusive(True)
        self.notifications1.setObjectName("notifications1")
        self.verticalLayout.addWidget(self.notifications1)
        self.settings1 = QtWidgets.QPushButton(parent=self.icon_image)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.settings1.setFont(font)
        self.settings1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/sidebar icon/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.settings1.setIcon(icon5)
        self.settings1.setCheckable(True)
        self.settings1.setAutoExclusive(True)
        self.settings1.setObjectName("settings1")
        self.verticalLayout.addWidget(self.settings1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 361, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.signout1 = QtWidgets.QPushButton(parent=self.icon_image)
        self.signout1.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/sidebar icon/log-out.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.signout1.setIcon(icon6)
        self.signout1.setCheckable(True)
        self.signout1.setAutoExclusive(True)
        self.signout1.setObjectName("signout1")
        self.verticalLayout_3.addWidget(self.signout1)
        self.gridLayout.addWidget(self.icon_image, 0, 0, 1, 1)
        self.icon_bar = QtWidgets.QWidget(parent=self.centralwidget)
        self.icon_bar.setStyleSheet("QWidget{\n"
"background-color: rgb(232, 133, 4);\n"
"}\n"
"\n"
"QPushButton{\n"
"     color: black;\n"
"    text-align:left;\n"
"    height:30;\n"
"    border:none;\n"
"    padding-left:10px;\n"
"    border-top-left-radius:10px;\n"
"    border-top-right-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"    border-bottom-right-radius:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color: #F5FAFE;\n"
"    color: black;\n"
"    font-weight:bold;\n"
"}")
        self.icon_bar.setObjectName("icon_bar")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.icon_bar)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.icon_bar)
        self.label_2.setMinimumSize(QtCore.QSize(40, 40))
        self.label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/sidebar icon/user.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.icon_bar)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(9, 9, -1, -1)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.dashboard2 = QtWidgets.QPushButton(parent=self.icon_bar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dashboard2.setFont(font)
        self.dashboard2.setIcon(icon)
        self.dashboard2.setCheckable(True)
        self.dashboard2.setChecked(True)
        self.dashboard2.setAutoExclusive(True)
        self.dashboard2.setObjectName("dashboard2")
        self.verticalLayout_2.addWidget(self.dashboard2)
        self.properties2 = QtWidgets.QPushButton(parent=self.icon_bar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.properties2.setFont(font)
        self.properties2.setIcon(icon1)
        self.properties2.setCheckable(True)
        self.properties2.setAutoExclusive(True)
        self.properties2.setObjectName("properties2")
        self.verticalLayout_2.addWidget(self.properties2)
        self.tenants2 = QtWidgets.QPushButton(parent=self.icon_bar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tenants2.setFont(font)
        self.tenants2.setIcon(icon2)
        self.tenants2.setCheckable(True)
        self.tenants2.setAutoExclusive(True)
        self.tenants2.setObjectName("tenants2")
        self.verticalLayout_2.addWidget(self.tenants2)
        self.contractors2 = QtWidgets.QPushButton(parent=self.icon_bar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.contractors2.setFont(font)
        self.contractors2.setIcon(icon3)
        self.contractors2.setCheckable(True)
        self.contractors2.setAutoExclusive(True)
        self.contractors2.setObjectName("contractors2")
        self.verticalLayout_2.addWidget(self.contractors2)
        self.notifications2 = QtWidgets.QPushButton(parent=self.icon_bar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.notifications2.setFont(font)
        self.notifications2.setIcon(icon4)
        self.notifications2.setCheckable(True)
        self.notifications2.setAutoExclusive(True)
        self.notifications2.setObjectName("notifications2")
        self.verticalLayout_2.addWidget(self.notifications2)
        self.settings2 = QtWidgets.QPushButton(parent=self.icon_bar)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.settings2.setFont(font)
        self.settings2.setIcon(icon5)
        self.settings2.setCheckable(True)
        self.settings2.setAutoExclusive(True)
        self.settings2.setObjectName("settings2")
        self.verticalLayout_2.addWidget(self.settings2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 367, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.signout2 = QtWidgets.QPushButton(parent=self.icon_bar)
        self.signout2.setIcon(icon6)
        self.signout2.setCheckable(True)
        self.signout2.setAutoExclusive(True)
        self.signout2.setObjectName("signout2")
        self.verticalLayout_4.addWidget(self.signout2)
        self.gridLayout.addWidget(self.icon_bar, 0, 1, 1, 1)
        self.main_page = QtWidgets.QWidget(parent=self.centralwidget)
        self.main_page.setObjectName("main_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.header = QtWidgets.QWidget(parent=self.main_page)
        self.header.setObjectName("header")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.header)
        self.pushButton_15.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/sidebar icon/menu.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_15.setIcon(icon7)
        self.pushButton_15.setCheckable(True)
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout.addWidget(self.pushButton_15)
        spacerItem2 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_6 = QtWidgets.QLabel(parent=self.header)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        spacerItem3 = QtWidgets.QSpacerItem(138, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.header)
        self.pushButton_16.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/sidebar icon/user.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_16.setIcon(icon8)
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout.addWidget(self.pushButton_16)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.header)
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.main_page)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Dashboard = QtWidgets.QWidget()
        self.Dashboard.setObjectName("Dashboard")
        self.label_7 = QtWidgets.QLabel(parent=self.Dashboard)
        self.label_7.setGeometry(QtCore.QRect(130, 90, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.Dashboard)
        self.Property = QtWidgets.QWidget()
        self.Property.setObjectName("Property")
        self.label_8 = QtWidgets.QLabel(parent=self.Property)
        self.label_8.setGeometry(QtCore.QRect(120, 80, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.Property)
        self.Tenant = QtWidgets.QWidget()
        self.Tenant.setObjectName("Tenant")
        self.label_9 = QtWidgets.QLabel(parent=self.Tenant)
        self.label_9.setGeometry(QtCore.QRect(120, 60, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.stackedWidget.addWidget(self.Tenant)
        self.Contractor = QtWidgets.QWidget()
        self.Contractor.setObjectName("Contractor")
        self.label_10 = QtWidgets.QLabel(parent=self.Contractor)
        self.label_10.setGeometry(QtCore.QRect(120, 40, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.Contractor)
        self.Notification = QtWidgets.QWidget()
        self.Notification.setObjectName("Notification")
        self.label_11 = QtWidgets.QLabel(parent=self.Notification)
        self.label_11.setGeometry(QtCore.QRect(120, 20, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.Notification)
        self.Setting = QtWidgets.QWidget()
        self.Setting.setObjectName("Setting")
        self.label_12 = QtWidgets.QLabel(parent=self.Setting)
        self.label_12.setGeometry(QtCore.QRect(130, 60, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.stackedWidget.addWidget(self.Setting)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.main_page, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_15.toggled['bool'].connect(self.icon_image.setHidden) # type: ignore
        self.pushButton_15.toggled['bool'].connect(self.icon_bar.setVisible) # type: ignore
        self.dashboard2.toggled['bool'].connect(self.dashboard1.setChecked) # type: ignore
        self.dashboard1.toggled['bool'].connect(self.dashboard2.setChecked) # type: ignore
        self.properties2.toggled['bool'].connect(self.properties1.setChecked) # type: ignore
        self.properties1.toggled['bool'].connect(self.properties2.setChecked) # type: ignore
        self.tenants1.toggled['bool'].connect(self.tenants2.setChecked) # type: ignore
        self.tenants2.toggled['bool'].connect(self.tenants1.setChecked) # type: ignore
        self.contractors1.toggled['bool'].connect(self.contractors2.setChecked) # type: ignore
        self.contractors2.toggled['bool'].connect(self.contractors1.setChecked) # type: ignore
        self.notifications1.toggled['bool'].connect(self.notifications2.setChecked) # type: ignore
        self.notifications2.toggled['bool'].connect(self.notifications1.setChecked) # type: ignore
        self.settings1.toggled['bool'].connect(self.settings2.setChecked) # type: ignore
        self.settings2.toggled['bool'].connect(self.settings1.setChecked) # type: ignore
        self.signout1.toggled['bool'].connect(MainWindow.close) # type: ignore
        self.signout2.toggled['bool'].connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "MENU"))
        self.dashboard2.setText(_translate("MainWindow", "Dashboard"))
        self.properties2.setText(_translate("MainWindow", "Properties"))
        self.tenants2.setText(_translate("MainWindow", "Tenants"))
        self.contractors2.setText(_translate("MainWindow", "Contractors"))
        self.notifications2.setText(_translate("MainWindow", "Notifications"))
        self.settings2.setText(_translate("MainWindow", "Settings"))
        self.signout2.setText(_translate("MainWindow", "Sign Out"))
        self.label_6.setText(_translate("MainWindow", "PARA - Property Solutions"))
        self.label_7.setText(_translate("MainWindow", "Dashboard Page"))
        self.label_8.setText(_translate("MainWindow", "Properties Page"))
        self.label_9.setText(_translate("MainWindow", "Tenants Page"))
        self.label_10.setText(_translate("MainWindow", "Contractors Page"))
        self.label_11.setText(_translate("MainWindow", "Notification Page"))
        self.label_12.setText(_translate("MainWindow", "Settings Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
