'''
237-QAbstractSlider-信号

API:
    valueChanged() -- 值改变信号
    sliderPressed() -- 滑块被按下
    sliderMoved(int value) -- 滑块移动
    sliderReleased() -- 滑块释放
    actionTriggered(int action) -- 触发一定行为
    rangeChanged(int min，int max) -- 数值范围发生改变

附:
    QAbstractSlider.SliderNoAction
    QAbstractSlider.SliderSingleStepAdd -- 滑块单步步长增加
    QAbstractSlider.SliderSingleStepSub -- 滑块单步步长减少
    QAbstractSlider.SliderPageStepAdd -- 页的步长增加
    QAbstractSlider.SliderPageStepSub -- 页的步长减少
    QAbstractSlider.SliderToMinimum -- 滚动到最小值
    QAbstractSlider.SliderToMaximum -- 滚动到最大值
    QAbstractSlider.SliderMove -- 滑块移动
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSlider


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('237-QAbstractSlider-信号')
        self.resize(1000, 500)

        s = QSlider(self)
        s.move(10, 10)
        s.valueChanged.connect(lambda val: print('值改变了', val))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
