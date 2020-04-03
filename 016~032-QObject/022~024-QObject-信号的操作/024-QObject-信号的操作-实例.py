'''
024-QObject-信号的操作-实例

1. 当用户点击按钮的时候, 打印"点我嘎哈?"

2. 在所有修改的窗口标题前, 添加前缀"撩课-"
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # 修改标题信号 连接 槽函数
        self.windowTitleChanged.connect(self._add_prefix)
        # 修改标题
        self.setWindowTitle('example 1')
        # 再次修改标题
        self.setWindowTitle('example 2')
        self.set_ui()

    def set_ui(self):
        self.set_button()

    def set_button(self):
        btn = QPushButton(self)
        btn.setText('点击我')
        btn.clicked.connect(self._button_slot)

    def _button_slot(self):
        '''槽函数
        点击按钮时打印一句话
        '''
        print('点我嘎哈?')

    def _add_prefix(self, str=''):
        '''槽函数
        修改标题时，在标题前添加标题前缀

        若仅仅是重新设置标题内容的话，修改标题的信号已经和此槽函数连接，会造成死循环；
        可以先取消连接，重新设置标题后，重新连接；也可以临时阻断信号
        '''
        # method one
        self.windowTitleChanged.disconnect()
        self.setWindowTitle('撩课-%s' % (str))
        self.windowTitleChanged.connect(self._add_prefix)

        # method two
        self.blockSignals(True)
        self.setWindowTitle('撩课-%s' % (str))
        self.blockSignals(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
