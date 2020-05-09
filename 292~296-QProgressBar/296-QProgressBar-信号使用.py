'''
296-QProgressBar-信号使用

valueChanged(int) -- 值改变时的信息

附:
QTimer

API:
    start(int) -- 定时器开始, int: 定时器每次执行时间
    stop() -- 定时器结束
信号:
    timeout -- 执行时间到了

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar
from PyQt5.QtCore import QTimer


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('296-QProgressBar-信号使用')
        self.resize(1000, 500)

        self.pb = QProgressBar(self)
        self.pb.move(10, 10)
        self.pb.setValue(30)

        '''值改变信号'''
        self.pb.valueChanged.connect(lambda int: print('值改变了, %s' % (int)))

        self.time = QTimer(self.pb)
        self.time.timeout.connect(self._timeout)
        self.time.start(1000)

    def _timeout(self):
        self.pb.setValue(self.pb.value() + 1)
        if self.pb.value() >= self.pb.maximum():
            self.time.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
