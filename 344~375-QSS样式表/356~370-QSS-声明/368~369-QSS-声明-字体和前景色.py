'''
368-QSS-声明-字体和前景色

字体:
    统一设置 -- font
    分开设置
        font-family -- 设置字体家族
        font-size -- 字体大小
        font-style -- 字体样式, normal 默认值, italic 斜体, oblique 倾斜字
        font-weight -- 字体粗细, 100~900
文本:
    color -- 字体颜色

最小最大尺寸:
    min-width -- 最大宽度
    min-height -- 最小高度
    max-width -- 最大宽度
    max-height -- 最大高度
'''
import sys

from PyQt5.QtWidgets import QWidget, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle('368-QSS-声明-字体和前景色')
        self.resize(1000, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
