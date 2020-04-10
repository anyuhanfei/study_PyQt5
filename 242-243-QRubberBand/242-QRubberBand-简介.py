'''
242-QRubberBand-简介

提供一个矩形或线来指示选择或边界
一般结合鼠标事件一同协作

继承自 QWidget

构造函数:
    QRubberBand(QRubberBand.Shape, QWidget)

API:
    移动
        move(x, y)
        move(QPoint)
    调整大小:
        resize(width, height)
        resize(QSize)
    统一设置:
        setGeometry(int x, int y, int width, int height)
        setGeometry(QRect rect)
    形状获取:
        shape() -> QRubberBand.Shape

附:
    QRubberBand.Shape
        QRubberBand.Line
        QRubberBand.Rectangle
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QRubberBand


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('242-QRubberBand-简介')
        self.resize(1000, 500)

        rb = QRubberBand(QRubberBand.Rectangle, self)

        '''统一设置大小'''
        rb.setGeometry(10, 10, 60, 60)
        rb.setVisible(True)  # 默认不显示


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
