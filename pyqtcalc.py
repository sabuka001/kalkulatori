import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("kalkulator.py")
        self.setFixedSize(300, 200)
        self.initUI()

    def initUI(self):
        self.current = ''
        frame = QVBoxLayout()
        self.display = QLineEdit('0')
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        font = self.display.font()
        font.setPointSize(font.pointSize() + 8)
        self.display.setFont(font)

        frame.addWidget(self.display)
        grid = QGridLayout()
        grid.setSpacing(5)
        frame.addLayout(grid)
        self.setLayout(frame)
        names = [
            'qleari', 'kurva', 'daxurva', u"\N{DIVISION SIGN}", '7', '8', '9',
            u"\N{MULTIPLICATION SIGN}", '4', '5', '6', '-', '1', '2', '3', '+',
            '0', '00', '.', '='
        ]

        positions = [(i, j) for i in range(5) for j in range(4)]
        for position, name in zip(positions, names):
            if name == '':
                continue
            button = QPushButton(name)
            button.resize(10, 10)
            button.clicked.connect(self.press_btn)
            grid.addWidget(button, *position)

    def press_btn(self):
        button_text = self.sender()
        if button_text.text() == 'qleari':
            self.current = ''
            self.display.setText(self.current)
        elif button_text.text() == 'kurva':
            self.current = self.current[:-1]
            self.display.setText(self.current)
        elif button_text.text() == 'daxurva':
            self.close()
        elif button_text.text() == '=':
            try:
                if u"\N{DIVISION SIGN}" in self.current:
                    self.current = self.current.replace(
                        u"\N{DIVISION SIGN}", '/')
                elif u"\N{MULTIPLICATION SIGN}" in self.current:
                    self.current = self.current.replace(
                        u"\N{MULTIPLICATION SIGN}", "*")
                self.current = str(eval(self.current))
                self.display.setText(self.current)
            except Exception as e:
                QMessageBox.about(self, 'kalkulaturi ambobs rom ',
                                  'nu cughlutob chqim jim da nu gveghadavebi, nulze ver gayof')
        else:
            self.current += button_text.text()
            self.display.setText(self.current)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
