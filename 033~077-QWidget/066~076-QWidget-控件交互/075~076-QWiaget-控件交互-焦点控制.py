'''
075~076-QWiaget-控件交互-焦点控制
'''
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel
from PyQt5.Qt import Qt


class Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('075~076_QWiaget_控件交互_焦点控制')
        self.move(200, 200)
        self.resize(900, 500)

        le_1 = QLineEdit(self)
        le_1.move(10, 10)

        le_2 = QLineEdit(self)
        le_2.move(10, 50)

        le_3 = QLineEdit(self)
        le_3.move(10, 90)

        le_4 = QLineEdit(self)
        le_4.move(10, 130)

        # 打开窗口时，le_2 获取焦点
        le_2.setFocus()

        # 只能点击获取焦点
        le_1.setFocusPolicy(Qt.ClickFocus)

        # 只能按 tab 键获取焦点
        le_2.setFocusPolicy(Qt.TabFocus)

        # 点击和 tab 键都可以获取焦点
        le_3.setFocusPolicy(Qt.StrongFocus)

        # 点击和 tab 键都不能获取焦点
        le_4.setFocusPolicy(Qt.NoFocus)

        # 获取子控件中获取焦点的那一个
        label = QLabel(self)
        label.move(10, 200)
        label.setText('当前获取焦点的子控件为：%s' % (self.focusWidget()))
        label.adjustSize()

        # 聚焦下一个子控件
        self.focusNextChild()

        # 聚焦上一个子控件
        self.focusPreviousChild()

        # 聚焦相邻子控件
        self.focusNextPrevChild(True)  # 下一个
        self.focusNextPrevChild(False)  # 上一个


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
