'''
344-QSS-简介

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('344-QSS-简介')
        self.resize(1000, 500)

        box_1 = QWidget()
        box_2 = QWidget()
        box_1.setStyleSheet('background-color: red;')
        box_2.setStyleSheet('background-color: yellow;')

        bl = QVBoxLayout()

        bl.addWidget(box_1)
        bl.addWidget(box_2)

        self.setLayout(bl)

        label_1 = QLabel('标签1', box_1)
        label_1.move(10, 10)
        btn_1 = QPushButton('按钮1', box_1)
        btn_1.move(10, 50)

        label_2 = QLabel('标签2', box_2)
        label_2.move(10, 10)
        btn_2 = QPushButton('按钮2', box_2)
        btn_2.move(10, 50)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
