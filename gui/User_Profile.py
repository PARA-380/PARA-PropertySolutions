# Form implementation generated from reading ui file 'User_Profile.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 738)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(70, 52, 258, 327))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_2 = QtWidgets.QSplitter(parent=self.widget)
        self.splitter_2.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(parent=self.splitter_2)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.splitter_2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.splitter_2)
        self.splitter = QtWidgets.QSplitter(parent=self.widget)
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(parent=self.splitter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.splitter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_4 = QtWidgets.QSplitter(parent=self.widget)
        self.splitter_4.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_3 = QtWidgets.QLabel(parent=self.splitter_4)
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.splitter_4)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.splitter_4)
        self.splitter_3 = QtWidgets.QSplitter(parent=self.widget)
        self.splitter_3.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_4 = QtWidgets.QLabel(parent=self.splitter_3)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.splitter_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.splitter_3)
        self.splitter_5 = QtWidgets.QSplitter(parent=self.widget)
        self.splitter_5.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.pushButton = QtWidgets.QPushButton(parent=self.splitter_5)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.splitter_5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.splitter_5)
        self.textEdit = QtWidgets.QTextEdit(parent=self.widget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "First_name"))
        self.label_3.setText(_translate("MainWindow", "Last_name"))
        self.label_4.setText(_translate("MainWindow", "Phone Number"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Numeric only"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Display Info "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
