'''
196-QAbstractSpinBox-信号

editingFinished() -- 结束编辑时调用(失去焦点)
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QAbstractSpinBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('196-QAbstractSpinBox-信号')
        self.resize(1000, 500)

        asb = QAbstractSpinBox(self)
        asb.editingFinished.connect(lambda: print('结束编辑'))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
