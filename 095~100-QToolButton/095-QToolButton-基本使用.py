'''
095-QToolButton-基本使用

一般情况下，窗口自上而下分别为，标题栏，菜单栏，工具栏，工作区，状态栏。QToolButton 就是设置工具栏中的按钮。

工具栏中提供快捷访问的工具按钮，通常只显示图标。

继承于 QAbstractButton。
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QToolButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class Window(QWidget):
    widget = 50

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('095_QToolButton_基本使用')
        self.resize(1000, 500)

        toolb = QToolButton(self)

        '''设置文本'''
        toolb.setText('工具')

        '''设置图标'''
        # 设置图标后文本消失
        icon = QIcon('./xxx.png')
        toolb.setIcon(icon)

        '''修改图标大小'''
        toolb.setIconSize(QSize(60, 60))

        '''提示文本'''
        toolb.setToolTip('这是一个工具')


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
