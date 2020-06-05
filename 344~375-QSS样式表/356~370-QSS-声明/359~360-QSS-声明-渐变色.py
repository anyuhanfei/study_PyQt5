'''
359-QSS-声明-渐变色

线性渐变:
    qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 white, stop:0.4 gray, stop:1 green)
        x1, y1 表示起始坐标, x2, y2 表示结束坐标,  stop: 后面加 0~1 的值, 表示路程百分比, 后面再跟颜色

辐射渐变:
    qradialgradient(cx:0.7, cy:0.7, radius:0.5, fx:0.5, fy:0.5, stop:0 red, stop:1 orange)
        cx, cy 表示圆心坐标, radius 表示半径, fx, fy 表示光源坐标, stop 与上类似

角度渐变:
    qconicalgradient(cx:0.5, cy:0.5, angle:10, stop:0 red, stop:1 orange)
        cx, cy 表示中心点, angle 表示起始的角度, stop 与上类似
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
