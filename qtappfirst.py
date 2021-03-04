#basic_window.py
# Import necessary modules

import sys #use sys to accept command-line arguments
from PyQt5.QtWidgets import QApplication, QWidget

class EmptyWindow(QWidget): 
    def __init__(self):
        super().__init__()# create default constructor for QWidget
        self.initializeUI()

    def initializeUI(self):
        """ Initialize the window and display its contents to the screen."""
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Empty window in PyQt')
        self.show()

#Run program
#Main method
if __name__ == '__main__':
    app = QApplication(sys.argv) # Create application object
    window = EmptyWindow()
    sys.exit(app.exec_()) # Start the event loop and use sys.exit to close the application