'''
291-QLCDNumber-分段样式

API:
    setSegmentStyle(self, QLCDNumber.SegmentStyle)
    segmentStyle(self) -> QLCDNumber.SegmentStyle

附:
    QLCDNumber.Outline -- 生成填充了背景颜色的凸起部分
    QLCDNumber.Filled -- 生成填充前景色的凸起部分。(默认)
    QLCDNumber.Flat -- 生成填充前景色的平坦段。

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLCDNumber


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('291-QLCDNumber-分段样式')
        self.resize(1000, 500)

        lcdn1 = QLCDNumber(2, self)
        lcdn1.move(10, 10)
        lcdn1.resize(300, 60)
        lcdn1.display(99)

        lcdn2 = QLCDNumber(2, self)
        lcdn2.move(10, 100)
        lcdn2.resize(300, 60)
        lcdn2.display(99)
        lcdn2.setSegmentStyle(QLCDNumber.Outline)

        lcdn3 = QLCDNumber(2, self)
        lcdn3.move(10, 190)
        lcdn3.resize(300, 60)
        lcdn3.display(99)
        lcdn3.setSegmentStyle(QLCDNumber.Flat)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
