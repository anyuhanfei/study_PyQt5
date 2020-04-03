'''
121-QLineEdit-添加自定义行为

为文本框添加附加的行为操作，功能类似于 清空文本的按钮(120) 这样的功能，不过这个行为操作的图标、功能、展示位置都是可以自定义的

API
    addAction(QAction, QLineEdit.ActionPosition) -- 添加一个操作行为
    addAction(QIcon, QLineEdit.ActionPosition) -> QAction -- 另一种添加方式

QLineEdit.ActionPosition: 展示位置
    QLineEdit.LeadingPosition -- 前面
    QLineEdit.TrailingPosition -- 后面
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QAction
from PyQt5.QtGui import QIcon


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('121_QLineEdit_添加自定义行为')
        self.resize(1000, 500)

        self.le = QLineEdit(self)

        '''添加自定义行为'''
        # 方法一
        self.action_one = QAction(QIcon('./show.png'), '', self)
        self.action_one.triggered.connect(self._action)
        self.le.addAction(self.action_one, QLineEdit.LeadingPosition)

        # 方法二
        self.action_two = self.le.addAction(QIcon('./show.png'), QLineEdit.TrailingPosition)
        self.action_two.triggered.connect(self._action)

    def _action(self):
        '''显示或者隐藏输入内容'''
        mode = self.le.echoMode()
        if mode == 0:
            self.action_one.setIcon(QIcon('./hide.png'))
            self.action_two.setIcon(QIcon('./hide.png'))
            self.le.setEchoMode(2)
        else:
            self.action_one.setIcon(QIcon('./show.png'))
            self.action_two.setIcon(QIcon('./show.png'))
            self.le.setEchoMode(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
