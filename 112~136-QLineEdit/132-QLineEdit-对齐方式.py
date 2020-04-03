'''
132-QLineEdit-对齐方式

API:
    setAlignment(Qt.Alignment) -- 设置对齐方式
    alignment() -> Qt.Alignment -- 获取对齐方式

Qt.Alignment：
    Qt.AlignLeft -- 水平靠左
    Qt.AlignRight -- 水平靠右
    Qt.AlignHCenter -- 水平居中
    Qt.AlignJustify -- 文本两端对齐
    Qt.AlignTop -- 垂直靠上
    Qt.AlignBottom -- 垂直考下
    Qt.AlignVCenter -- 垂直居中
    Qt.AlignBaseline -- 基线对齐
    Qt.AlignCenter -- 垂直和水平都居中，等同于 Qt.AlignHCenter | Qt.AlignVCenter
    注：多种对齐方式同时设置，使用 '|' 符号连接
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('132_QLineEdit_对齐方式')
        self.resize(1000, 500)

        le = QLineEdit(self)
        le.resize(100, 100)
        le.move(10, 10)

        '''设置文本对齐方式'''
        le.setAlignment(Qt.AlignCenter)

        '''获取文本对齐方式'''
        print(le.alignment())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
