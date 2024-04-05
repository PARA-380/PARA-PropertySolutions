# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import gui.rc_allicons
import gui.rc_images

from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DashBoard(object):
    def setupUi(self, DashBoard):
        DashBoard.setObjectName("DashBoard")
        DashBoard.resize(1033, 731)
        self.centralwidget = QtWidgets.QWidget(parent=DashBoard)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.signout_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.signout_btn.setFont(font)
        self.signout_btn.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/feather/log-out.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.signout_btn.setIcon(icon)
        self.signout_btn.setObjectName("signout_btn")
        self.horizontalLayout_3.addWidget(self.signout_btn)
        spacerItem = QtWidgets.QSpacerItem(588, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/Application.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(parent=self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.splitter)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/feather/user.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/feather/settings.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.splitter)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Properties_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Properties_btn.setFont(font)
        self.Properties_btn.setStyleSheet("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/feather/home.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Properties_btn.setIcon(icon3)
        self.Properties_btn.setCheckable(False)
        self.Properties_btn.setChecked(False)
        self.Properties_btn.setAutoRepeat(False)
        self.Properties_btn.setAutoExclusive(False)
        self.Properties_btn.setObjectName("Properties_btn")
        self.gridLayout.addWidget(self.Properties_btn, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/feather/bell.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.Tenants_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.Tenants_btn.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/feather/users.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.Tenants_btn.setIcon(icon5)
        self.Tenants_btn.setObjectName("Tenants_btn")
        self.gridLayout.addWidget(self.Tenants_btn, 0, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/feather/tool.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.splitter, 1, 0, 1, 1)
        DashBoard.setCentralWidget(self.centralwidget)

        self.retranslateUi(DashBoard)
        self.signout_btn.toggled['bool'].connect(DashBoard.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DashBoard)

    def retranslateUi(self, DashBoard):
        _translate = QtCore.QCoreApplication.translate
        DashBoard.setWindowTitle(_translate("DashBoard", "MainWindow"))
        self.signout_btn.setText(_translate("DashBoard", "Sign out"))
        self.label_2.setText(_translate("DashBoard", "WELCOME TO PARA PROPERTY SOLUTIONS - DASHBOARD"))
        self.pushButton_3.setText(_translate("DashBoard", "Profile"))
        self.pushButton_2.setText(_translate("DashBoard", "Settings"))
        self.Properties_btn.setText(_translate("DashBoard", "Properties"))
        self.pushButton_4.setText(_translate("DashBoard", "Notifications"))
        self.Tenants_btn.setText(_translate("DashBoard", "Tenants"))
        self.pushButton_5.setText(_translate("DashBoard", "Contractors"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DashBoard = QtWidgets.QMainWindow()
    ui = Ui_DashBoard()
    ui.setupUi(DashBoard)
    DashBoard.show()
    sys.exit(app.exec())
