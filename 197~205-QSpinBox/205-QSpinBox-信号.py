'''
205-QSpinBox-信号

API:
    valueChanged(int i) -- 值改变时发送的信号
    valueChanged(QString text) -- 值改变时发送的信号 [str]

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSpinBox


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('205-QSpinBox-信号')
        self.resize(1000, 500)

        sb = QSpinBox(self)

        '''信号'''
        sb.valueChanged.connect(lambda i: print(type(i), i))
        sb.valueChanged[str].connect(lambda i: print(type(i), i))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
