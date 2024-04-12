import sys
from PyQt6.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QPushButton,
  QVBoxLayout,
  QWidget,
)
class AnotherWindow(QWidget):
  
  """
  This "window" is a QWidget. If it has no parent, it
  will appear as a free-floating window.
  """
  def __init__(self):
    super().__init__()
    button = QPushButton("Push for going back")
    button.clicked.connect(self.back_to_main)
    layout = QVBoxLayout()
    layout.addWidget(button)
    self.setLayout(layout)
    """
    self.label = QLabel("Another Window")
    layout.addWidget(self.label)
    self.setLayout(layout)
    """
  def back_to_main(self, checked):
    self.m = MainWindow()
    self.m.show()
    self.close()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        self.w = AnotherWindow()
        self.w.show()
        self.close()
    
app = QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())