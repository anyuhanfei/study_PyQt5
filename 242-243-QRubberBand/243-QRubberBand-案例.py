'''
243-QRubberBand-案例

在一个空白窗口, 展示多个复选框控件, 通过橡皮筋实现批量选中与取消选中效果
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QRubberBand
from PyQt5.QtCore import QRect, QSize


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('243-QRubberBand-案例')
        self.resize(1000, 500)

        for i in range(0, 36):
            cb = QCheckBox(self)
            cb.move(i % 6 * 40 + 10, i // 6 * 40 + 10)  # X 轴用取余计算, Y 轴用整除计算
            cb.setText(str(i))

    def mousePressEvent(self, evt):
        '''鼠标按下时执行'''
        # 创建一个橡皮筋选中控件
        self.rb = QRubberBand(QRubberBand.Rectangle, self)
        # 鼠标按下的位置
        self.起始位置 = evt.pos()
        self.rb.setGeometry(QRect(self.起始位置, QSize()))  # 起始位置 + 空尺寸
        # 展示橡皮筋控件
        self.rb.show()

    def mouseMoveEvent(self, evt):
        '''鼠标移动时执行'''
        # 调整橡皮筋控件的位置和尺寸
        self.rb.setGeometry(QRect(self.起始位置, evt.pos()).normalized())  # 起始位置 + 鼠标当前位置  normalized() 自动识别尺寸

    def mouseReleaseEvent(self, evt):
        '''鼠标松开时执行'''
        # 获取橡皮筋控件的位置和尺寸
        rect = self.rb.geometry()
        # 遍历所有控件, 康康哪个控件在橡皮筋控件内
        for i in self.children():
            if rect.contains(i.geometry()) and i.inherits('QCheckBox'):  # 包含在橡皮筋控件内 并且是 QCheckBox 控件
                i.toggle()
        # 隐藏橡皮筋控件
        self.rb.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
