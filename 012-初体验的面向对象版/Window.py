from PyQt5.QtWidgets import QWidget, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('暗语寒飞')
        self.resize(500, 500)
        self.move(400, 200)

        self.setup_label_hw()

    def setup_label_hw(self):
        '''设置一个标签'''
        label = QLabel(self)
        label.setText('Hello World')
        label.move(200, 200)
