import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QDialog
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
        self.setGeometry(1150, 150, 600, 700) #(x, y, width height)

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

        labels = [
            ("First Name", 130),
            ("Last Name", 180),
            ("Username", 230),
            ("Create Password", 280),
            ("Confirm Password", 330),
            ("Email", 380),
            ("Contact Number", 430)
        ]
        for label_text, y_position in labels:
            self.createTextbox(label_text, y_position)

        self.button_cancel = QPushButton('Cancel!', self)
        self.button_cancel.move(100, 500) # button.move(x,y)
        self.button_cancel.resize(150, 40)

        self.button_submit = QPushButton('Submit', self)
        self.button_submit.move(350, 500) # button.move(x,y)
        self.button_submit.resize(150, 40)

        self.button_submit.clicked.connect(self.show_processing_window)

        self.setCentralWidget(central_widget)
        self.show()

    def createTextbox(self, label_text, y_position):
        textbox = QLineEdit(self)
        textbox.move(310, y_position)
        textbox.resize(200, 40)
        textbox.setText(f"{label_text}: ")

        textbox_label = QLabel(label_text, self)
        textbox_label.move(110, y_position + 5)
        font = QFont("Arial", 10)
        textbox_label.setFont(font)

    def show_processing_window(self):
        self.processing_window = ProcessingWindow()
        self.processing_window.exec_()


class ProcessingWindow(QDialog):
    def __init__(self):
        super(). __init__()
        self.setWindowTitle("Data")
        self.setGeometry(1300, 200, 300, 200)

        self.message_label = QLabel("Application is ongoing, Please wait for a bit")
        font = QFont("Arial", 12)
        self.message_label.setFont(font)
        self.message_label.setAlignment(Qt.AlignCenter)

        layout - QVBoxLayout()
        layout.addWidget(self.message_label)
        self.setLayout(layout)

        self.setWindowModality(Qt.ApplicationModal)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = App()
    sys.exit(app.exec())