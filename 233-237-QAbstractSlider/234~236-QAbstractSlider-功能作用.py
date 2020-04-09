'''
234~236-QAbstractSlider-功能作用

API:
    数值范围:
        setMaximum(int) -- 设置最大的数值
        maximum() -> int -- 获取最大数值
        setMinimum(int) -- 设置最小数值
        minimum() -> int -- 获取最小数值
    当前数值:
        setValue(int) -- 设置当前数值
        value() -> int -- 获取当前数值
    步长: (键盘有用)
        setPageStep(int) -- 设置页步长 (键盘左右键)
        pageStep() -> int -- 获取页步长
        setSingleStep(int) -- 设置单步步长 (键盘上下键)
        singleStep() -> int -- 获取单步步长
    是否追踪: (在拖拽中时, value 是否跟着改变, 默认为 True)
        setTracking(bool enable)
        hasTracking() -> bool
    滑块位置: (不追踪时, value 值不跟着改变)
        setSliderPosition(int)
        sliderPosition() -> int
    倒立外观:
        setInvertedAppearance(bool)
        invertedAppearance() -> bool
    操作反转:
        setInvertedControls(bool)
        invertedControls() -> bool
    滑块方向:
        setOrientation(Qt.Orientation)
        orientation() -> Qt.Orientation
    是否按下:
        setSliderDown(bool)
        isSliderDown() -> bool

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QLabel


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('234~236-QAbstractSlider-功能作用')
        self.resize(1000, 500)

        self.label = QLabel(self)
        self.label.move(50, 10)
        self.label.resize(100, 30)
        self.label.setText('0')

        s = QSlider(self)
        s.move(10, 10)
        s.valueChanged.connect(lambda val: self.label.setText(str(val)))

        '''数值范围'''
        # 设置最大的数值
        s.setMaximum(100)
        # 设置最小数值
        s.setMinimum(0)
        # 获取最大的数值
        print('获取最大的数值:', s.maximum())
        # 获取最小数值
        print('获取最小数值:', s.minimum())

        '''当前数值'''
        # 设置当前数值
        s.setValue(50)
        # 获取当前数值
        print('获取当前数值:', s.value())

        '''步长'''
        # 设置页步长
        s.setPageStep(10)
        # 获取页步长
        print('获取页步长:', s.pageStep())
        # 设置单步步长
        s.setSingleStep(10)
        # 获取单步步长
        print('获取单步步长:', s.singleStep())

        '''追踪'''
        # 设置为不追踪
        s.setTracking(False)
        # 获取是否跟踪
        print('获取是否跟踪:', s.hasTracking())

        '''滑块位置'''
        # 设置滑块位置, 当设置为不追踪时, 仅仅是修改了滑块的位置, 没有修改值, 想要修改值就需要点击一下滑块(一个看似移动了滑块的操作)
        s.setSliderPosition(10)
        # 获取滑块位置
        print('获取滑块位置:', s.sliderPosition())

        '''倒立外观'''
        # 键盘方向键修改的是值, 滑块的移动仅仅是因为要和值保持一致, 所以倒立外观后对于滑块来说, 需要反向使用键盘的方向键
        s.setInvertedAppearance(True)

        '''操作反转'''
        # 已倒立操作类似.
        s.setInvertedControls(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
