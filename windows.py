from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel

import sys

from tools.read_settings import get_settings

class MainWindow(QMainWindow):
    """
    
    """
    def __init__(self, name, fontsize):
        super().__init__()

        self.setWindowTitle = "Test"

        lbl1 = QLabel(f"Hello {name}!", self)

        button = QPushButton("Press!", self)
        button.clicked.connect(self.test_event)

        button.move(30, 30)

        self.setFixedSize(QSize(400, 300))

        #self.setCentralWidget(button)
    
    def test_event(self):
        print("Clicked")

class SettingsWindow(QWidget):
    """
    
    """
    def __init__(self):
        super().__init__()

name, fontsize, window_x, window_y = get_settings("settings.json")

app = QApplication([])

window = MainWindow(name, fontsize)
window.show()

app.exec()