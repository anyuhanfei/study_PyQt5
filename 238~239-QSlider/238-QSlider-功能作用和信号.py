'''
238-QSlider-功能作用和信号

垂直或水平滑块
它允许用户沿水平或垂直凹槽移动滑块手柄，并将手柄的位置转换为合法范围内的整数值

继承自 QAbstractSlider

API:
    刻度控制:
        setTickPosition(self, QSlider.TickPosition)
        sd.tickPosition() -> QSlider.TickPosition
        sd.setTickInterval(int) -- 这是值间隔，而不是像素间隔。如果为0，滑块将在singleStep和pageStep之间进行选择
        sd.tickInterval() -> int

附:
    QSlider.NoTicks -- 0 -- 不要画任何刻度线。
    QSlider.TicksBothSides -- 3 -- 在凹槽两侧画刻度线。
    QSlider.TicksAbove -- 1 -- 在（水平）滑块上方绘制刻度线
    QSlider.TicksBelow -- 2 -- 在（水平）滑块下方绘制刻度线
    QSlider.TicksLeft -- 1 -- 在（垂直）滑块的左侧绘制刻度线
    QSlider.TicksRight -- 2 -- 在（垂直）滑块右侧绘制刻度线
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSlider


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('238-QSlider-功能作用和信号')
        self.resize(1000, 500)

        s = QSlider(self)
        s.move(10, 10)

        '''刻度'''
        s.setTickPosition(QSlider.TicksBothSides)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
