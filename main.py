import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)
        self.create_ui()

    def create_ui(self):

        self.layout = QVBoxLayout()

        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setFixedHeight(50)
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setStyleSheet('font-size: 24px;')
        self.layout.addWidget(self.result_display)
        self.grid_layout = QGridLayout()
        self.buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]

        positions = [(i, j) for i in range(4) for j in range(4)]

        for position, button_text in zip(positions, self.buttons):
            button = QPushButton(button_text)
            button.setFixedSize(60, 60)
            button.setStyleSheet('font-size: 18px;')
            button.clicked.connect(self.on_button_click)
            self.grid_layout.addWidget(button, *position)

        self.layout.addLayout(self.grid_layout)
        self.setLayout(self.layout)

    def on_button_click(self):
        sender = self.sender().text()

        if sender == '=':
            try:
                result = eval(self.result_display.text())
                self.result_display.setText(str(result))
            except:
                self.result_display.setText('Error')
        else:
            self.result_display.setText(self.result_display.text() + sender)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
