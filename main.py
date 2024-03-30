import sys, os
from PySide6.QtWidgets import (QCheckBox,
                               QPushButton,
                               QApplication,
                               QLabel,
                               QVBoxLayout,
                               QMainWindow,
                               QComboBox,
                               QWidget,
                               QLineEdit)
from PySide6.QtCore import QSize
import PySide6.QtGui

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.advantage_or_disadvantage = "None"

        self.setFixedSize(QSize(250, 185))
        self.setWindowTitle('dnd cubes')
        # Create widgets
        self.button = QPushButton("roll")
        self.lable = QLabel('d')
        self.combobox1 = QComboBox()
        self.combobox2 = QComboBox()
        self.advantage_checkbox = QCheckBox(text="advantage")
        self.disadvantage_checkbox = QCheckBox(text="disadvantage")
        self.lineedit = QLineEdit()
        self.lineedit.setMaxLength(10)
        self.lineedit.setPlaceholderText("Enter a number to plus")

        # יצירת חיבורים לפונקציות
        self.button.clicked.connect(self.roller)
        self.advantage_checkbox.stateChanged.connect(self.advantagef)
        self.lineedit.textEdited.connect(self.entered_number)

        self.combobox1.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        self.combobox2.addItems(['4', '6', '8', '10', '12', '20', '100'])

        layout = QVBoxLayout()
        layout.addWidget(self.combobox1)
        layout.addWidget(self.lable)
        layout.addWidget(self.combobox2)
        layout.addWidget(self.advantage_checkbox)
        layout.addWidget(self.disadvantage_checkbox)
        layout.addWidget(self.lineedit)
        layout.addWidget(self.button)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    # Greets the user
    def roller(self):
        print("Hello")

    def advantagef(self):
        if self.advantage_checkbox.isChecked() and (self.advantage_or_disadvantage != "False"):
            self.advantage_or_disadvantage = "True"

    def disadvantagef(self):
        if self.disadvantage_checkbox.isChecked() and (self.advantage_or_disadvantage != "True"):
            self.advantage_or_disadvantage = "False"

    def entered_number(self):
        self.plus_number = int(self.lineedit.text())
        print(self.plus_number)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    app.setWindowIcon(PySide6.QtGui.QIcon(os.path.join(basedir,'Twenty_sided_dice.png')))

    # Create and show the form
    dndcube = MainWindow()
    dndcube.show()
    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    # Run the main Qt loop
    sys.exit(app.exec())