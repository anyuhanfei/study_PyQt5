'''
356-QSS-声明-边框

控件的边框就是围绕内容和内边距的一条或多条线

每个边框有三个方面: 样式, 宽度, 颜色

样式:
    统一设置 -- border-style: 上 右 下 左
    分开设置 -- border-top-style
                border-right-style
                border-bottom-style
                border-left-style
    常用取值:
        none -- 定义无边框
        dotted -- 定义点状边框
        dashed -- 定义虚线
        solid -- 定义实线
        double -- 定义双线
        groove -- 定义 3D 凹槽边框
        fidge -- 定义 3D 垄状边框
        inset -- 定义 3D inset 边框
        outset -- 定义 3D outset 边框

宽度:
    统一设置 -- border-width: 上 右 下 左
    分开设置 -- border-top-width
                border-right-width
                border-bottom-width
                border-left-width
    常用取值:
        10px
        2em   (1em = 16px)

颜色:
    统一设置 -- border-color
    分开设置 -- border-top-color
                border-right-color
                border-bottom-color
                border-left-color
    常用取值:
        color_name -- red, yellow, green, cyan
        rgb_number -- rgb(255, 0, 255)
        hex_number -- #00ff00

圆角:
    统一设置 -- border-radius (圆角半径)
    分开设置 -- border-top-left-radius
                border-top-right-radius
                border-bottom-right-radius
                border-bottom-left-radius
    常用取值:
        像素值

边框图片:
    border-image: url(图片路径) 四个图片裁剪值 重复
            裁剪值: (由四条线将图片裁剪为9份)
                上 -- 距离上边的线
                右 -- 距离右边的线
                下 -- 距离下边的线
                左 -- 距离左边的线
            重复: (排除四个角, 其他部分的重复策略)
                round -- 平铺
                repeat -- 重复
                stretch -- 拉伸
    例: border-image:url('./xxx.png') 30 30 30 30 repeat

    注意: 需要使用 border-width 辅助确定边框宽度
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('356-QSS-声明-边框')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
