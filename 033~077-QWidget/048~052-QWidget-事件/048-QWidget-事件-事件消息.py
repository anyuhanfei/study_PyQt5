'''
048-QWidget-事件-事件消息
'''

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class Window(QWidget):
    y = 10

    def __init__(self):
        super().__init__()
        self.setWindowTitle('048_QWidget_事件_事件消息')
        self.resize(700, 700)
        self.move(200, 200)

    def showEvent(self, QShowEvent):
        '''展示窗口时的事件函数'''
        self._input_content('窗口展示了')

    def closeEvent(self, QCloseEvent):
        '''关闭窗口时的事件函数'''
        self._input_content('窗口关闭了')

    def moveEvent(self, QMoveEvent):
        '''移动窗口时的事件函数'''
        self._input_content('窗口移动了')

    def resizeEvent(self, QResizeEvent):
        '''控件大小调整的事件函数'''
        self._input_content('窗口大小改变了')

    def enterEvent(self, QEvent):
        '''鼠标进入的事件函数'''
        self._input_content('鼠标进入了窗口')

    def leaveEvent(self, QEvent):
        '''鼠标离开的事件函数'''
        self._input_content('鼠标离开了窗口')

    def mousePressEvent(self, QMouseEvent):
        '''鼠标按下的事件函数'''
        self._input_content('鼠标被按下了')

    def mouseReleaseEvent(self, QMouseEvent):
        '''鼠标释放的事件函数'''
        self._input_content('鼠标被释放了')

    def mouseDoubleClickEvent(self, QMouseEvent):
        '''鼠标双击的事件函数'''
        self._input_content('鼠标双击了')

    def mouseMoveEvent(self, QMouseEvent):
        '''鼠标跟踪的事件函数'''
        self._input_content('鼠标按下时被移动了')

    def keyPressEvent(self, QKeyEvent):
        '''键盘按下的事件函数'''
        self._input_content('键盘被按下了')

    def keyReleaseEvent(self, QKeyEvent):
        '''键盘释放的事件函数'''
        self._input_content('键盘被释放了')

    def focusInEvent(self, QFocusEvent):
        '''焦点获取的事件函数'''
        self._input_content('焦点被获取了')

    def focusOutEvent(self, QFocusEvent):
        '''焦点失去的事件函数'''
        self._input_content('焦点已经失去了')

    def dragEnterEvent(self, QDragEnterEvent):
        '''拖拽进入的事件函数'''
        self._input_content('拖拽进入了窗口')

    def dragLeaveEvent(self, QDragLeaveEvent):
        '''拖拽离开的事件函数'''
        self._input_content('拖拽离开了窗口')

    def dragMoveEvent(self, QDragMoveEvent):
        '''拖拽移动的事件函数'''
        self._input_content('拖拽在窗口中移动')

    def dragEvent(self, QDragEvent):
        '''拖拽放下的事件函数'''
        self._input_content('拖拽被放下了')

    def paintEvent(self, QPaintEvent):
        '''显示控件，更新控件的事件函数'''
        # self._input_content('控件更新了')

    def changeEvent(self, QEvent):
        '''控件改变的事件函数'''
        self._input_content('控件改变了')

    def contextMenuEvent(self, QContextMenuEvent):
        '''访问右键菜单的事件函数'''
        self._input_content('右键点击了')

    def inputMethodEvent(self, QInputMethodEvent):
        '''输入法调用的事件函数'''
        self._input_content('输入法被调用了')

    def _input_content(self, content):
        label = QLabel(self)
        label.setText(content)
        label.move(10, self.y)
        label.resize(200, 20)
        label.show()
        self.y += 20


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
