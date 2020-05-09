'''
290-QLCDNumber-溢出判定和信号

API:
    checkOverflow(self, float) -> bool
    checkOverflow(self, int) -> bool

溢出的信号:
    overflow

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('290-QLCDNumber-溢出判定和信号')
        self.resize(1000, 500)

        lcdn = QLCDNumber(2, self)
        lcdn.move(10, 10)
        lcdn.resize(300, 60)

        '''判断是否溢出'''
        print('99是否会溢出:%s' % (lcdn.checkOverflow(99)))
        print('100是否会溢出:%s' % (lcdn.checkOverflow(100)))

        '''设置溢出信号'''
        lcdn.overflow.connect(lambda: print('溢出了'))
        lcdn.display(100)  # 先设置信号, 在设置值


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
