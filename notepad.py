# importing necessary modules:
import sys
from PyQt5.QtWidgets import(QApplication, QWidget, QPushButton, QTextEdit, QMessageBox, QFileDialog)

# Notepad class project below:
class NotePad(QWidget):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
    
    def initialize_ui(self):
        """
        Initialize the window for displaying its contents to the screen
        """
        self.setGeometry(100, 20, 500,700)
        self.setWindowTitle("4.1 - Notepad GUI by: Khaled")
        self.show_notepad_components()
    
    

