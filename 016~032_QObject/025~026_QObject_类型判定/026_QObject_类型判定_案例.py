'''
026_QObject_类型判定_案例

创建一个窗口, 包含多个QLabel或其他控件, 将包含在窗口内所有的QLabel控件, 设置背景色cyan
'''
import sys

from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('026_QObject_类型判定_案例')
        self.resize(500, 500)

        self.index()

    def index(self):
        label1 = QLabel(self)
        label1.setText('label 1')
        label1.move(10, 10)

        label2 = QLabel(self)
        label2.setText('label 2')
        label2.move(10, 40)

        btn1 = QPushButton(self)
        btn1.setText('button 1')
        btn1.move(10, 70)

        # self.findChildren(QLabel) 此方法返回 self 对象中的所有 Qlabel 控件(也是一种方法，但因与本章无关，所以不用)
        # 获取所有控件，并判断控件的父类是否是 QLabel 来判定此控件是否是 QLabel 控件
        for widget in self.children():
            if widget.inherits('QLabel') is True:
                widget.setStyleSheet("background-color: cyan;")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
