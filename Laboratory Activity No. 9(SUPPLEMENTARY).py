import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class App(QMainWindow):

    def __init__(self):
        super().__init__() #initializes the main window like in the window previous one
        #window = QMainWindow
        self.title = "Account Registration"
        self.initUI()

    def initUI(self):
        #Main Window
        self.setWindowTitle(self.title)
        self.setGeometry(700, 200, 600, 700) #(x, y, width height)

        # sets an icon
        self.setWindowIcon(QIcon('pythonico.ico'))

        # LABEL
        self.textboxlbl = QLabel("ACCOUNT REGISTRATION", self)
        font = QFont('Arial', 25, QFont.Bold)
        self.textboxlbl.setFont(font)


        #Size
        layout = QVBoxLayout()
        layout.addWidget(self.textboxlbl, alignment = Qt.AlignCenter | Qt.AlignTop )
        layout.setContentsMargins(40, 40, 40, 40) #(top, left, bottom, right)
        central_widget = QWidget(self)
        central_widget.setLayout(layout)

        # fields = [
        #     ("First Name: ", "Enter First Name: ", False),
        #     ("Last Name: ", "Enter Last Name: ", False),
        #     ("Username: ", "Enter Username: ", False),
        #     ("Create Password: ", "Enter Password: ", False),
        #     ("Confirm Password:  ", "Enter Password: ", False),
        #     ("Email: ", "Enter Email: ", False),
        #     ("Contact Number: ", "Enter Contact Number: ", False),
        # ]



        self.button = QPushButton('Cancel!', self)
        self.button.move(100, 600) # button.move(x,y)
        self.button.resize(150, 40)

        self.button = QPushButton('Submit', self)
        self.button.move(350, 600) # button.move(x,y)
        self.button.resize(150, 40)
        self.setCentralWidget(central_widget)

        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec())