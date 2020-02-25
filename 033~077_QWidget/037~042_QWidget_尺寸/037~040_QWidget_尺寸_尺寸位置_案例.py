'''
037~040_QWidget_尺寸_尺寸位置_案例

1. 创建一个窗口, 设置尺寸为500 x 500, 位置为 300, 300

2. 通过给定的的个数, 你负责在一个窗口内创建相应个数的子控件
    按照九宫格的布局进行摆放
'''
import sys

import math

from PyQt5.QtWidgets import QApplication, QWidget


class Window(QWidget):
    child_widget_number = 9  # 子控件数量
    x_widget_number = 3  # 子控件列数
    y_widget_number = 3  # 子控件行数
    child_widget_width = 0  # 子控件的宽
    child_widget_height = 0  # 子控件的高
    width = 500  # 宽
    height = 500  # 高

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 设置宽高，位置
        self.resize(self.width, self.height)
        self.move(300, 300)

    def set_number(self, number: int):
        '''设置子控件个数'''
        self.child_widget_number = number
        self._auto_x_y_widget_number()
        self._auto_child_widget_width_height()

    def run(self):
        self.index()
        self.show()

    def index(self):
        '''设置子控件'''
        number = 0
        for y in range(0, self.y_widget_number):
            for x in range(0, self.x_widget_number):
                # 生成子控件，设置子控件宽高，位置，背景颜色
                chile_qwidget = QWidget(self)
                chile_qwidget.resize(self.child_widget_width, self.child_widget_height)
                chile_qwidget.move(x * self.child_widget_width, y * self.child_widget_height)
                chile_qwidget.setStyleSheet('background-color: red;border: 0.5px solid yellow')
                # 判断子控件数量是否已达到
                number += 1
                if number >= self.child_widget_number:
                    break

    def _auto_x_y_widget_number(self):
        '''自动设置行列最适合数量'''
        for i in range(1, self.child_widget_number):
            if self.child_widget_number <= (i * i):
                self.x_widget_number = i
                break
        self.y_widget_number = math.ceil(self.child_widget_number / self.x_widget_number)

    def _auto_child_widget_width_height(self):
        '''自动设置子控件最适合的宽和高'''
        self.child_widget_width = self.width / self.x_widget_number
        self.child_widget_height = self.height / self.y_widget_number


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.set_number(432)
    window.run()

    sys.exit(app.exec_())
