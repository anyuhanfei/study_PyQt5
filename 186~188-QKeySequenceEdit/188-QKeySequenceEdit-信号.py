'''
188-QkeySequenceEdit-信号

API:
    editingFinished() -- 结束编辑时发射
    keySequenceChanged(QKeySequence  keySequence) -- 键位序列改变时发射

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QKeySequenceEdit


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('188-QkeySequenceEdit-信号')
        self.resize(1000, 500)

        kse = QKeySequenceEdit(self)

        '''信号'''
        kse.editingFinished.connect(lambda: print('结束编辑'))
        kse.keySequenceChanged.connect(lambda key: print('键位序列改变', key.toString()))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
