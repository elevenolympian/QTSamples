#basic application
import sys, os.path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont, QPixmap


class QTUserProfile(QWidget): 
    def __init__(self): 
        super().__init__()

        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("2.1 - Anwendungsprofile Grafikschnittstelle")
        self.displayImages()
        self.displayUserInfo()

        #show the predefined GUI
        self.show()
    
    def displayImages(self):
        background_image = "images/skyblue.png"
        profile_image = "images/profile_image.png"

        try: 
            with open(background_image):
                background = QLabel(self)
                pixmap = QPixmap(background_image)
                background.setPixmap(pixmap)
        except:
            print("Image not found")

        try: 
            with open(profile_image):
                user_image = QLabel(self)
                pixmap = QPixmap(profile_image)
                user_image.setPixmap(pixmap)
                user_image.move(80, 20)
        except FileNotFoundError:
            print("Image not found")

    def displayUserInfo(self):
        user_name = QLabel(self)
        user_name.setText("Max Mustermann")
        user_name.move(85, 140)
        user_name.setFont(QFont('Arial', 20))

        bio_title = QLabel(self)
        bio_title.setText("Biographie")
        bio_title.move(15, 170)
        bio_title.setFont(QFont('Arial', 17))

        about = QLabel(self)
        about.setText("Ich bin ein Softwareentwickler, der mit 8 Jahre Erfahrung habe, indem wunderbare Quellcode schreibt")
        about.setWordWrap(True)
        about.move(15, 190)

        skills_title = QLabel(self)
        skills_title.setText("Fähigkeiten")
        skills_title.move(15, 240)
        skills_title.setFont(QFont('Arial', 17))

        skills = QLabel(self)
        skills.setText("Python  |  PHP  |  SQL  |  JavaScript")
        skills.move(15, 260)

        experience_title = QLabel(self)
        experience_title.setText("Experience")
        experience_title.move(15, 290)
        experience_title.setFont(QFont('Arial', 17))

        experience = QLabel(self)
        experience.setText("Python Entwickler")
        experience.move(15, 310)

        dates = QLabel(self)
        dates.setText("März 2011 - Weiterhin")
        dates.move(15, 330)
        dates.setFont(QFont('Arial', 10))

        experience = QLabel(self)
        experience.setText("Pizza Liefer Service")
        experience.move(15, 350)

        dates = QLabel(self)
        dates.setText("Aug 2015 - Dec 2017")
        dates.move(15, 370)
        dates.setFont(QFont('Arial', 10))

#Run the application
if __name__ == '__main__': 
    app = QApplication(sys.argv)
    window = QTUserProfile()
    sys.exit(app.exec_())