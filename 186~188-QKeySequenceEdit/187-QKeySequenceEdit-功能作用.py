'''
187-QKeySequenceEdit-功能作用

API:
    setKeySequence(QKeySequence keySequence) -- 设置键的序列
    keySequence() -> QKeySequence -- 获取键的序列
    clear() -- 清除
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QKeySequenceEdit
from PyQt5.QtGui import QKeySequence
from PyQt5.Qt import Qt


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('187-QKeySequenceEdit-功能作用')
        self.resize(1000, 500)

        kse = QKeySequenceEdit(self)

        '''设置一个键位序列'''
        ks = QKeySequence('Ctrl+I')
        ks = QKeySequence(QKeySequence.Find)
        ks = QKeySequence(Qt.CTRL + Qt.ALT + Qt.Key_I)

        '''将键位序列输入到控件中'''
        kse.setKeySequence(ks)

        '''获取控件中的键位序列'''
        print('控件中的键位序列:', kse.keySequence().toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
