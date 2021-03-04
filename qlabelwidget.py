#qlabelwidget.py
#import necessary modules

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
import pathlib

class ImageWindow(QWidget): 
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """ Initialize UI with the window and display its contents to the screen. """ 
        self.setGeometry(100, 100, 250, 250)
        self.setWindowTitle('QLabelExample')
        self.displayLabels()

        self.show()

    def displayLabels(self): 
        """Display text and images using QLabels"""
        text = QLabel(self)
        text.setText("Image sample")
        text.move(105, 15)
        print("hello images")
        print("current filepath", pathlib.Path(__file__).parent.absolute())
        image = "/images/world.png"
        try:
            with open(image):
                world_image = QLabel(self)
                pixmap = QPixmap(image)
                world_image.setPixmap(pixmap)
                world_image.move(25, 40)
        except FileNotFoundError:
            print("The world image file cannot be found")

#Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ImageWindow()
    sys.exit(app.exec_())