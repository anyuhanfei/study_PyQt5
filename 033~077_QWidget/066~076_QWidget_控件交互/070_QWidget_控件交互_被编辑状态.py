'''
070_QWidget_控件交互_被编辑状态
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700, 700)
        self.move(200, 200)

        # 标题中的中括号中的内容正常状态下是不会显示的,中括号可以放在任何位置，但是中括号内只能存放 * 号
        self.setWindowTitle('070_QWidget_控件交互_被编辑状态[*]')

        # 只有设置成被编辑状态时才会被显示
        self.setWindowModified(True)

        # 判断窗口是否处于被编辑状态
        print(self.isWindowModified())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
