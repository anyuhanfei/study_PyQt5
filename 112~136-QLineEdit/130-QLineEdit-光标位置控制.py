'''
130-QLineEdit-光标位置控制

用代码控制输入框中的光标位置，API 都是可执行方法

API：
    cursorBackward(bool mark，int steps = 1) -- 向后(左)移动steps个字符
    cursorForward(bool mark，int steps = 1) -- 向前(右)移动steps个字符
    cursorWordBackward(bool mark) -- 向后(左)移动一个单词长度
    cursorWordForward(bool mark) -- 向前(右)移动一个单词长度
    home(bool mark) -- 移动到行首
    end(bool mark) -- 移动到行尾
    setCursorPosition(int) -- 设置光标位置
    cursorPosition() -- 获取光标位置
    cursorPositionAt(const QPoint＆ pos) -- 获取指定坐标位置对应文本光标位置
    注：
        mark: True -- 带选中效果
        mark: False -- 不带选中效果
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('130_QLineEdit_光标位置控制')
        self.resize(1000, 500)

        self.le = QLineEdit(self)
        self.le.move(10, 10)
        self.btn = QPushButton('按钮', self)
        self.btn.move(10, 40)
        self.btn.clicked.connect(self._cursor)

    def _cursor(self):
        '''向后移动两位(其他方法类似)'''
        self.le.cursorBackward(False, 2)

        # 点击按钮后，输入框焦点失去，给一下焦点
        self.le.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
