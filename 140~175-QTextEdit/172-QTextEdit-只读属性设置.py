'''
172-QTextEdit-只读属性设置

仅仅限制用户操作

API:
    setReadOnly(self, bool) -- 设置是否只读
    isReadOnly() -> bool -- 获取是否是只读
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('172-QTextEdit-只读属性设置')
        self.resize(1000, 500)

        te = QTextEdit(self)
        te.setText('123456')

        '''设置是否只读'''
        te.setReadOnly(True)
        te.setText('abcdefg')

        '''获取是否只读'''
        print('当前是否是只读:', te.isReadOnly())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
