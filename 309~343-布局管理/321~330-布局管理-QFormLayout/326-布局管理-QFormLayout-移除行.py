'''
326-布局管理-QFormLayout-移除行

移除行(删除子控件)
    removeRow(self, int)
    removeRow(self, QWidget)
    removeRow(self, QLayout)
    romoveRow(self, QLayout)

移除行(不删除子控件)
    takeRow(self, int)->QFormLayout.TakeRowResult
    takeRow(self, QWidget)->QFromLayout.TakeRowResult
    takeRow(self, QLayout)->QFormLayout.TakeRowResult
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFormLayout, QLineEdit, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('326-布局管理-QFormLayout-移除行')
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

        fl.removeRow(0)

        '''移除,但不删除, 需要手动清理'''
        print(fl.takeRow(1))
        button.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
