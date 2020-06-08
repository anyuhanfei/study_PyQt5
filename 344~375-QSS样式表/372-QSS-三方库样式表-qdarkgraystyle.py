'''
372-QSS-三方库样式表-qdarkgraystyle

'''
import sys

import qdarkgraystyle
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('372-QSS-三方库样式表-qdarkgraystyle')
        self.resize(1000, 500)

        label = QLabel('xxx')
        btn = QPushButton()

        bl = QVBoxLayout()

        bl.addWidget(label)
        bl.addWidget(btn)

        self.setLayout(bl)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    '''设置成暗黑效果'''
    app.setStyleSheet(qdarkgraystyle.load_stylesheet_pyqt5())

    sys.exit(app.exec_())
