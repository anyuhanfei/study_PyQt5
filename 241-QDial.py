'''
241-QDial

倒圆的范围控制, 比如汽车仪表盘上的速度计

继承自 QAbstractSlider

API: (大多继承自父类)
    是否显示刻度:
        setNotchesVisible(bool)
        notchesVisible() -> bool
    大刻度控制:
        setPageStep(int)
    是否启用包裹:
        setWrapping(bool) -- 启用则会在控件周边都设置上刻度, 可以任意指向
        wrapping() -> bool
    凹口之间的目标像素数:
        setNotchTarget(float)
        notchTarget() -> float
    缺口大小:
        notchSize() -- 默认值为1

信号继承自父类

'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
