import sys, os
from PySide6.QtWidgets import (QCheckBox, QPushButton, QApplication, QLabel,
                               QVBoxLayout, QMainWindow, QComboBox, QWidget)
import PySide6.QtGui, PySide6.QtCore

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.advantage_or_disadvantage = None
        self.advantage = False
        self.disadvantage = False
        # Create widgets
        self.button = QPushButton("roll")
        self.lable = QLabel('d')
        # Create layout and add widgets
        layout = QVBoxLayout()
        self.button.clicked.connect(self.greetings)
        combobox1 = QComboBox()
        combobox2 = QComboBox()
        self.advantage_checkbox = QCheckBox(text="advantage")
        disadvantage_checkbox = QCheckBox(text="disadvantage")
        combobox1.addItems(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
        combobox2.addItems(['4', '6', '8', '10', '12', '20', '100'])

        layout.addWidget(combobox1)
        layout.addWidget(self.lable)
        layout.addWidget(combobox2)
        layout.addWidget(self.advantage_checkbox)
        layout.addWidget(disadvantage_checkbox)
        layout.addWidget(self.button)
        widget = QWidget()
        widget.setLayout(layout)
        self.advantage_checkbox.stateChanged.connect(self.advantagef)
        self.setCentralWidget(widget)



    # Greets the user
    def greetings(self):
        print("Hello")

    def advantagef(self):
        self.advantage = not self.advantage
        if self.advantage == True:
            self.advantage_or_disadvantage = True

    def disadvantagef(self):
        self.disadvantage = not self.advantage1
        if self.advantage == True:
            self.advantage_or_disadvantage = False


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    app.setWindowIcon(PySide6.QtGui.QIcon(os.path.join(basedir,'Twenty_sided_dice.png')))

    # Create and show the form
    dndcube = MainWindow()
    dndcube.show()
    # Run the main Qt loop
    sys.exit(app.exec())