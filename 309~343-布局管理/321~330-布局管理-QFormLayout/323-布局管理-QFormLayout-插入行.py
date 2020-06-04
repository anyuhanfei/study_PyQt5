'''
323-布局管理-QFormLayout-插入行

insertRow(self, int, QWidget, QWidget)
insertRow(self, int, QWidget, QLayout)
insertRow(self, int, str, QWidget)
insertRow(self, int, str, QLayout)
insertRow(self, int, QWidget)
insertRow(self, int, QLayout)


int 指定要插入位置的索引, 若添加的位置索引不存在, 则直接加在最后
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFormLayout, QPushButton, QLineEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('323-布局管理-QFormLayout-插入行')
        self.resize(1000, 500)

        fl = QFormLayout()

        label_1 = QLabel('标签1')
        le_1 = QLineEdit()
        le_2 = QLineEdit()
        le_3 = QLineEdit()
        button = QPushButton('确认')

        fl.addRow(label_1, le_1)
        fl.addRow('标签2', le_2)
        fl.addRow(button)

        '''插入行'''
        fl.insertRow(1, '标签3', le_3)

        self.setLayout(fl)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
