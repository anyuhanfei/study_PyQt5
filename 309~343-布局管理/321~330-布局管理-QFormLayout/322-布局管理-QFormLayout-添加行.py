'''
322-布局管理-QFormLayout-添加行

addRow(self, QWidget, QWidget)
addRow(self, QWidget, QLayout)
addRow(self, str, QWidget)
addRow(self, str, QLayout)
addRow(self, QWidget)
addRow(self, QLayout)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFormLayout, QPushButton, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('322-布局管理-QFormLayout-添加行')
        self.resize(1000, 500)

        fl = QFormLayout()

        label_1 = QLabel('标签1')
        le_1 = QLineEdit()
        le_2 = QLineEdit()
        button = QPushButton('确认')

        fl.addRow(label_1, le_1)
        fl.addRow('标签2', le_2)
        fl.addRow(button)

        self.setLayout(fl)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
