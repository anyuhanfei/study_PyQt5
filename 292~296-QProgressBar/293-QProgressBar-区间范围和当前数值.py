'''
293-QProgressBar-区间范围和当前数值

API:
    setMinimum(self, int) -- 设置最小值, 默认为0
    minimum() -> int -- 获取最小值
    setMaximum(self, int) -- 设置最大值, 默认为100
    maximum() -> int -- 获取最大值
    setRange(self, int, int) -- 设置区间
    setValue(self, int) -- 设置当前值
    reset() -- 重置当前值
    value() -- 获取当前值

注: 最大值和最小值如果都是0, 则进入繁忙提示


'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QProgressBar


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('293-QProgressBar-区间范围和当前数值')
        self.resize(1000, 500)

        pb = QProgressBar(self)
        pb.move(10, 10)
        '''设置区间'''
        pb.setMinimum(100)
        pb.setMaximum(1000)
        '''设置值'''
        pb.setValue(600)

        pb2 = QProgressBar(self)
        pb2.move(10, 50)
        pb2.setRange(0, 0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
