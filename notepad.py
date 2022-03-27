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
    
    
    def show_notepad_components(self):
        """
        Create widgets for notepad GUI and arrange the in window.
        """
        # Create push Buttons for editing menu
        new_btn = QPushButton("New", self)
        new_btn.move(10, 20)
        new_btn.clicked.connect(self.clear_txt)
        save_btn = QPushButton("Save", self)
        save_btn.move(100, 20)
        save_btn.clicked.connect(self.save_text)
        
        # Create text edit field:
        self.text_field = QTextEdit(self)
        self.text_field.resize(480, 300)
        self.text_field.move(10, 60)
    
    def clear_txt(self):
        """
        If the new btn clicked, display asking user if they want to clear the text field or not.
        """
        confirm = QMessageBox.question(self,'Clear Confirm Message.','Are you sure want to clear text',QMessageBox.Yes,QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.text_field.clear()
            
    def save_text(self):
        """
        If the save is clicked, display dialog to save the text in the text edit field to a text file.
        """
        # Get and Convert value of QTextEdit to plaintext
        text = self.text_field.toPlainText()
        # We use spread variables
        file_name,_ = QFileDialog.getSaveFileName(self,'Save Text',"","All Files (*);;Text Files (*.txt);;Python Script (*.py)")
        if file_name:
            with open(file_name,'w',encoding='utf-8') as f:
                f.write(text)
                
            
    
    
# Execution lines
if __name__ == "__main__":
    app = QApplication(sys.argv)
    note_pad = NotePad()   
    sys.exit(app.exec_())

