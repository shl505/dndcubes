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


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.advantage_or_disadvantage = "None"

        self.setFixedSize(QSize(250, 275))
        self.setWindowTitle('D&D Cubes')
        # Create widgets
        self.button = QPushButton("roll")
        self.lable = QLabel('d')
        self.lable2 = QLabel('Enter a number to plus')
        self.combobox1 = QComboBox()
        self.combobox2 = QComboBox()
        self.lineedit = QSpinBox()
        self.lineedit.setMaximum(10)
        self.lineedit.setMinimum(0)
        self.radio_button1 = QRadioButton("Advantage")
        self.radio_button2 = QRadioButton("Disadvantage")
        self.radio_button3 = QRadioButton("None")
        self.lable3 = QLabel('outcome')

        # יצירת חיבורים לפונקציות
        self.button.clicked.connect(Cube.roll)

        self.combobox1.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.combobox2.addItems(['4', '6', '8', '10', '12', '20', '100'])

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.combobox1)
        self.layout.addWidget(self.lable)
        self.layout.addWidget(self.combobox2)
        self.layout.addWidget(self.lable2)
        self.layout.addWidget(self.lineedit)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.radio_button1)
        self.layout.addWidget(self.radio_button2)
        self.layout.addWidget(self.radio_button3)
        self.layout.addWidget(self.lable3)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)


class Cube:

    def roll(self):

        type_of_cube = int(dndcube.combobox2.currentText())

        # אם רגיל אז none, אם יתרון אז true ואם חסרון אז false
        is_advantage = "None"
        plus_number = int(dndcube.lineedit.text())
        # מספר הקוביות
        number_cubes = int(dndcube.combobox1.currentText())

        if dndcube.radio_button1.isChecked():
            is_advantage = "True"
        elif dndcube.radio_button2.isChecked():
            is_advantage = "False"
        elif dndcube.radio_button3.isChecked():
            is_advantage = "None"
        outcome = 0
        for i in range(0, number_cubes):
            outcome = outcome + random.randint(1, type_of_cube)
        output = int(outcome)

        if is_advantage == "True":
            outcome2 = random.randint(1, type_of_cube)
            if outcome2 > outcome:
                output = outcome2
            else:
                output = outcome
        elif is_advantage == "False":
            outcome2 = random.randint(1, type_of_cube)
            if outcome2 > outcome:
                output = outcome
            else:
                output = outcome2

        dndcube.lable3.setText(str(output + plus_number))
        return str(output + plus_number)


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



