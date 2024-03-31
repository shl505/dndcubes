import sys, os, random

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QPushButton,
                               QApplication,
                               QLabel,
                               QVBoxLayout,
                               QMainWindow,
                               QComboBox,
                               QWidget,
                               QRadioButton,
                               QSpinBox)
from PySide6.QtCore import QSize
import PySide6.QtGui

basedir = os.path.dirname(__file__)

class Cube:
    type_of_cube = 20
    # אם רגיל אז none, אם יתרון אז true ואם חסרון אז false
    is_advantage = None
    plus_number = 0
    # מספר הקוביות
    number_cubes = 1

    def roll(self):
        self.type_of_cube = dndcube.combobox2.currentText()
        if dndcube.radio_button1.isChecked():
            self.is_advantage = True
        elif dndcube.radio_button2.isChecked():
            self.is_advantage = False
        elif dndcube.radio_button3.isChecked():
            self.is_advantage = None

        outcome = random.randint(1, self.type_of_cube)
        return

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.advantage_or_disadvantage = "None"

        self.setFixedSize(QSize(250, 275))
        self.setWindowTitle('dnd cubes')
        # Create widgets
        self.button = QPushButton("roll")
        self.lable = QLabel('d')
        self.img = QLabel()
        self.combobox1 = QComboBox()
        self.combobox2 = QComboBox()
        self.lineedit = QSpinBox()
        self.lineedit.setMaximum(10)
        self.lineedit.setMinimum(0)
        self.radio_button1 = QRadioButton("Advantage")
        self.radio_button2 = QRadioButton("Disadvantage")
        self.radio_button3 = QRadioButton("None")

        # יצירת חיבורים לפונקציות
        self.button.clicked.connect(Cube.roll)
        self.lineedit.valueChanged.connect(self.entered_number)
        self.radio_button1.clicked.connect(self.advantagef)
        self.radio_button2.clicked.connect(self.disadvantagef)
        self.radio_button3.clicked.connect(self.no_advantage)

        self.combobox1.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.combobox2.addItems(['4', '6', '8', '10', '12', '20', '100'])

        layout = QVBoxLayout()
        layout.addWidget(self.combobox1)
        layout.addWidget(self.lable)
        layout.addWidget(self.combobox2)
        layout.addWidget(self.lineedit)
        layout.addWidget(self.button)
        layout.addWidget(self.radio_button1)
        layout.addWidget(self.radio_button2)
        layout.addWidget(self.radio_button3)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def roller(self):
        print("Hello")

    def advantagef(self):
        if (self.advantage_or_disadvantage != "False"):
            self.advantage_or_disadvantage = "True"
        print("clicked")

    def disadvantagef(self):
        if (self.advantage_or_disadvantage != "True"):
            self.advantage_or_disadvantage = "False"
        print("clicked1")

    def no_advantage(self):
        self.advantage_or_disadvantage = "None"
        print("None")

    def entered_number(self):
        if type(self.lineedit.text()) == int:
            self.plus_number = int(self.lineedit.text())
            print(self.plus_number)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    app.setWindowIcon(PySide6.QtGui.QIcon(os.path.join(basedir, 'Twenty_sided_dice.png')))

    dndcube = MainWindow()
    dndcube.show()
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    # Run the main Qt loop
    sys.exit(app.exec())



