'''
053-QWidget-父子关系-API
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('053_QWidget_父子关系_API')
        self.resize(500, 500)
        self.move(200, 200)

        label_1 = QLabel(self)
        label_1.move(10, 10)
        label_1.setText('label 1')

        label_2 = QLabel(self)
        label_2.move(10, 50)
        label_2.setText('label 2')

        label_3 = QLabel(self)
        label_3.move(10, 90)
        label_3.setText('label 3')

        # 获取指定坐标位置的控件对象
        self.childAt(10, 50).setStyleSheet('background-color: red;')

        # 指定一个子控件，获取它的父控件对象
        label_1.parentWidget().setStyleSheet('background-color: yellow;')

        # 获取所有子控件组成的边界矩形（x, y, 宽, 高）
        print(self.childrenRect())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
