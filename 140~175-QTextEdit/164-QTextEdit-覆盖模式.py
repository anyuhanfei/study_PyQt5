'''
164-QTextEdit-覆盖模式

当在光标处输入新的文本时, 并且光标之后已经有文本了, 若采用覆盖模式, 会覆盖旧的文本

API:
    setOverwriteMode(bool) -- 设置覆盖模式
    overwriteMode() -> bool -- 获取覆盖模式
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('164-QTextEdit-覆盖模式')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.setText('123456789')

        # 改一下光标位置
        te_cursor = te.textCursor()
        te_cursor.setPosition(4)
        te.setTextCursor(te_cursor)

        '''设置覆盖模式'''
        te.setOverwriteMode(True)

        '''获取覆盖模式'''
        print('是否是覆盖模式:', te.overwriteMode())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
