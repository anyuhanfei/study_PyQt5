'''
239-QSlider-案例

在滑块移动时, 通过标签, 展示滑块当前的数值
并要求标签的位置, 一直在滑块所在位置的中间
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QSlider


class Window(QWidget):
    label_x = 16
    label_y = 82

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('239-QSlider-案例')
        self.resize(1000, 500)

        self.slider = QSlider(self)
        self.slider.move(10, 10)
        self.slider.setMaximum(9)

        self.label = QLabel(self)
        self.label.move(self.label_x, self.label_y)
        self.label.setText(str(self.slider.value()))

        self.slider.valueChanged.connect(self._move_slider)

    def _move_slider(self, val):
        '''修改标签的值和位置'''
        self.label.setText(str(self.slider.value()))
        self.label.move(self.label_x, self.label_y - val * 8)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
