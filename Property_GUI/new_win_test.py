import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QApplication, QDialog, QLabel


class NewWindow(QDialog):
    def __init__(self, property_number):
        super().__init__()

        self.setWindowTitle(f"Property {property_number}")
        self.setMinimumSize(200, 200)

        self.layout = QVBoxLayout(self)
        self.label = QLabel(f"This is Property {property_number}'s window", self)
        self.layout.addWidget(self.label)