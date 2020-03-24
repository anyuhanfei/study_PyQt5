'''
138_QFrame_基本功能

QFrame 的功能基本都是设置控件样式，可设置框架形状、框架阴影、框架的几个线宽、框架样式和框架矩形。

可通过多个API来实现一个特殊的样式。

API：
    框架形状：
        setFrameShape(QFrame.Shape) -- 设置框架形状
        frameShape() -> QFrame.Shape -- 获取框架形状
            附：QFrame.Shape：
                QFrame.NoFrame -- QFrame什么都没画
                QFrame.Box -- QFrame围绕其内容绘制一个框
                QFrame.Panel -- QFrame绘制一个面板，使内容显得凸起或凹陷
                QFrame.HLine -- QFrame绘制一条没有框架的水平线（用作分隔符）
                QFrame.VLine -- QFrame绘制一条无框架的垂直线（用作分隔符）
                QFrame.StyledPanel -- 绘制一个矩形面板，其外观取决于当前的GUI样式。它可以升起或凹陷。
                QFrame.WinPanel -- 绘制一个可以像Windows 2000中那样凸起或凹陷的矩形面板。指定此形状可将线宽设置为2像素。WinPanel是为了兼容性而提供的。对于GUI样式独立性，建议使用StyledPanel。

    框架阴影：
        setFrameShadow(QFrame.Shadow) -- 设置框架阴影
        frameShadow() -> QFrame.Shadow -- 获取框架阴影
            附：QFrame.Shadow：
                QFrame.Plain -- 框架和内容与周围环境呈现水平;（没有任何3D效果）
                QFrame.Raised -- 框架和内容出现; 使用当前颜色组的浅色和深色绘制3D凸起线
                QFrame.Sunken -- 框架和内容出现凹陷; 使用当前颜色组的浅色和深色绘制3D凹陷线

    框架的几个线宽：
        setLineWidth(int width) -- 设置外线宽度
        lineWidth() -- 获取外线宽度
        setMidLineWidth(int width) -- 设置中线宽度
        midLineWidth() -- 获取中线宽度
        frameWidth() -- 获取总宽度

    框架样式:
        setFrameStyle(int style) -- 形状和阴影的组合
        frameStyle() -> style -- 获取框架样式

    框架矩形：
        setFrameRect(QRect) -- 设置框架的矩形
        frameRect() -> QRect -- 获取框架的矩形
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFrame
from PyQt5.QtCore import QRect


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('138_QFrame_基本功能')
        self.resize(1000, 500)

        f = QFrame(self)
        f.resize(100, 100)
        f.move(10, 10)
        f.setStyleSheet('background-color: red;')

        '''框架形状'''
        f.setFrameShape(QFrame.Panel)

        '''框架阴影'''
        f.setFrameShadow(QFrame.Sunken)

        '''框架样式'''
        # f.setFrameStyle(QFrame.Panel | QFrame.Sunken)  # 同上两个API的结合版

        '''框架的几个线宽'''
        # 外线宽度
        f.setLineWidth(16)
        # 中线宽度
        f.setMidLineWidth(12)

        '''框架边框'''
        f.setFrameRect(QRect(20, 20, 20, 20))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
